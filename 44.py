from functions import *

def pentagonal(n): return n*(3*n-1)/2

def  checkIfPentagonal(x):
    xDigits = nDigits(x)

    if xDigits % 2 == 0:
        nDigitsLimit = xDigits/2 
    else:
        nDigitsLimit = (xDigits+1)/2

    
    if nDigitsLimit > 1:
        start = pow(10,nDigitsLimit-2)*8
    else:
        start = pow(10,nDigitsLimit-1)

    end = pow(10,nDigitsLimit)

    for n in range(start,end):
        if pentagonal(n) == x:
            return n
    
    return -1

def condition(a,b):
    dif = a - b

    if checkIfPentagonal( dif ) == -1:
        return -1

    print '(%d,%d) The dif is pentagonal!' % (a,b)

    if checkIfPentagonal(a + b) == -1:
        return -1

    return dif


def genPentagonal(digits):
    result = []
    counter = 1
    p = 0

    while nDigits(p) <= digits:
        p = pentagonal(counter)
        result.append( p )
        counter += 1

    return result
    


power = 4

pen = genPentagonal(power*2 + 1)

size = len(pen)

process = 0

start = 1
limit = pow(10,power+1)

winner = limit

for x in pen:
    index = pen.index(x)

    process = printState(process,index,size)

    for y in pen[:index]:
        D = x - y
        if (x + y) in pen and D in pen:
            print '(%d,%d) \t D = %d' % (x,y,x-y)
            
            if winner > D:
                winner = D
                break
        if winner != limit:
            break

if winner == limit:
    print 'Not found :('
else:
    print 'record: %d' % winner