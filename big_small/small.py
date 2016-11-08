def bigSmall(nums):
	m = 10
	r =  min(nums)
	for x in nums:
		t = len(str(abs(x)))
		if t <= m:
			m = t
		if x > r:
			r = x
	return r



nums = [1, 2, 3]
print(bigSmall(nums))