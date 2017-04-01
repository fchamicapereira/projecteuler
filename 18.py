grid = []
file = open('p067_triangle.txt')

for row in file:
    row = row.replace("\n", "")
    line = row.split(' ')
    line = map(int,line)
    grid.append(line)

#grid = []
#grid = [[3],[7,4],[2,4,6],[8,5,9,3]]

def maj(v,l,c,s):
    lines = len(s)

    if l+1 < lines:
        first = v[l][c] + s[l+1][c]
        second = v[l][c+1] + s[l+1][c+1]
    else:
        first = v[l][c]
        second = v[l][c+1]

    if first > second:
        return first
    return second

lines = len(grid)
solve = []

for x in range(0,lines):
    solve.append([])

for x in range(lines - 1,-1,-1):
    for y in range(0,len(grid[x])-1):
        winner = maj(grid,x,y,solve)

        solve[x].append(winner )

solve[0].append( solve[1][0] + grid[0][0] )

print grid
print solve
print solve[0][0]