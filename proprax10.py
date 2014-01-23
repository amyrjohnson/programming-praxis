# remove all duplicate chars from a string ('aaabbb' ==> 'ab')

def no_dups(str):
	newstr = ""
	used = []
	for c in str:
		if c not in used:
			used.append(c)
			newstr += c
	return newstr
	
# remove consecutive spaces from a string

def single_space(str):
	newstr = ""
	for i, c in enumerate(str):
		print c, i
		if c == " " and i < (len(str) -1):
			if str[i+1] == " ":
				pass
			else:
				newstr += c
		else:
			newstr += c
	return newstr
