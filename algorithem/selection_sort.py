def selection_sort(arr) :
    for i in range(len(arr)) :
        min_idx = i
        for j in range(i+1, len(arr)) :
            if arr[min_idx] > arr[j] :
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print('Selection sort: the sorted array is', arr)
