def cut(x,length):
    s = str(x)

    while len(s) > length:
        s = s[1:]

    s = ''.join(s)
    s = int(s)

    return s


result = 0
limit = 1000

for x in range(1,limit + 1):
    result += pow(x,x)

result = list(str(result))

start = len(result) - 1
end = start - 11
s = ''

for x in range(start,end,-1):
    s = result[x] + s

print s

result = 0
for x in range(1,limit + 1):
    result += pow(x,x)
    result = cut(result,10)

print result,len(str(result))