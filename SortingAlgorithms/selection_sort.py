def selection_sort(arr):
	out = []
	for x in range(len(arr)):
		sm = arr.pop(smallest(arr))
		out.append(sm)

	return out

def smallest(list):
	smv = list[0]
	smi = 0
	for x in range(1, len(list)):
		if list[x] < smv:
			smv = list[x]
			smi = x
			# print("val", smv)
			# print("in", smi)

	return smi