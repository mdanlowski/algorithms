# Selection sort implementation

import numpy.random as rnd
import matplotlib.pyplot as pl

#==========================
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

def selSort(arr):
	out = []
	for x in range(0, len(arr)):
		sm = arr.pop(smallest(arr))
		out.append(sm)

	return out
#==========================

data = []
for x in range(0, 1000):
	data.append(1000*rnd.rand())

srt = selSort(data)

pl.hist(srt)
pl.show()