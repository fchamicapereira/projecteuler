from functions import *

def t(n): return int(0.5*n*(n+1))

def isTriangle(x):
    x = 2*x
    digits = nDigits(x)

    if digits % 2 == 0:
        end = pow(10, (digits / 2))
    else:
        end = pow(10,( digits + 1 ) /2)

    n = 1

    while n < end:
        if n*(n+1) == x:
            return n
        n += 1

    return -1

def wordValue(word):
    sum = 0
    base = ord('A')

    for letter in word:
        sum += ord(letter) - base + 1

    return sum

words = []

with open('p042_words.txt','r') as f:
    for line in f:
        for word in line.split(','):
           words.append(word[1:-1])

sum = 0
for word in words:
    value = wordValue(word)
    n = isTriangle(value)

    if n != -1:
        sum += 1
        print word,value,n

print sum