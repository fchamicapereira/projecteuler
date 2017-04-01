from functions import *
import signal
import bisect

global dt
global d

dt = 15

def handler(signum, frame):
    global d
    global dt

    print 'Signal handler called with signal', signum
    print 'd =',d,"(",100.0*d/1000000,"% )"
    signal.alarm(dt)


global primes
primes = generatePrimes( 1000000 )
print "done calculating primes"


def primeDivisors2(n):
    global primes
    list = []
    start = n

    if n <= 1:
        return []
    
    if n not in primes:
        start = int(math.sqrt(n))
    else:
        return [n]
    
    i = bisect.bisect_left(primes, start)

    while i >= 0:
        p = primes[i]
        if n % p == 0:
            list.append(p)
            break
        i -= 1
    
    list.extend(primeDivisors(n/p))
    return list

def simplify3(a,b):

    aDivisors = primeDivisors2(a)
    bDivisors = primeDivisors2(b)

    inCommon = list(set(aDivisors) & set(bDivisors))

    for d in inCommon:
        ca = aDivisors.count(d)
        cb = bDivisors.count(d)

        if ca < cb: c = ca
        else: c = cb

        for i in range(0,c):
            a /= d  
            b /= d

    
    return [a,b]

def main():
    fractions = set()
    global d

    signal.signal(signal.SIGALRM, handler)
    signal.alarm(dt)

    d = 2
    
    while d <= 1000000:
        n = 1
        while n < d:
            #f = simplify3(n,d)
            f = float(n)/d
            #if f not in fractions:
            fractions.update([f])

            n += 1
        d += 1
    
    print len(fractions)

main()