def isPrime2(num) :
    if num <2 :
        return 0
    for i in range(2,num) :
        if(num%i) ==0 :
            return 0
    return 1

min = 1
max = 100
for i in range(min,max+1) :
    if isPrime2(i):
        print('Between',min,' and ',max, ':', i,'is a prime number!')
