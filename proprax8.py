#fizzbuzz

def fizzbuzz(n):
	for i in range(n+1):
		if i % 15 == 0:
			print "FizzBuzz"
		elif i % 5 == 0:
			print "Buzz"
		elif i % 3 == 0:
			print "Fizz"
		else:
			print i

#split a list in half
import math 

def split_list(l):
	halfway = int(math.floor(len(l)/2))
	return l[:halfway], l[halfway:]
