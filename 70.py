from functions import *
import bisect

limit = pow(10,5)

def primes1(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

global primes
global phiList
#primes = generatePrimes(limit*2)
primes = primes1( limit*2 )
phiList = [0]*limit

def pD( n ):
    global primes
    l = []
    start = n

    if n <= 1:
        return []
    
    if n not in primes:
        start = int(math.sqrt(n))
    else:
        return [n]
    
    size = len(primes)
    i = bisect.bisect(l, start) + 1

    while i >= 0:
        p = primes[i]

        if n % p == 0:
            l.append(p)
            break

        i -= 1

    l.extend(pD(n/p))
    return l

print 'Primes done'

def isPermut(x,y):
    x = list(str(x))
    y = list(str(y))

    if len(x) != len(y):
        return False

    x.sort()
    y.sort()

    return x == y

def phi_fast(n):
    p = set(pD(n))
    result = 1.0

    for i in p:
        result *= (1 - 1/float(i) )
    
    return int(n*result)

def phi_slow(n):
    coPrimes = [1]

    def isCoPrime(x,y):
        pdX = pD(x)
        pdY = pD(y)
        print x,pdX,y,pdY
        return len( set( pdX ).intersection( pdY ) ) == 0
    
    for x in range(2,n):
        if isCoPrime(n,x):
            coPrimes.append(x)
        print n,x

    return coPrimes

#print phi_slow(10)

def main():
    x = 2
    result = [0,0,limit]

    while x < limit:
        p = phi_fast(x)

        if isPermut(x,p) and float(x)/p < result[2]:
        	result = [x,p,float(x)/p]
        
        x += 1

    print result

main()