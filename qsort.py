def quicksort( arr ):
	if len(arr) < 2:
		return arr
	else:
		pvti = int(len(arr)/2)
		pvt = arr[pvti]
		less = [x for x in (arr[:pvti]+arr[pvti+1:]) if x <= pvt]
		greater = [x for x in (arr[:pvti]+arr[pvti+1:]) if x > pvt]
		print(pvt)
		return quicksort(less) + [pvt] + quicksort(greater)
		

a = [1,0,58,4,11,1,2]		

print( quicksort(a) )
# print(a[:2])
# print(a[:2+1])
# print(a[:2-1])
