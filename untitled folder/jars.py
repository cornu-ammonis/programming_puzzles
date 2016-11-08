def threeGlasses(cap):
	possibilities = []
	amount = 0
	for i in cap:
		amount = amount + i
	possibilities.append(amount)
	print(possibilities[0])


array = [1, 2, 3]
threeGlasses(array)

