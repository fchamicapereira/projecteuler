from functions import *

def primeGenerator(limit):
    n = 2
    primes = []

    while n <= limit:
        if prime(n):
            primes.append(n)
        n += 1

    return primes

n = 5
primes = primeGenerator(10000)
max = primes[ len(primes) - 1 ]
found = False

while found == False:
    if n > max:
        print ' nao deu :('
        break
    
    while n in primes:
        n += 2
    
    for p in primes:
        state = True

        if p >= n:
            print 'found! %d' % n
            found = True
            break
        
        for square in range(1,n):
            result = p + 2*(square**2)
            
            if result > n:
                break
            
            if result == n:
                state = False
                break

        if state == False:
            break

    n += 2
