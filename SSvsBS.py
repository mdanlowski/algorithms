# linear search vs binary search performed on a sorted array
import timeit as tm
import numpy.random as rnd

def lsearch(list, item):
	for x in list:
		if item == list[x]: 
			return x
			break
	return None

def bsearch(list, item):
	low = 0
	hi = len(list)-1

	while low <= hi:
		pivot = int((low+hi)/2)
		if list[pivot] == item: return pivot # the item has been found
		if list[pivot] > item:
			hi = pivot-1
		else: # pivot (guess) lower than number in question
			low = pivot+1
	return None


# generate dataset

data = []
for x in range(0,10000000):
	data.append(x)

randy = round(10000000*rnd.rand())

start = tm.default_timer()
##############################
print("searched number will be the same as the index it is under; the number is: " + str(randy))
print("linear search done, index:", lsearch( data, randy ))
##############################
print("linear search time:", tm.default_timer() - start)

start = tm.default_timer()
##############################
print("binary search done, index:", bsearch( data, randy ))
##############################
print("binary search time:", tm.default_timer() - start)
