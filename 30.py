digits = 5


def sumPowers(x):
    s = list(str(x))
    n = map(int, s)
    sum = 0
    for d in n:
        sum += pow(d,5)
    
    if sum == x:
        return True
    return False


limit = pow(10,digits+1)

sum = 0

for x in range(2,limit):
    if sumPowers(x):
        sum += x

print sum