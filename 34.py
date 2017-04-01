from functions import *

def guilty(fac, number):
    n = listOfDigits(number)
    size = len(n)
    condition = False

    for i in range(0,size):
        if condition:
            n[i] = 0

        elif fac[n[i]] > number:
            if i-1 >= 0:
                n[i-1] += 1
                n[i] = 0

            else:
                for x in range(0,size):
                    n[x] = 0
                n = [1] + n
                r = map(str,n)
                r = ''.join(r)
                r = int(r)
                return r

            condition = True

    r = map(str,n)
    r = ''.join(r)
    r = int(r)

    if r == number:
        n[ size-1 ] = 0
        n[ size-2 ] += 1

        r = map(str,n)
        r = ''.join(r)
        r = int(r)

        return r

    return r

fac = []

for x in range(0,10):
    fac.append( factorial(x) )

digits = 2
n = '99'

while 1:
    if digits*fac[9] < int(n):
        end = digits*fac[9]
        break
    digits += 1
    n += '9'

result = 0
x = 10

while x < end:
    digits = listOfDigits(x)

    sum = 0

    for d in digits:
        sum += fac[d]

    if x == sum:
        result += x
        print x
        x += 1

    elif sum > x:
        x = guilty(fac,x)

    x += 1

print "sum = " + str(result)