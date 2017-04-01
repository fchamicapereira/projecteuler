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

def evaluate(n):
    s = sumProperDivisors(n)
    if n == s:
        return 'perfect'
    if s < n:
        return 'deficient'
    return 'abundant'

limit = 28123
abundant = []
numbers = []

for n in range(0,limit+1):
    numbers.append(0)

for x in range(2,limit+1):
    if evaluate(x) == 'abundant':
        abundant.append(x)

size = len(abundant)

for x in range(0,size):
    for y in range(x,size):
        a = abundant[x]
        b = abundant[y]
        if a+b-1 < limit+1:
            numbers[a+b-1] = 1

sum = 0
for i in range(0,len(numbers)):
    if numbers[i] == 0:
        sum += i+1

print sum
