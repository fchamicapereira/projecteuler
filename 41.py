from functions import *

record = 0


for n in range(1,9):
    x = pow(10,n)-1
    
    if n not in [1,4,7]:
        continue

    while x > 1:
        if pandigital(x,n) and prime(x):
            print 'found! %d pandigital: %d' % (n,x)
            if x > record:
                record = x
            break
        x -= 1

print record