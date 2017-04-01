from functions import *

limit = 1000000

sum = 0
for x in range(limit):
    if palyndrome(x) and palyndrome( changeBase(x,2) ):
        print 'base 10: %d \nbase 2:  %d \n' % ( x, changeBase(x,2) )
        sum += x

print 'sum: ' + str(sum)