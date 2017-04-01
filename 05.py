end = 20

i = end
go = True

if i % 2 != 0:
    i+=1

while go:
    i+=2
    go = False

    for x in range(3,end):
        if i % x != 0:
            go = True
            break
print i