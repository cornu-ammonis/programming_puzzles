def time_this(original_function):      
    def new_function(*args,**kwargs):
        import datetime                 
        before = datetime.datetime.now()                     
        x = original_function(*args,**kwargs)                
        after = datetime.datetime.now()                      
        print "Elapsed Time = {0}".format(after-before)      
        return x                                             
    return new_function

def recur(n):
	y = int(n/2)
	if n > 0:
		return y + recur(y)
	else:
		return 0

@time_this
def countHighestPower(N):
	n = int(N)

	return str(recur(n))

print(countHighestPower("100000000000"))


