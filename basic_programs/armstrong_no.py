def power(x, y) :
    # print(x,y)
    if y==0 :
        return 1
    if y%2==0 :
        return power(x, int(y/2))*power(x, int(y/2))
    return x*power(x, int(y/2))*power(x, int(y/2))

def order(x) :
    # variable to store of the number
    n = 0
    while (x!=0) :
        n = n+1
        x = int(x/10)
    return n

def isArmstrong(x) :
    n = order(x)
    temp = x
    sum1 = 0
    while (temp!=0) :
        # print(temp)
        r = temp%10
        # print(r)
        sum1 = sum1 + power(r, n)
        temp = int(temp/10)
    return (sum1 == x)

x = 1634
print(isArmstrong(x))
x = 1253
print(isArmstrong(x))
