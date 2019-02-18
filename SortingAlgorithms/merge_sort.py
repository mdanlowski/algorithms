def merge_sort(arr):
    d = round(len(arr)/2)
    if len(arr) < 2: return arr

    larr = arr[:d]
    rarr = arr[d:]
    
    larr = merge_sort(larr)
    rarr = merge_sort(rarr)

    return merge(larr, rarr)

def merge(l, r):
    # l = ensure_array(l)
    # r = ensure_array(r)
    ret_arr = []

    while len(l) > 0 and len(r) > 0:
        if l[0] <= r[0]: ret_arr.append(l.pop(0))
        else: ret_arr.append(r.pop(0))
        
    if len(l) > 0: return ret_arr + l
    elif len(r) > 0: return ret_arr + r
    else: return ret_arr


# def ensure_array(obj):
#     if type(obj) == type(1):
#         templ = []
#         templ.append(obj)
#         return templ
#     else: return obj


import timeit as t
