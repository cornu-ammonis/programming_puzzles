import datetime 


def recur(n):
	y = int(n/2)
	if y > 0:
		return y + recur(y)
	else:
		return 0


def countHighestPower(N):
	n = int(N)

	return str(recur(n))


def time(N):
	before = datetime.datetime.now()
	ans = countHighestPower(N)
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

doubling(10000000000)
		


