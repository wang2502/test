def RemoveNthword(lst, word, N) :
    newList = []
    count = 0

    print('Old list is', lst)
    print('Word =', word)
    print('N =', N)
    # iterate the elements
    for i in lst :
        if (i != word) :
            newList.append(i)
            continue
        count += 1
        if(count != N) :
            newList.append(i)

    if count == 0 or count < N :
        # print(count)
        print('Item not found')
        return newList
    print('Updated list is', newList)
    # print(count)
    return newList

list = ['greeks','for','greeks']
word = 'greeks'
N = 1

RemoveNthword(list, word, N)
