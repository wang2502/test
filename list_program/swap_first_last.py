def swapList(list) :

    first = list.pop(0)
    last = list.pop(-1)

    list.insert(0,last)
    list.append(first)

    return list

newList = [12, '3', 45, 23, 43]
print(newList)
print(swapList(newList))
