from functions import *

def digitsInCommon(x,y):
    a = map(int,str(x))
    b = map(int,str(y))
    return list(set(a) & set(b))

def condition(a,b):
    na = map(int,str(a))
    nb = map(int,str(b))

    digits = digitsInCommon(a,b)

    if len(digits) == 0 or len(digits) == len(na) or len(digits) == len(nb):
        return False

    if na[ len(na)-1 ] == 0 and nb[ len(nb)-1 ] == 0:
        return False

    for d in digits:
        limitA = na.count(d)
        limitB = nb.count(d)

        if limitA < limitB:
            limit = limitA
        else:
            limit = limitB
        
        for i in range(0,limit):
            na.remove(d)
            nb.remove(d)

    na = map(str,na)
    nb = map(str,nb)

    aAfter = ''.join(na)
    aAfter = int(aAfter)

    bAfter = ''.join(nb)
    bAfter = int(bAfter)

    if aAfter == 0 or bAfter == 0:
        return False
    
    if float(a)/b == float(aAfter)/bAfter:
        print '%d/%d = %d/%d = %f' % (a,b,aAfter,bAfter,float(a)/b)
        return True
    return False

counter = 0
a = 1
b = 10
result = []

while counter < 4:
    for a in range(10,b):
        if condition(a,b):
            counter += 1
            result.append([a,b])
    b += 1

print "Solutions:"
print result

nomerator = 1
denominator = 1

for x in result:
    nomerator *= x[0]
    denominator *= x[1]

result = simplify(nomerator,denominator)
print '%d/%d = %d/%d' % (nomerator,denominator,result[0],result[1])