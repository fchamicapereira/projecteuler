from functions import *

def leftToRight(x):
    s = str(x)
    s = s[1:]

    while len(s) > 0:
        if not prime(int(s)):
            return False
        s = s[1:]
    
    return True

def rightToLeft(x):
    s = str(x)
    s = s[::-1]
    s = s[1:]

    while len(s) > 0:
        if not prime(int(s[::-1])):
            return False
        s = s[1:]
    
    return True

limit = 11
counter = 0
n = 10
sum = 0

print leftToRight(11)

while counter < limit:
    if prime(n) and leftToRight(n) and rightToLeft(n):
        print 'Found: %d' % (n)
        counter += 1
        sum += n
    n += 1

print 'sum: ' + str(sum)
