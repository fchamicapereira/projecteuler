from functions import prime
import math

n = 600851475143

limit = int(math.sqrt(n))

for x in range(1,limit):
    if prime(x) and (n % x == 0):
       print x