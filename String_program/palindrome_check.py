def isPalindrome(s) :
    return s == s[::-1]

def isPalindrome2(s) :
    rev = ''.join(reversed(s))
    return (s == rev)


s = 'malayalam'
if isPalindrome2(s) :
    print('Yes')
else:
    print('No')
