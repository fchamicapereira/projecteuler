def period(q):
    if q % 10 in [1,3,7,9]:
        n = 1
        while 1:
            if (pow(10,n)-1) % q == 0:
                return n
            n += 1
    else:
        return 0

limit = 1000

maj = 0
n = 0
for x in range(3,limit,2):
    if x % 10 in [1,3,7,9]:
        temp = period(x)
        if temp > maj:
            maj = temp
            n = x

print n,maj
