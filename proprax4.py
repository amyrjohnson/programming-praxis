# This exercise is part of our on-going series of interview questions:
# 
# Given two strings, determine if all the characters in the second string appear in the first string;
#  thus, DA is a subset of ABCD. Counts matter, so DAD is not a subset of ABCD, 
#  since there are two D in the second string but only one D in the first string. You may 
#  assume that the second string is no longer than the first string.
# 
# Your task is to write a function to determine if one string is a subset of another string. 
# You should work as you would in a programming interview; if you find one solution, 
# search for a better solution. When you are finished, you are welcome to read or run a 
# suggested solution, or to post your own solution or discuss the exercise in the comments below.


def substring(str1,str2):
	d = {}
	for char in str2:
		if char in d:
			d[char] += 1
		else:
			d[char] = 1
	for char in str1:
		if char in d:
			if d[char] > 1:
				d[char] -= 1
			else:
				del d[char]
		else:
			return False
	return True
