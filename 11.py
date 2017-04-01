lines = [line.rstrip('\n') for line in open('11.dat')]

grid = []

for x in lines:
    result = x.split(' ')
    result = map(int,result)
    grid.append(result)


product = 1
temp = 1
size = len(grid[0])
obj = 4

for y in range(0,size):
    for x in range(0,size):
        if x + obj-1 < size: #right
            if y - (obj-1) >= 0: #diagonal up right
                for i in range(0,obj):
                    temp *= grid[y-i][x+i]
                if temp > product:
                    product = temp
                temp = 1

            if y + obj-1 < size: #diagonal down right
                for i in range(0,obj):
                    temp *= grid[y+i][x+i]
                if temp > product:
                    product = temp
                temp = 1
            
            #right
            for i in range(0,obj):
                temp *= grid[y][x+i]
            if temp > product:
                product = temp
            temp = 1

        #down
        if y + obj-1 < size:
            for i in range(0,obj):
                temp *= grid[y+i][x]
            if temp > product:
                product = temp
            temp = 1

print product