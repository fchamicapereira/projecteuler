from functions import prime

place = 10001

counter = 0
n = 1

while counter != place:
    n += 1
    if prime(n):
        counter += 1

print n