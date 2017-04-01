import math
from functions import *
import time

def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6

    return True


def main():
    counter = 0
    nTriangle = 0
    d = 0
    limit = 500

    while d < limit:
        counter += 1
        nTriangle += counter
        d = divisors(nTriangle)

    print counter, nTriangle,d

startTime = time.time()
main()
print str(time.time() - startTime) + ' sec'