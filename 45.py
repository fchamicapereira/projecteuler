from functions import *

p = []
h = []
t = []

for x in range(1,1000000):
    p.append( pentagonal(x) )
    h.append( x*(2*x - 1) )
    t.append( triangle(x) )

int1 = list(set(p).intersection(h))
print int1
