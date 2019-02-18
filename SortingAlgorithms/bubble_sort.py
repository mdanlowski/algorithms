def bubble_sort(arr):
    sort_done = False
    swap = 0
    
    while(not sort_done):   
        sort_done = True
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                sort_done = False
                swap = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = swap

    return arr