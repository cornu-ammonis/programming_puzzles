#compute a volume given an array of current volumes - the primary methods pass around a "cap"
 # array, which is what is originally given to the method and defines maximum volumes for cup i where cap[i] = max,
 # and also various amounts or working_amount arrays which represent the *current* volume at that point in the tree of 
 # possible operations. compute total simplifies the process of adding those possible voluems to a list.

def compute_total(array):
	total = 0
	for x in array:
		total = total + x
	return total

#no longer relevant
def compute_totals(array):
	totals = []
	for x in array:
		amt = compute_total(x)
		if amt not in totals:
			totals.append(amt)
	return totals



#cap is each cups maximum and amounts is the current amount of water in each cup, pours water from isource into itarget
#until either itarget is full or isource is empty
def pour(cap, amounts, itarget, isource):
	while (amounts[itarget] < cap[itarget] and amounts[isource] > 0):
		amounts[itarget] = amounts[itarget] + 1
		amounts[isource] = amounts[isource] - 1
	return amounts

#given a current state of volumes in each cup, determines whether that possible volume has already been added to the list 
# and adds if it has not been. distinction between possibilities and totes - possibilities is a list
# of  the raw arays of a particular set of volumes, eg [3, 4, 5] -- totes a list of the total volumes, eg (12). 
# possibliities is used for memoization, such that recursion stops if a current state has alread been passed through 
# recursion once before. this possibilities has duplicates of total volumes, whereas totes may have only one copy of a 
# particular volume, its length is used to return the int representing total number of possibilities
def add_possibility(amounts, possibilities):
	a = compute_total(amounts)
	if amounts not in possibilities and a != 0:
		possibilities.append(amounts)
	if a not in totes and a != 0:
		totes.append(a)
	return possibilities

#given a current state of volumes, explores all possibilities involving emptying either one or two 
# of the cups, and then passes those volume states back to the recursive function
def empty(cap, amounts, possibilities):
	w_amounts = amounts[:]
	
	for i in range(len(amounts)):
		if w_amounts[i] != 0:

			w_amounts[i] = 0
			if w_amounts not in possibilities:
				possibilities = recur(cap, w_amounts, possibilities)
		z_amounts = w_amounts[:]
		for y in range(len(amounts)):
			if y != i and w_amounts[y] != 0:
				w_amounts[y] = 0
				if w_amounts not in possibilities:
					possibilities = recur(cap, w_amounts, possibilities)
				
				w_amounts = z_amounts[:]
		
		w_amounts = amounts[:]
	return possibilities




def recur(cap, amounts, possibilities):
	amount = compute_total(amounts)

	if amount == 0:
		return possibilities
	else:
		possibilities = add_possibility(amounts, possibilities)
		
		working_amounts = amounts[:]

		#checks if any of the cups contains less than tehir maximum -- if they do, pouring is possible
		# and so the loops explore all pouring possibilities, exploring emptying sub possibilities with each 
		# subsequent state. else, simply call the empty function to explore all possiblities of emptying cups from current
		# state,, because pouring is not possible yet in that case.
		if working_amounts[0] < cap[0] or working_amounts[1] < cap[1] or working_amounts[2] < cap[2]:
			for i in range(len(working_amounts)):
				if working_amounts[i] < cap[i]:
					for y in range(len(working_amounts)):
						if y!=i and working_amounts[y] > 0:
							working_amounts = pour(cap, working_amounts, i, y)
							if working_amounts not in possibilities:
								possibilities = recur(cap, working_amounts, possibilities)
							possibilities = empty(cap, working_amounts, possibilities)
							working_amounts = amounts[:]
							
								

		else:
			possibilities = empty(cap, working_amounts, possibilities)


		return possibilities

def preprocess(cap):
	kind = "undefined"
	num_even = 0
	#if (cap[0] % 2 == 0) and (cap[1] % 2 == 0) and (cap[2] % 2 == 0)
	for x in cap:
		if x % 2 == 0:
			num_even = num_even + 1

	if num_even == 3:
		kind = "all_even"
		maximum  = compute_total(cap)
		minimum = min(cap)
		i = maximum
		while (i >= minimum):
			totes.append(i)
			i = i - minimum
		for x in cap:
			if (maximum - x) % minimum  != 0 and x!= minimum:
				print "error case"
				y = cap.index(x)
				new_cap = cap[:]
				new_cap[y] = 0
				new_max = compute_total(new_cap)
				for a in new_cap:
					if a != 0 and a != minimum:
						third_value = a
				z = new_max
				while (z > 0):
					if z not in totes:
						totes.append(z)
					z = z - minimum
				z = new_max
				while(z > 0):
					if z not in totes:
						totes.append(z)
					z = z - third_value
				z = new_max
				while (z > 0):
					if z not in totes:
						totes.append(z)
					z = z - abs(third_value - cap[y])
				z = new_max
				while (z > 0):
					if z not in totes:
						totes.append(z)
					b = (third_value - (cap[y] - minimum))
					if b <= 0:
						z = 0
					else:
						z = z - b


	return kind





def threeGlasses(cap):
	
	possibilities = []
	amounts = cap[:]
	#adds initial total amount to list
	#possibilities.append(compute_total(amounts))
	
	#if any cup = 1 capacity, the number of possible volumes = the total starting volume
	for x in cap:
		if x == 1:
			return compute_total(cap)

	
	possibilities = recur(cap, amounts, possibilities)

	

	#totes contains one copy of each possible volume produced, so its length is the answer
	#return str(len(totes)) + str(totes)
	return len(totes)

def threeGlasses_pre(cap):
	
	possibilities = []
	
	kind = ""
	kind = preprocess(cap)
	if (kind == "all_even"):
		#return str(len(totes)) + str(totes)
		print "used all even"
		return len(totes)

	amounts = cap[:]
	possibilities = recur(cap, amounts, possibilities)

	#totes contains one copy of each possible volume produced, so its length is the answer
	#return str(len(totes)) + str(totes)
	return len(totes)

def verify_principle(cap):
	
	return_bool = True
	maximum = max(cap)
	ans = threeGlasses(cap)

	i = 1
	while( i <= maximum):
		if i not in totes:
			return_bool = False
		i = i + 1

	return "for cap: " + str(cap) + "answer = " + ans + "and verification = " + str(return_bool)



test = [12, 50, 100]
totes = []
#print(threeGlasses(test))

original = threeGlasses(test)
print(original)
totes = []
new = threeGlasses_pre(test)

if (new == original):
	print "success: " + str(new)
else:
	print "Failure " + str(new)



