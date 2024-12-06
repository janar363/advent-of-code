def getGrid():
    with open("input") as file:
        grid = [[pos for pos in line.strip()] for line in file.readlines()]

    return grid

grid = getGrid()
def getPos(grid):
    pos = (-1, -1)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] in ['^', '>', '<', 'V']: 
                pos = (i, j)
                break

        if pos != (-1, -1): break
    return pos

originalPos = getPos(grid)
originalDir = grid[originalPos[0]][originalPos[1]]
pos = originalPos

gaurdInGrid = True
part1 = set()

while gaurdInGrid:

    part1.add(pos)
    if grid[pos[0]][pos[1]] == '^':
        if pos[0] != 0 and grid[pos[0]-1][pos[1]] == '.':
            grid[pos[0]-1][pos[1]] = grid[pos[0]][pos[1]]
            grid[pos[0]][pos[1]] = '.'
            pos = (pos[0]-1, pos[1])
        elif pos[0] == 0:
            gaurdInGrid = False
        elif grid[pos[0]-1][pos[1]] == '#':
            grid[pos[0]][pos[1]] = '>'
    elif grid[pos[0]][pos[1]] == '>':
        if pos[1] != len(grid[0])-1 and grid[pos[0]][pos[1]+1] == '.':
            grid[pos[0]][pos[1]+1] = grid[pos[0]][pos[1]]
            grid[pos[0]][pos[1]] = '.'
            pos = (pos[0], pos[1]+1)
        elif pos[1] == len(grid[0])-1:
            gaurdInGrid = False
        elif grid[pos[0]][pos[1]+1] == '#':
            grid[pos[0]][pos[1]] = 'V'
    elif grid[pos[0]][pos[1]] == 'V':
        if pos[0] != len(grid)-1 and grid[pos[0]+1][pos[1]] == '.':
            grid[pos[0]+1][pos[1]] = grid[pos[0]][pos[1]]
            grid[pos[0]][pos[1]] = '.'
            pos = (pos[0]+1, pos[1])
        elif pos[0] == len(grid)-1:
            gaurdInGrid = False
        elif grid[pos[0]+1][pos[1]] == '#':
            grid[pos[0]][pos[1]] = '<'
    elif grid[pos[0]][pos[1]] == '<':
        if pos[1] != 0 and grid[pos[0]][pos[1]-1] == '.':
            grid[pos[0]][pos[1]-1] = grid[pos[0]][pos[1]]
            grid[pos[0]][pos[1]] = '.'
            pos = (pos[0], pos[1]-1)
        elif pos[1] == 0:
            gaurdInGrid = False
        elif grid[pos[0]][pos[1]-1] == '#':
            grid[pos[0]][pos[1]] = '^'

        
print('part1 : ', len(part1))

part2 = 0
c = 0
loopC = 5


for blockPos in part1:
    
    if blockPos == originalPos: continue
    pos = originalPos
    grid = getGrid()
    grid[blockPos[0]][blockPos[1]] = 'O'

    gaurdInGrid = True
    visited = {}
    maxC = 0
    blockFound = False
    # print("for block position ", blockPos)
    while gaurdInGrid and maxC < loopC:
        if blockFound:
                if len(visited.keys()) == 0: visited[blockPos] = 1
                visited[pos] = 1 if pos not in list(visited.keys()) else visited[pos] + 1
                if visited[pos] > maxC: maxC = visited[pos]


        if grid[pos[0]][pos[1]] == '^':
            # print("entered ^ if for pos ", pos)
            if pos[0] != 0 and grid[pos[0]-1][pos[1]] == '.':
                grid[pos[0]-1][pos[1]] = grid[pos[0]][pos[1]]
                grid[pos[0]][pos[1]] = '.'
                pos = (pos[0]-1, pos[1])
            elif pos[0] == 0:
                gaurdInGrid = False
            elif grid[pos[0]-1][pos[1]] == '#':
                grid[pos[0]][pos[1]] = '>'
                # print("change direction to ", grid[pos[0]][pos[1]])
            elif grid[pos[0]-1][pos[1]] == 'O':
                blockFound = True
                grid[pos[0]][pos[1]] = '>'
                # print("change direction to ", grid[pos[0]][pos[1]])
        elif grid[pos[0]][pos[1]] == '>':
            # print("entered > if for pos ", pos)
            if pos[1] != len(grid[0])-1 and grid[pos[0]][pos[1]+1] == '.':
                grid[pos[0]][pos[1]+1] = grid[pos[0]][pos[1]]
                grid[pos[0]][pos[1]] = '.'
                pos = (pos[0], pos[1]+1)
            elif pos[1] == len(grid[0])-1:
                gaurdInGrid = False
            elif grid[pos[0]][pos[1]+1] == '#':
                grid[pos[0]][pos[1]] = 'V'
            elif grid[pos[0]][pos[1]+1] == 'O':
                blockFound = True
                grid[pos[0]][pos[1]] = 'V'
        elif grid[pos[0]][pos[1]] == 'V':
            # print("entered V if for pos ", pos)
            if pos[0] != len(grid)-1 and grid[pos[0]+1][pos[1]] == '.':
                grid[pos[0]+1][pos[1]] = grid[pos[0]][pos[1]]
                grid[pos[0]][pos[1]] = '.'
                pos = (pos[0]+1, pos[1])
            elif pos[0] == len(grid)-1:
                gaurdInGrid = False
            elif grid[pos[0]+1][pos[1]] == '#':
                grid[pos[0]][pos[1]] = '<'
            elif grid[pos[0]+1][pos[1]] == 'O':
                blockFound = True
                grid[pos[0]][pos[1]] = '<'
        elif grid[pos[0]][pos[1]] == '<':
            # print("entered < if for pos ", pos)
            if pos[1] != 0 and grid[pos[0]][pos[1]-1] == '.':
                grid[pos[0]][pos[1]-1] = grid[pos[0]][pos[1]]
                grid[pos[0]][pos[1]] = '.'
                pos = (pos[0], pos[1]-1)
            elif pos[1] == 0:
                gaurdInGrid = False
            elif grid[pos[0]][pos[1]-1] == '#':
                grid[pos[0]][pos[1]] = '^'
            elif grid[pos[0]][pos[1]-1] == 'O':
                blockFound = True
                grid[pos[0]][pos[1]] = '^'

        
    if maxC == loopC: 
        part2 += 1



print("part2 ", part2)
