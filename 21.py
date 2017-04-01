def sumProperDivisors(n):
    i = 2
    sum = 1

    while i*i < n:
        if n % i == 0:
            sum += i + n/i
        i += 1
        
    if i*i == n:
        sum += i

    return sum

def amicable(a):
    b = sumProperDivisors(a)
    c = sumProperDivisors(b)

    if a == b:
        return False
    if a != c:
        return False
    
    return True

limit = 10000
sum = 0

for x in range(1,limit):
    if amicable(x):
        sum += x

print sum
