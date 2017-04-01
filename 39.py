from functions import *
import math

def is_square(apositiveint):
    x = apositiveint // 2
    seen = set([x])
    while x * x != apositiveint:
        x = (x + (apositiveint // x)) // 2
        if x in seen: return False
        seen.add(x)
    return True

def solutions(p):
    s = []
    exceptions = []

    for h in range(2,p):
        for a in range(2,h):
            if a+h > p or a in exceptions:
                break

            hS = h*h
            aS = a*a
            bS = hS-aS

            if not is_square(bS):
                continue

            b = int(math.sqrt(bS))
            
            if h+a+b == p:
                exceptions.append(b)
                s.append([a,b,h])
    return s

limit = 1001
record = 0
solution = 0

for p in range(2,limit):
    nSol = len(solutions(p))
    if nSol > record:
        print 'record with %d: %d solutions' % (p,nSol)
        record = nSol
        solution = p

print solution