def Cloning(li1) :
    li_copy = [i for i in li1]
    return li_copy

li1 = [4,5,6,2,1]
li2 = Cloning(li1)

print('Original list:', li1)
print('After cloning:', li2)
