# Write a program that takes a list of integers and a target number and determines
# if any two integers in the list sum to the target number. If so, return the two numbers.
# If not, return an indication that no such integers exist.

def sumtarget(numbers, target):
	used = False
	for num in numbers:
		if target-num in numbers and num != target/2:
			return num, target-num
		if num == target/2:
			if used:
				return num, num
			used = True
	print "No Solution"
	

print sumtarget([2,2,2,2,2,2,2,2],4)
print sumtarget([1,8,3,6,5,5,5,1,4],9)
print sumtarget([10,5,5,4,2,10],20)
print sumtarget([10,15,5,10],20)
print sumtarget([3,3,3],10)
