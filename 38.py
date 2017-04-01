from functions import *

def condition(x):
    s = str(x)
    digits = nDigits(x)
    counter = 2

    if repeatDigits(x):
        return -1

    while digits < 9:
        product = x*counter

        if repeatDigits(product):
            return -1

        sAdd = str(product)
        s += sAdd
        counter += 1
        digits += len(sAdd)

    if digits == 9 and pandigital(int(s),9):
        return int(s)
    
    return -1


limit = pow(10,4)
result = 0

for x in range(2,limit):
    temp = condition(x)
    if temp > result:
        print 'new record! %d made %d' % (x,temp)
        result = temp

print result