def binary_search(arr, low, high, x) :
    if high >= low :
        mid = (high + low) // 2

        if arr[mid] == x :
            return mid
        if arr[mid] > x :
            return binary_search(arr, low, mid-1, x)
        else:
            return binary_search(arr, mid+1, high, x)
    else:
        return -1

def lin_search(arr, x) :
    for i in range(len(arr)) :
        if arr[i] == x :
            return i
    return -1

arr = [2, 3, 4, 10, 40]
x = 10

result = binary_search(arr, 0, len(arr)-1, x)

if result != -1 :
    print('Binary search: Element is present at index', str(result))
else :
    print('Element is not present in array')

result = lin_search(arr, x)

if result != -1 :
    print('Linear search: Element is present at index', result)
else :
    print('Element is not present in array')
