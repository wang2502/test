def insertionSort(arr) :
    for i in range(1, len(arr)) :
        key = arr[i]
        j = i-1
        while j>=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key

def insertionRecursive(arr, n) :
    if n <= 1 :
        return
    insertionRecursive(arr, n-1)
    last = arr[n-1]
    j = n-2

    while (j>=0 and arr[j]>last) :
        arr[j+1] = arr[j]
        j = j-1
    arr[j+1] = last

arr = [12, 11, 13, 5, 8]
insertionSort(arr)
print('Insertion sorting:', arr)

n = len(arr)
insertionRecursive(arr, n)
print('Insertion recursive sorting:', arr)
