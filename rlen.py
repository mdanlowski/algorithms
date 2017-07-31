def rlen(list):
	if list == []:
		return 0
	else:
		return 1 + rlen(list[1:])

###
print(rlen([1,4,0]))