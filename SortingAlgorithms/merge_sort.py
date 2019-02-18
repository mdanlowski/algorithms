def merge_sort(arr):
    d = int(round(len(arr)/2))
    if len(arr) < 2: return arr

    larr = arr[:d]
    rarr = arr[d:]
    
    larr = merge_sort(larr)
    rarr = merge_sort(rarr)

    return merge(larr, rarr)

def merge(l, r):
    ret_arr = []

    while len(l) > 0 and len(r) > 0:
        if l[0] <= r[0]: ret_arr.append(l.pop(0))
        else: ret_arr.append(r.pop(0))
        
    if len(l) > 0: return ret_arr + l
    elif len(r) > 0: return ret_arr + r
    else: return ret_arr
