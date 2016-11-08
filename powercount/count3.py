def time_this(original_function):      
    def new_function(*args,**kwargs):
        import datetime                 
        before = datetime.datetime.now()                     
        x = original_function(*args,**kwargs)                
        after = datetime.datetime.now()                      
        print "Elapsed Time = {0}".format(after-before)      
        return x                                             
    return new_function

def H(k):
	p = 2 
	x = 0 
	while p <= k:
		if k % p != 0:
			return x
		p = p + p
		x = x + 1
	return x

@time_this
def countHighestPower(N):
	n = int(N)
	i = 2 
	count = 0 
	while i <= n:
		count = count + H(i)
		i = i + 2
	return str(count)


print(countHighestPower("100000000"))
