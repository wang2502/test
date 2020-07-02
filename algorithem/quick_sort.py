def partition(arr, low, high) :
    i = (low-1)
    pivot = arr[high]
    for j in range(low, high) :
        if arr[j] <= pivot :
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quickSort(arr, low, high) :
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi + 1, high)

def quickSortIterative(arr, l, h) :
    size = h - l + 1
    stack = [0] * size

    top = -1

    top += 1
    stack[top] = l
    top += 1
    stack[top] = h

    while top >= 0 :
        h = stack[top]
        top -= 1
        l = stack[top]
        top -= 1

        p = partition(arr, l, h)

        if p-1 > l :
            top += 1
            stack[top] = l
            top += 1
            stack[top] = p - 1

        if p+1 < h :
            top += 1
            stack[top] = p + 1
            top += 1
            stack[top] = h

arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n-1)
print('Quick sort: the sorted array is', arr)
quickSortIterative(arr, 0, n-1)
print('Iterative quick sort: the sorted array is', arr)
