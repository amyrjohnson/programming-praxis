# Store Credit: You receive a credit C at a local store and would like to buy two items. 
# You first walk through the store and create a list L of all available items. 
# From this list you would like to buy two items that add up to the entire value of the credit. 
# The solution you provide will consist of the two integers indicating the positions of the 
# items in your list (smaller number first). For instance, with C=100 and L={5,75,25} the 
# solution is 2,3; with C=200 and L={150,24,79,50,88,345,3} the solution is 1,4; and with 
# C=8 and L={2,1,9,4,4,56,90,3} the solution is 4,5.



def store_credit(C,L):
	items = []
	for item in L:
		if item != C/2 and C-item in L:
			items.append(L.index(item)+1)
			items.append(L.index(C-item)+1)
			return items
		if item == C/2:
			list2 = L[L.index(item)+1:]
			if C-item in list2:
				items.append(L.index(item)+1)
				items.append(list2.index(item)+items[0]+1)
				return items
	print "No Solution"
