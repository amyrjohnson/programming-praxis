#reverse sublists of size k

def reverse_sublists(l, k):
	sublists = []
	reversed_list = []
	i = 0
	while i <= len(l)/k:
		try:
			sublists.append(l[k*i:k*(i+1)])
			i+= 1
		except IndexError:
			sublists.append(l[k*i:])
			i+=1
	for sublist in sublists:
		sublist.reverse()
		reversed_list.extend(sublist)
	return reversed_list

