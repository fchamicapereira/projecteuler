from functions import prime

limit = 2000000
i = 2
sum = 0

while 1:
    if i > limit:
        break
    if prime(i):
        sum += i
    i += 1

print sum