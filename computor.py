import regex

class Polynome:

	def __init__(self, pol):
		self.a = 0
		self.b = 0
		self.c = 0
		self.elements = []

		self.inscribe(pol)

	def inscribe(self, pol):
		equalities = self.split_equality(pol)

		self.split_elements(equalities[0], False)
		self.split_elements(equalities[1], True)

		for element in self.elements:
			self.parse_element(element)

	@staticmethod
	def split_equality(pol):
		equalities = []

		if len(equalities) != 2:
			raise Exception('" {} " is not an equation.'.format(pol))
		return equalities

	def split_elements(self, array, after_equal):
		pass

	def parse_element(self, element):
		pass


tests = [
	'',
]

for test in tests:
	try :
		Polynome(test)
	except Exception as error:
		print(error.message)
