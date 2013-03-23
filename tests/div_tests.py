
from nose import *
from div import divide

def test_divide():

	for num in range(0, 10):
		for den in range(0, 10):
			exp_quotient = num // den
			exp_remainder = num % den
			quotient, remainder = divide(num, den)

			assertEqual(exp_quotient, quotient)
			assertEqual(exp_remainder, remainder)