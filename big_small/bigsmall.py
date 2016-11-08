import math
def bigSmall(nums):
	minimum = 10
	tempmin = 11
	result = 420
	for x in nums:
		if x > 0:
			tempmin = int(math.log10(x))+1
		elif x == 0:
			
			tempmin = 1
		else:
			tempmin = int(math.log10(-x))+1
		if tempmin < minimum:
			result = x
			minimum = tempmin
		elif tempmin == minimum:
			if x > result:
				result = x

	return result



nums = [-7462, 7346, 9443, 6010, 7143, 1012, -5694, 3852, -5535, 8220, 5861, -9121, -763, -653, -752, -580, 8954, 672, 1745, 1788, 1727, 7981, 2337, 5331, 9908]

print(bigSmall(nums))