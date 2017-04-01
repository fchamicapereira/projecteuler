f = open("p022_names.txt")

string = f.read().replace('"','')

names = string.split(',')

names.sort()

def valueLeter(c):
    return ord(c)-64

sum = 0
nNames = len(names)
for i in range(0,nNames):
    value = 0
    for c in names[i]:
        value += valueLeter(c)
    value = value * (i+1)
    sum += value

print sum
