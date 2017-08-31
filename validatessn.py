def ssn(num):
	if len(num) != 11:
		return False
	for a in range(0,3):
		if  num[a].isdecimal() is False:
			return False
	if num[3]!="-":
		return False
	for b in range(4,6):
		if  num[b].isdecimal() is False:
			return False
	if num[6]!="-":
		return False
	for c in range(7,11):
		if  num[c].isdecimal() is False:
			return False
		
	return True

	

print(ssn("123-45-6789"))
