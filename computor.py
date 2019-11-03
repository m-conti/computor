import regex
import re


class Polynome:

	def __init__(self, pol):
		self.a = 0
		self.b = 0
		self.c = 0
		self.elements = []

		self.inscribe(pol)

	def __str__(self):
		return 'a = {a} | b = {b} | c = {c}'.format(a=self.a, b=self.b, c=self.c)

	def inscribe(self, pol):
		self.split_elements(pol)
		self.parse_elements()

	def split_elements(self, part):
		self.elements = list(filter(lambda elem: elem[0] or elem[1], re.findall(regex.part, part)))
		print(self.elements)

	def parse_elements(self):
		after_equality = False
		subtract = False
		for element in self.elements:
			(value, unknown, power, operand) = element
			number = float(value) if not subtract else -float(value)
			self.set_value(number, unknown, power)
			(subtract, after_equality) = self.set_operand(operand, after_equality)

	def set_value(self, number, unknown, power):
		if unknown and power == '2':
			self.a += number
		elif unknown and (not power or power == '1'):
			self.b += number
		elif not unknown or (unknown and power == '0'):
			self.c += number

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

# bug {+nb|-nb}
tests = [
	'1 * x ^ 2 + 2 * x + 3 = 0',
	'1 x ^ 2 + 2 * x + 3 = 0',
	'1*x^2 + 2 * x + 3 = 0',
	'1x^2 + 2 * x + 3 = 0',
	'1 * x ^ 2 + 2 * x ^ 1 + 3 = 0',
	'1 * x ^ 2 + 2*x^1 + 3 = 0',
	'1 * x ^ 2 + 2 * x + 3 * x ^ 0 = 0',
	'1 * x ^ 2 + 2 * x + 3*x^0 = 0',
	'1 * x ^ 2 + 2 * x = -3',
	'1 * x ^ 2 = -2 * x + -3',
	'0 = -1 * x ^ 2 - 2 * x + -3',
]

for test in tests:
	try:
		#pol = Polynome(test)
		#print(pol)
		for match in re.finditer(regex.part, test):
			print(match.groupdict())
	except Exception as error:
		print('Error : ' + str(error))
