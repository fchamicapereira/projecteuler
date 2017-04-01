def digits(n):
    return len(str(n))

d = 1000

first = 1
second = 1
place = 2
dCounter = 0

while dCounter < d:
    place += 1
    
    fib = first + second
    first = second
    second = fib

    dCounter = digits(fib)

print place
    
    
