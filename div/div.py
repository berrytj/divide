
def divide(num, den):
	'''Accept a numerator and a denominator.  Return
	quotient and remainder in special cases.  In all
	other cases, dictate a range of possible solutions
	and initiate binary search.'''

	if den == 0:
		return 'Error', 'Error'
	elif num == 0:
		return 0, 0
	elif den == 1:
		return num, 0

	sign = cmp(num * den, 0)  # The sign that the correct quotient must have.
	outer = sign * abs(num)   # The outside of the range to search within.
	inner = 0                 # The inside of the range to search within.

	return find_quotient(num, den, inner, outer, sign)


def find_quotient(num, den, inner, outer, sign):
	'''Bisect the range of possible solutions, returning
	the bisector if the corresponding remainder is between
	zero and the denominator.  In all other cases, repeat
	binary search on the appropriate half of the range.'''

	mid = (inner + outer) // 2  # Bisect the range being searched.
	remainder = num - mid * den

	if remainder == 0:
		return mid, remainder  # Return solution.

	elif cmp(remainder, 0) == cmp(den, 0):
	# If remainder and denominator have the same sign:

		if 0 < abs(remainder) < abs(den):
			return mid, remainder  # Return solution.

		else:  # If remainder is `absolutely` larger than the denominator:
			if sign == 1:
				# If quotient is positive:
				inner = mid + 1  # Search outer range.
			else:
				# If quotient is negative:
				outer = mid + 1  # Search inner range.

	else:  # If remainder has a different sign than the denominator:

		if sign == 1:
			# If quotient is positive:
			outer = mid - 1  # Search inner range.
		else:
			# If quotient is negative:
			inner = mid - 1  # Search outer range.
	
	return find_quotient(num, den, inner, outer, sign)




