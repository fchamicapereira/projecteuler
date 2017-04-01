def fact(x):
    if x == 1:
        return 1
    return x*fact(x-1)

def sumOfDigits(x):
    string = str(x)
    sum = 0

    for c in string:
        sum += int(c)
    
    return sum

print sumOfDigits(fact(100))