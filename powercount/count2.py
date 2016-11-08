import math 
def time_this(original_function):      
    def new_function(*args,**kwargs):
        import datetime                 
        before = datetime.datetime.now()                     
        x = original_function(*args,**kwargs)                
        after = datetime.datetime.now()                      
        print "Elapsed Time = {0}".format(after-before)      
        return x                                             
    return new_function


def seed_table(bound):
	mylist = [None] * int((bound + 1))
	i = 0 
	
	while i <= bound:
		mylist[i] = 2**i
		i = i + 1
	return mylist 




def H(k, seedtable):
	if k % 2 != 0:
		return 0

	j = int(math.sqrt(k)) 
	while j > 0:
		po = seedtable[j]
		if k % po == 0:
			return j
		j = j - 1
	

@time_this
def countHighestPower(N):
	n = int(N)
	bound = math.sqrt(n)
	seedtable = seed_table(bound)
	i = 2
	count = 0
	while i <= n:
		count = count + H(i, seedtable)
		i = i + 2

	return str(count)


print(countHighestPower("100000000000"))



