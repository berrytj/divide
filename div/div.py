
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