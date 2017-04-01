from functions import *

global maxIt

maxIt = 50
maxN = 10000

def isLychrel(n,i):
    if i == maxIt:
        return True

    if palyndrome(n) and i != 0:
        return False
    
    newN = n + reverseNumber(n)

    return isLychrel( newN, i+1 )

counter = 0
for x in range(10,maxN):
    if isLychrel(x,0):
        counter += 1
print counter