def quicksort( arr ):
	if len(arr) < 2:
		return arr
	else:
		pvti = int(len(arr)/2)
		pvt = arr[pvti]
		less = [x for x in (arr[:pvti]+arr[pvti+1:]) if x <= pvt]
		greater = [x for x in (arr[:pvti]+arr[pvti+1:]) if x > pvt]
		return quicksort(less) + [pvt] + quicksort(greater)

import numpy.random as rnd		

# a = [1,0,0,0,58,4,-15,11,1,2,152]		
x = [int(x*rnd.rand()) for x in range(0, 100)]

print( quicksort(x) )

