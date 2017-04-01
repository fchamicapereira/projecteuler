def isPrime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5

    while i*i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True

def primes(a,b):
    n = 0

    while isPrime(n*n+a*n+b):
        n += 1

    return n

limit = 1000

nPrimes = 0
aW = 0
bW = 0

for a in range(-limit,limit):
    for b in range(-limit,limit):
        temp = primes(a,b)
        if temp > nPrimes:
            nPrimes = temp
            aW = a
            bW = b

print aW,bW,aW*bW
