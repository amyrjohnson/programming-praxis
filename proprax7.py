#find the first non-repeating character in a string

def first_nonrepeat(str):
	for i, c in enumerate(str):
		if c not in str[:i] + str[i+1:]:
			return c
	else:
		print "None"
	