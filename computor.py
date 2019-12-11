from Polynome import Polynome
import sys

# bug {+nb|-nb}
tests = [
	'1 * x ^ 2 + 2 * x + 3 = 0',
	'1 x ^ 2 + 2 * x + +3 = 0',
	'1*x^2 + 2 * x - 3 = 0',
	'1x^2 + 2 * x + -3 = 0',
	'1 * x ^ 2 + 2 * x ^ 1 - 3 = 0',
	'1 * x ^ 2 + 2*x^1 + -3 = 0',
	'1 * x ^ 2 + 2 * x + -3 * x ^ 0 = 0',
	'1 * x ^ 2 + 2 * x - 3*x^0 = 0',
	'1 * x ^ 2 + 2 * x = 3',
	'1 * x ^ 2 = -2 * x + 3',
	'0 = -1 * x ^ 2 - 2 * x + +3',
	'x^2 + 2 * x - 3 = 0',
	'-1 * x ^ 2 + 2 * x + -3 = -2 * x^2',
	'-x ^ 2 + 2 * x - 3 = -2 * x^2',
	'1 * x ^ 2 + x + -3 = -x',
	'2 * x^2 = 0'
]


def print_solution(pol, str_in):
	print('polynomial: ' + str_in)
	print('Polynomial degree: ' + str(pol.degree))
	print(pol.reduced)
	print(pol.solution())


def do_test():
	for test in tests:
		try:
			pol = Polynome(test)
			print_solution(pol, test)
		except Exception as error:
			print('Error : ' + str(error))


if __name__ == '__main__':
	if len(sys.argv) <= 1:
		print('no argument pass.')
	elif sys.argv[1] == 'tests':
		do_test()
	else:
		for arg in sys.argv[1:]:
			try:
				pol = Polynome(arg)
				print_solution(pol, arg)
			except Exception as error:
				print('Error : ' + str(error))
