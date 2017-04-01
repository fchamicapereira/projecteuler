from functions import *

limit = 10000

def listPrimeDivisors(limit):
    x = 2
    result = []
    while  x <= limit:
        result.append( list(set(primeDivisors(x) ) ) )
        x += 1
    return result

global pD
pD = listPrimeDivisors( limit )
print 'prime divisors list complete. len=',len(pD)

def isCoPrime(x,y):
    global pD
    return len( set( pD[x - 2]).intersection( pD[y - 2] ) ) == 0

def phi(n):
    p = pD[ n - 2 ]
    result = 1.0

    for i in p:
        result *= (1 - 1/float(i) )
    
    return int(n*result)

x = 2
result = [0,0]

while x <= limit:
    temp = float(x)/phi(x)
    
    if temp > result[1]:
        result[1] = temp
        result[0] = x
    x += 1

print result