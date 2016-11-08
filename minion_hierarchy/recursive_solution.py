import datetime
def max_employees(x):
	if x < 0 :
		return 0
	if x == 0:
		return 1
	else:
		n = max_employees(x-1)
		return (7*(n-max_employees(x-2)) + n)

def time(N):
	before = datetime.datetime.now()
	ans = max_employees(N)
	after = datetime.datetime.now()
	print ans
	return (after - before)


def doubling(N):
	prev = time(N)
	while(N < 100):
		N = N * 2
		t = time(N)
		s = "{0} {1} {2}\n".format(N, t, t.total_seconds()/prev.total_seconds())
		print s 
		prev = t

doubling(1)
		


