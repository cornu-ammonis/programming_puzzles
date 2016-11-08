from math import pow
import datetime

def max_employees(x):
	n = 0
	while (x > 0):
		n  = n + pow(7, x)
		x = x -1
	return n + 1


#test cases. 1 should return 8, 2 should return 57

def time(N):
	before = datetime.datetime.now()
	ans = max_employees(N)
	after = datetime.datetime.now()
	print ans
	return (after - before)


def doubling(N):
	prev = time(N)
	while(N < 20000000000000):
		N = N * 2
		t = time(N)
		s = "{0} {1} {2}\n".format(N, t, t.total_seconds()/prev.total_seconds())
		print s 
		prev = t

doubling(1)
		

