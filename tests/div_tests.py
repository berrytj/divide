
from nose import *
from div.div import divide

def test_divide():

	for num in range(0, 10):
		for den in range(0, 10):
			
			if den == 0:
				exp_quotient = 'Error'
				exp_remainder = 'Error'
			else:
				exp_quotient = num // den
				exp_remainder = num % den

			quotient, remainder = divide(num, den)

			assertEqual(exp_quotient, quotient)
			assertEqual(exp_remainder, remainder)