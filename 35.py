from functions import *

def circularPrime(n):
    s = map(str,str(n))
    size = len(s)
    comb = [n]

    for x in range(0,size-1):
        temp = list(s)

        for i in range(0,size):
            temp[i] = s[ (x+i+1) % size ]

        comb.append( int( ''.join(temp) ) )
    
    for x in comb:
        if prime(x) != True:
            return False
    
    return True

limit = 1000000
counter = 0

for x in range(2,limit):
    if circularPrime(x):
        print x
        counter += 1

print "Counter = " + str(counter)