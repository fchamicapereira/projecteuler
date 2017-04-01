from functions import palyndrome
import math

power = 2

start = 10**(power+1) - 1
end = 10**power
result = 0
resultX = 0
resultY = 0

for x in range(start,end,-1):
    for y in range(start,end,-1):
        product = x*y
        if palyndrome(product) and product > result:
            result = product
            resultX = x
            resultY = y
print str(result) + " = " + str(resultX) + " * " + str(resultY)