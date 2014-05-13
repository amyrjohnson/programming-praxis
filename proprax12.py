def foursum(l):
	if 0 in l: #0 in list
		return (0,0,0,0)
	if all(item > 0 for item in l) or all(item < 0 for item in l): #all items neg or pos
		print "No Solution"
		return None
	for elem in l:
		if -1*elem in l:  #case 1: one neg and one pos sum to 0
			return (elem, elem, -elem, -elem)
	negatives = []
	positives = []
	for item in l:
		if item>0:
			positives.append(item)
		else:
			negatives.append(item)
	sumgroups(positives, 2) #case
		
	#case 2: two pos and two neg sum to 0 e.g. 1,5,-4,-2
	#case 3: two pos and one neg repeated sum to 0 (and vice versa) e.g. 1,5,-3,-3
	#case 4: three pos and one neg sum to 0 (and vice versa) e.g. 1,2,3,-6
	#case 5: two pos repeated and one neg sum to 0 (and vice versa) e.g. 1,1,4,-6
	#case 6: one pos repeated and one neg sum to 0 (and vice versa) e.g. 2,2,2,-6
		
		
import itertools		
def sumgroups(l,n):
	sums = []
	for c in combinations(l,n):
		if c not in sums:
			sums.append(c)
	return sums