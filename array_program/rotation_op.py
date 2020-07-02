def leftRotate(arr, d, n) :
    for i in range(d) :
        leftRotatebyOne(arr, n)

def leftRotatebyOne(arr, n) :
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp

def rverseArray(arr, start, end) :
    while(start<end) :
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1

def leftRotate_Reverse(arr, d) :
    n = len(arr)
    rverseArray(arr, 0, d-1)
    rverseArray(arr, d, n-1)
    rverseArray(arr, 0, n-1)

def printArray(arr, size) :
    for i in range(size) :
        print('%d'%arr[i], end = ' ')
    print('')

arr = [1, 2, 3, 4, 5, 6, 7]
# left move one
leftRotate(arr, 3, 7)
printArray(arr, 7)
# reverse method
leftRotate_Reverse(arr, 3)
printArray(arr, 7)
