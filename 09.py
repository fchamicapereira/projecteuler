import math

def checkPythTriple(a,b,c):
    if a*a + b*b == c*c:
        return True
    return False

def condition(a,b,c):
    if checkPythTriple(a,b,c) and a+b+c == 1000:
        return True
    return False

c = 2

go = 1

while go:
    c += 1

    for b in range(1,c - 1):
        for a in range(1,b - 1):
            if checkPythTriple(a,b,c):
                print str(a) + '^2 + ' + str(b) + '^2 = ' + str(c) + '^2'
            if condition(a,b,c):
                print str(a) + '*' + str(b) + '*' + str(c) + ' = ' + str(a*b*c)
                go = 0
                break
        if go == 0:
            break