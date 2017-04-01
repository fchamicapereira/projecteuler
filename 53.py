from functions import *

f = []
for x in range(0,1005):
    f.append( factorial(x) )

def combinations(f,n,p):
    return f[n] / ( f[p] * f[ n - p] )

counter = 0

for n in range(1,101):
    for p in range(1,x):
        r = combinations(f,n,p)
        if r > 1000000:
            counter += 1
            print n,p,r

print counter