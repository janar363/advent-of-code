from collections import deque
with open('input') as file:
    grid = [[int(ch) for ch in row.strip()] for row in file.readlines()]

headPositions = [(i, j )for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 0]

def getScore(pos):
    score = 0
    
    next = deque([pos])
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = {}
    while len(next) != 0:
        
        pos = next.popleft()
        if pos in list(visited.keys()): continue
        visited[pos] = True
        if grid[pos[0]][pos[1]] == 9: score += 1
        for dir in dirs:
            if 0 <= pos[0] + dir[0] < len(grid) and 0 <= pos[1] + dir[1] < len(grid[0]) and grid[pos[0] + dir[0]][pos[1] + dir[1]] == grid[pos[0]][pos[1]] + 1:
                next.append((pos[0] + dir[0], pos[1] + dir[1]))

    return score

def getScore2(pos):
    score = 0
    
    next = deque([pos])
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = {}
    while len(next) != 0:
        
        pos = next.popleft()

        visited[pos] = True
        if grid[pos[0]][pos[1]] == 9: score += 1
        for dir in dirs:
            if 0 <= pos[0] + dir[0] < len(grid) and 0 <= pos[1] + dir[1] < len(grid[0]) and grid[pos[0] + dir[0]][pos[1] + dir[1]] == grid[pos[0]][pos[1]] + 1:
                next.append((pos[0] + dir[0], pos[1] + dir[1]))

    return score

part1 = 0
part2 = 0
for headPosition in headPositions:
    part1 += getScore(headPosition)
    part2 += getScore2(headPosition)

print("part 1 : ", part1)
print("part 2 : ", part2)

