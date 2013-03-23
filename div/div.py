
def divide(num, den):
	''' '''

	if den == 0:
		return 'Error'
	elif num == 0:
		return 0, 0
	elif den == 1:
		return num, 0

	sign = cmp(num * den, 0)
	inner = sign
	outer = sign * abs(num)

	find(num, den, inner, outer)


def find(num, den, inner, outer):
	''' '''

	#mid = divide(inner + outer, 2)
	mid = (inner + outer) // 2
	estimate = mid * den
	remainder = estimate - num

	if remainder == 0:
		return mid, remainder
	elif cmp(remainder, 0) == cmp(den, 0):
		if 0 < abs(remainder) < abs(den):
			return mid, remainder
		else:
			outer = mid - 1  #narrow range if quotient should be positive
			#outer range if quotient should be negative
	else:
		inner = mid + 1  #outer range if quotient should be positive
		#narrow range if quotient should be negative

	find(num, den, inner, outer)











