def printGrid(g):
    size = len(g)

    for x in range(0,size):
        line = ''
        for y in range(0,size):
            line += str(g[x][y]) + '\t'
        print line


def sumDiagonal(g):
    size = len(g)
    sum = -1
    start = size/2
    
    x = 0
    y = 0

    while x < size:
        sum += g[x][y]
        x += 1
        y += 1
    
    x = size - 1
    y = 0

    while y < size:
        sum += g[x][y]
        x -= 1
        y += 1

    return sum

size = 1001

grid = []
for x in range(0,size):
    temp = []
    for y in range(0,size):
        temp.append(0)
    grid.append(temp)

start = size/2
grid[start][start] = 1


go = True
steps = 1
times = 2
direction = 0
counter = 0
x = start
y = start
number = 1

while go:
    if steps == size - 1:
        times = 3
        go = False
    
    for i in range(0,times):
        if counter == 0:
            for i in range(0,steps):
                number += 1
                y += 1
                grid[x][y] = number

        if counter == 1:
            for i in range(0,steps):
                number += 1
                x -= 1
                grid[x][y] = number
        
        if counter == 2:
            for i in range(0,steps):
                number += 1
                y -= 1
                grid[x][y] = number

        if counter == 3:
            for i in range(0,steps):
                number += 1
                x += 1
                grid[x][y] = number

        counter = (counter + 1) % 4

    steps += 1

print sumDiagonal(grid)