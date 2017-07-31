def rsum(list):
	if list == []:
		return 0

	else:
		return list[0] + rsum(list[1:])

arr = [1,2,3,5]
print(rsum(arr))