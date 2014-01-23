#determine if two strings are rotations of each other ("catdog" == "dogcat","catdog" != "odgcat")

def is_rotation(str1, str2):
	if len(str1) != len(str2):
		return False
	for char in str2:
		if char not in str1:
			return False
	count = 0
	while count <= len(str1):
		str2 = str2[1:] + str2[0]
		if str2 == str1:
			return True
		count += 1
	return False

			