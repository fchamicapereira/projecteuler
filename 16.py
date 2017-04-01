def sumDigits(n):
    n = str(n)
    sum = 0

    for x in n:
        sum += int(x)
    
    return sum

n = pow(2,1000)

print sumDigits(n)