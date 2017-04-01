from functions import *

def irrational(limit):
    n = ''
    digits = 0
    steps = 1
    counter = 1

    while digits <= limit:
        n += str(counter)
        counter +=1
        digits += steps

        if nDigits(counter) > steps:
            steps = nDigits(counter)
        
    n = map(int,n)
    return n

limitPower = 6
end = pow(10,limitPower)

n = irrational(end)
print len(n)

p = 2
product = 1
while p <= limitPower:
    print p
    product *= n[ pow(10,p)-1 ]
    p += 1

print product