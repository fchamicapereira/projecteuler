from functions import *

def sumDigits(n,sum):
    s = str(n)

    if len(s) == 1:
        return sum + int(s[0])

    return sumDigits( int(s[1:]), sum + int(s[0]) )

max = 0
for a in range(2,100):
    for b in range(1,100):
        p = pow(a,b)
        sumD = sumDigits(p,0)
        if sumD > max:
            max = sumD

print max