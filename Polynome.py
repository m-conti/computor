import regex
import re
import math
import cmath


class Polynome:

	def __init__(self, pol):
		self.a = 0
		self.b = 0
		self.c = 0
		self.elements = []

		if re.match(regex.equation, pol).group() != pol:
			raise Exception('Error !')
		self.inscribe(pol)

	def __str__(self):
		return 'a = {a:g} | b = {b:g} | c = {c:g}'.format(a=self.a, b=self.b, c=self.c)

	# b² − 4ac
	@property
	def delta(self):
		return self.b * self.b - 4 * self.a * self.c

	@property
	def reduced(self):
		parts = []
		if self.a:
			parts.append('{:g} * x² '.format(self.a))
		if self.b:
			parts.append('{:g} * x '.format(self.b))
		if self.c:
			parts.append('{:g} '.format(self.c))
		if parts:
			return '{}= 0'.format('+ '.join(parts))
		return '0 = 0'

	@property
	def degree(self):
		if self.a:
			return 2
		elif self.b:
			return 1
		return 0

	def inscribe(self, pol):
		self.split_elements(pol)
		self.parse_elements()

	def split_elements(self, part):
		self.elements = [match.groupdict() for match in re.finditer(regex.part, part)]

	def parse_elements(self):
		after_equality = False
		subtract = False
		for element in self.elements:
			if element['is_unknown']:
				if element['unknown']:
					number = float(element['unknown']) if not subtract else -float(element['unknown'])
				else:
					number = 1.0 if not subtract else -1.0
				if element['negate_unknown']:
					number = -number
			else:
				number = float(element['number']) if not subtract else -float(element['number'])
			self.set_value(number, element['is_unknown'], element['power'])
			(subtract, after_equality) = self.set_operand(element['operand'], after_equality)

	def set_value(self, number, unknown, power):
		if unknown and power == '2':
			self.a += number
		elif unknown and (not power or power == '1'):
			self.b += number
		elif not unknown or (unknown and power == '0'):
			self.c += number
		elif float(power) % 1:
			raise Exception('{} isn\'t a correct exponent'.format(power))
		elif int(power) > 2:
			raise Exception('the exponent {} is greater than 2. I can\' solve it.'.format(power))
		elif int(power) < 0:
			raise Exception('the exponent {} is smaller than 0. I can\' solve it.'.format(power))

	@staticmethod
	def set_operand(operand, after_equality):
		if operand == '+':
			return after_equality, after_equality
		if operand == '-':
			return not after_equality, after_equality
		if operand == '=':
			if after_equality:
				raise Exception('So many " = "')
			return True, True
		if not after_equality:
			raise Exception('It\'s not an equation')
		return False, True

	def resolve(self):
		if self.delta > 0:
			return 'positive', [
				'x1 = ' + str(-self.b + math.sqrt(self.delta) / (2 * self.a)),
				'x2 = ' + str(-self.b - math.sqrt(self.delta) / (2 * self.a)),
			]
		elif self.delta == 0:
			return 'null', ['x = ' + str(-self.b / (2 * self.a))]
		else:
			return 'negative', [
				'x1 = ' + str(-self.b + cmath.sqrt(self.delta) / (2 * self.a)),
				'x2 = ' + str(-self.b - cmath.sqrt(self.delta) / (2 * self.a)),
			]

	def solution(self):
		if self.degree == 0:
			return 'we have no solution' if self.c else 'we don\'t have unknown and the equation is solved'
		if self.degree == 1:
			return 'we have 1 solution : {:g}'.format((-self.c / self.b) + 0)
		(discriminant, solutions) = self.resolve()
		return 'the discriminant is {0}, we have {1} solution(s) :\n{2}'.format(
				discriminant,
				len(solutions),
				'\n'.join(solutions)
		)
