
from nose.tools import *
from div.div import divide

def test_divide():

	for num in range(-10, 10):
		for den in range(-10, 10):

			if den == 0:
				exp_quotient = 'Error'
				exp_remainder = 'Error'
			else:
				exp_quotient = num // den
				exp_remainder = num % den

			print 'num: ' + str(num) + ', den: ' + str(den)
			quotient, remainder = divide(num, den)

			assert_equal(exp_quotient, quotient)
			assert_equal(exp_remainder, remainder)