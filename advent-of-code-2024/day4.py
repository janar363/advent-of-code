with open('input') as f:
    grid = [[ch for ch in line.strip()] for line in f.readlines()]

part1 = 0
res = ['XMAS', 'SAMX']
for i in range(0, len(grid)):
    for j in range(0, len(grid[0])):
        if grid[i][j] in ['X', 'S']:
            if j + 3 < len(grid[0]):
                h = grid[i][j] + grid[i][j+1] + grid[i][j+2] + grid[i][j+3] 
                if h in res: part1 += 1
            if i + 3 < len(grid):
                v = grid[i][j] + grid[i+1][j] + grid[i+2][j] + grid[i+3][j]
                if v in res: part1 += 1

            if i + 3 < len(grid) and j + 3 < len(grid[0]):
                d1 = grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] + grid[i+3][j+3] 
                if d1 in res: part1 += 1
            if i + 3 < len(grid) and j - 3 >= 0:
                d2 = grid[i][j] + grid[i+1][j-1] + grid[i+2][j-2] + grid[i+3][j-3] 
                if d2 in res: part1 += 1

print(part1)

part2 = 0
for i in range(1, len(grid)-1):
    for j in range(1, len(grid[0])-1):
        if grid[i][j] == 'A':
            if grid[i-1][j-1] == 'M' and grid[i-1][j+1] == 'M' and grid[i+1][j-1] == 'S' and grid[i+1][j+1] == 'S': part2 += 1
            elif grid[i-1][j-1] == 'S' and grid[i-1][j+1] == 'M' and grid[i+1][j-1] == 'S' and grid[i+1][j+1] == 'M': part2 += 1
            elif grid[i-1][j-1] == 'S' and grid[i-1][j+1] == 'S' and grid[i+1][j-1] == 'M' and grid[i+1][j+1] == 'M': part2 += 1
            elif grid[i-1][j-1] == 'M' and grid[i-1][j+1] == 'S' and grid[i+1][j-1] == 'M' and grid[i+1][j+1] == 'S': part2 += 1

print(part2)






        