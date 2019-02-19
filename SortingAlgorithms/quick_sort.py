def quick_sort(arr):
	if len(arr) < 2:
		return arr
	else:
		pvti = int(len(arr)/2)
		pvt = arr[pvti]
		less = [x for x in (arr[:pvti]+arr[pvti+1:]) if x <= pvt]
		greater = [x for x in (arr[:pvti]+arr[pvti+1:]) if x > pvt]
		return quick_sort(less) + [pvt] + quick_sort(greater)


