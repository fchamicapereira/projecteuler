from functions import *

def checkProperty(numbers):
    size = len(numbers)
    numbers = map(str,numbers)
    for x in range(0,size-1):
        for y in range(x+1,size):
            s1 = int(float(numbers[x] + numbers[y]))

            if prime(s1) == False:
                return False

            s2 = int(float(numbers[y] + numbers[x]))

            if prime(s2) == False:
                return False

    return True
            

def f():
    limit = 10000
    primes = generatePrimes( limit )
    
    size = len( primes )
    print "Size:",size

    for a in range(1,size-4):
        for b in range(a+1,size-3):
            if checkProperty( [primes[a],primes[b]] ) == False:
                continue

            for c in range(b+1,size-2):
                if checkProperty( [primes[a],primes[c]] ) == False:
                    continue
                if checkProperty( [primes[b],primes[c]] ) == False:
                    continue

                for d in range(c+1,size-1):
                    if checkProperty( [primes[a],primes[d]] ) == False:
                        continue
                    
                    if checkProperty( [primes[b],primes[d]] ) == False:
                        continue

                    if checkProperty( [primes[c],primes[d]] ) == False:
                        continue

                    for e in range(d+1,size):
                        if checkProperty( [primes[a],primes[e]] ) == False:
                            continue
                    
                        if checkProperty( [primes[b],primes[e]] ) == False:
                            continue

                        if checkProperty( [primes[c],primes[e]] ) == False:
                            continue

                        if checkProperty( [primes[d],primes[e]] ) == False:
                            continue

                        print [primes[a],primes[b],primes[c],primes[d],primes[e]]
                        print primes[a] + primes[b] + primes[c] + primes[d] + primes[e]
                        return

functionDuration( f )