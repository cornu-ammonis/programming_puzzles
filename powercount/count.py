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




def H(k, seedtable, bound):
	if k % 2 != 0:
		return 0
	if k % 4 !=0:
		return 1
	if k % 8 !=0:
		return 2
	if k % 16 !=0:
		return 3
	if k % 32 !=0:
		return 4
	if k % 64 !=0:
		return 5
	if k % 128 !=0:
		return 6
	if k % 256 !=0:
		return 7
	temp = 0
	j = 8
	while j < bound:
		po = seedtable[j]
		if k % po == 0:
			temp = j
		if po >= k:
			return temp
		j = j + 1
	return temp

@time_this
def countHighestPower(N):
	n = int(N)
	bound = math.sqrt(n)
	seedtable = seed_table(bound)
	i = 2
	count = 0
	while i <= n:
		count = count + H(i, seedtable, bound)
		i = i + 2

	return str(count)


print(countHighestPower("100000000"))



