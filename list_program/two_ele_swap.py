def swapPositions(list, pos1, pos2) :
    get = list[pos1], list[pos2]
    list[pos2], list[pos1] = get

    return list

List = [23, 56, 89, 57]
print(List)
pos1, pos2 = 1, 3
print(swapPositions(List, pos1-1, pos2-1))
