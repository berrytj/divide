
from nose.tools import *
from div.div import divide

def test_divide():
	'''Test the `divide` function by inputting a wide
	range of integers and comparing the outcomes with
	the results of performing native calculations.'''

	# Test a wide range of both positive and negative integers.
	ints = range(-1050, -950) + range(-100, 100) + range(950, 1050)

	for num in ints:
		for den in ints:

			if den == 0:
				exp_quotient = 'Error'
				exp_remainder = 'Error'
			else:
				exp_quotient = num // den
				exp_remainder = num % den

			quotient, remainder = divide(num, den)

			assert_equal(exp_quotient, quotient)
			assert_equal(exp_remainder, remainder)
			

