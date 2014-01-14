# Consider an n-digit number k. Square it and add the right n digits to the left n or 
# n-1 digits. If the resultant sum is k, then k is called a Kaprekar number. For example, 
# 9 is a Kaprekar number since 92 = 81 and 8 + 1 = 9 and 297 is a Kaprekar number since 
# 2972 = 88209 and 88 + 209 = 297.
# 
# Your task is to write a function that identifies Kaprekar numbers and to determine
#  the Kaprekar numbers less than a thousand. When you are finished, you are welcome 
#  to read or run a suggested solution, or to post your own solution or discuss the 
#  exercise in the comments below.

def joinnums(l):
	num = ""
	for elem in l:
		num += elem
	return int(num)

def IsKaprekar(num):
	kaprekar = False
	digits = list(str(num**2))
	if num == 1:
		kaprekar = True
		return kaprekar
	if len(digits) < 2 and num != 1:
		return kaprekar
	elif len(digits) % 2 == 0:
		halfway = len(digits)/2
	elif len(digits) % 2 == 1:
		halfway = (len(digits)-1)/2
	kaprekar1 = joinnums(digits[:halfway])
	kaprekar2 = joinnums(digits[halfway:])
	if kaprekar1 + kaprekar2 == num:
		kaprekar = True
	return kaprekar
	
	
def kaprekars(limit):
	kknums = []
	for n in range(limit):
		if IsKaprekar(n) == True:
			kknums.append(n)
	return kknums
	
	
