# find factorial of given number
# recursive based approach
def factorial_recur(n) :

    # single line to find factorial
    return 1 if (n==1 or n==0) else n*factorial_recur(n-1)

def factorial_iter(n) :
    if n < 0 :
        return 0
    elif n==0 or n==1 :
        return 1
    else:
        fact = 1
        while(n>1) :
            fact *= n
            n -= 1
        return fact

def factorial_to(n) :
    return 1 if (n==1 or n==0) else n * factorial_to(n-1)


# Driver code
num = 20
print('Recursive: Factorial of', num, 'is', factorial_recur(num))
print('Iterative: Factorial of', num, 'is', factorial_iter(num))
print('Ternary operator: Factorial of', num, 'is', factorial_to(num))
