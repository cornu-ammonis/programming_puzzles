from math import pow

def max_employees(x):
	n = 0
	while (x > 0):
		n  = n + pow(7, x)
		x = x -1
	return n + 1


#test cases. 1 should return 8, 2 should return 57


result = max_employees(1)
print(result)
result = max_employees(2)
print(result)

