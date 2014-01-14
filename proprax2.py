# Write a function to reverse a string.
# Write a function to compute the Nth fibonacci number.
# Print out the grade-school multiplication table up to 12 x 12.
# Write a function that sums up integers from a text file, one per line.
# Write a function to print the odd numbers from 1 to 99.
# Find the largest int value in an int array.
# Format an RGB value (three 1-byte numbers) as a 6-digit hexadecimal string.

import sys

def reversestr(string):
	reverse = ""
	charlist = list(string)
	for char in charlist:
		reverse = char + reverse 
	return reverse
	
def fibonacci(n):
	if n == 1:
		return 0
	if n == 2:
		return 1
	if n >=3:
		fib1 = ""
		fib2 = 1
		fib3 = 0
		for num in range(2,n):
			fib1 = fib2 + fib3
			fib3 = fib2
			fib2 = fib1
		return fib1
	else:
		print "Error"

		
def timestable():
	for num in range(13):
		for n in range (13):
			print str(num) + ' x ' + str(n) + ' = ' + str(n*num)

		
def sumints(file):
	f = open(file, 'r')
	sum = 0
	for line in f:
		num = int(line.strip('\n'))
		sum += num
	return sum

def printodds():
	for num in range(100):
		if num % 2 == 1:
			print num

def largestint(l):
	largest = None
	for num in l:
		if num > largest:
			largest = num
	return largest

def hex(rgb):
	pass
		