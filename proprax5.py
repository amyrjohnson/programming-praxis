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
	
# Reverse Words: Given a list of space separated words, reverse the order of the words.
#  Each input string contains L letters and W words. An input string will only consist 
#  of letters and space characters. There will be exactly one space character 
# between each pair of consecutive words


def reverse_words(str):
	reverse = ""
	words = str.split(" ")
	words.reverse()
	newwords = " ".join(words)
	print newwords
	
# T9 Spelling: The Latin alphabet contains 26 characters and telephones only have ten 
# digits on the keypad. We would like to make it easier to write a message to your friend
# using a sequence of keypresses to indicate the desired characters. The letters are mapped 
# onto the digits as 2=ABC, 3=DEF, 4=GHI, 5=JKL, 6=MNO, 7=PQRS, 8=TUV, 9=WXYZ. To insert 
# the character B for instance, the program would press 22. In order to insert two characters


def T9(words):
	d = {}
	for a,b in zip(['A','D','G','J','M','P','T','W'], range(2,10)):
		d[a] = str(b)
	for a,b in zip(['B','E','H','K','N','Q','U','X'], [22,33,44,55,66,77,88,99]):
		d[a] = str(b)
	for a,b in zip(['C','F','I','L','O','R','V','Y','S','Z'],[222,333,444,555,666,777,888,999,7777,9999]):
		d[a] = str(b)
	d[" "] = '0'
	last = 1
	t9 = ''
	for char in words.upper():
		print char, d[char]
		if last == d[char][0] and d[char]!= '0':
			t9 += " "
		t9 += d[char]
		last = d[char][0]
	return t9

