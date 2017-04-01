def seq(n):
    counter = 1
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n + 1
        counter += 1
    return counter

limit = 1000000
size = 0
winner = 0

for x in range(1,limit):
    newSize = seq(x)
    if newSize > size:
        size = newSize
        winner = x

print winner,size