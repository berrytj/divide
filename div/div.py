
def divide(num, den):
	''' '''

	if den == 0:
		return 'Error', 'Error'
	elif num == 0:
		return 0, 0
	elif den == 1:
		return num, 0

	sign = cmp(num * den, 0)
	inner = 0
	outer = sign * abs(num)

	return find(num, den, inner, outer, sign)


def find(num, den, inner, outer, sign):
	''' '''
	#print 'inner = ' + str(inner) + ', outer = ' + str(outer)
	#mid = divide(inner + outer, 2)
	mid = (inner + outer) // 2
	print 'mid = ' + str(mid)
	estimate = mid * den
	print 'estimate: ' + str(estimate)
	remainder = num - estimate

	if remainder == 0:
		return mid, remainder
	elif cmp(remainder, 0) == cmp(den, 0):
		if 0 < abs(remainder) < abs(den):
			return mid, remainder
		else:
			if sign == 1:
				inner = mid + 1  #outer range if quotient should be positive
			else:
				outer = mid + 1  #narrow range if quotient should be negative
	else:
		if sign == 1:
			outer = mid - 1  #narrow range if quotient should be positive
		else:
			inner = mid - 1  #outer range if quotient should be negative
		

	return find(num, den, inner, outer, sign)











