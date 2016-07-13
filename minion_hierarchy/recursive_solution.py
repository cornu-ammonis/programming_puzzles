def max_employees(x):
	if x < 0 :
		return 0
	if x == 0:
		return 1
	else:
		n = max_employees(x-1)
		return (7*(n-max_employees(x-2)) + n)

#test cases. 1 should return 8, 2 should return 57


#result = max_employees(1)
#print(result)
#result = max_employees(2)
#print(result)


