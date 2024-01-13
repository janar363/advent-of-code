import sys
from copy import deepcopy
from collections import deque
from heapq import heappush, heappop
import math

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def validPos(pos):
    global grid

    if pos[0] < 0 or pos[0] >= len(grid): return False
    if pos[1] < 0 or pos[1] >= len(grid[0]): return False
    if grid[pos[0]][pos[1]] == '#': return False

    return True

def validPos2(pos):
    global grid

    if grid[pos[0] % len(grid)][pos[1] % len(grid[0])] == '#': return False

    return True
            
for arg in sys.argv[1:]:
    print('\n', arg)
    
    with open(arg) as f:
        grid = [[pos for pos in line.strip()] for line in f.readlines()]

    start = []
    for rid, r in enumerate(grid):
        if 'S' in r:
            start = (rid, r.index('S'))

    def get_possible_positions(total_steps):
        seen = set()

        q = deque([(start)])
        step_counts = [len(q)]
        seen.add(start)

        for i in range(total_steps):
            posLen = len(q)

            for _ in range(posLen):
                pos = q.popleft()

                for dir in dirs:
                    npos = (pos[0]+dir[0], pos[1]+dir[1])

                    if validPos(npos) and npos not in seen:
                        q.append(npos)
                        seen.add(npos)

            step_counts.append(len(q))

        total = 0

        print(step_counts)
        for i in range(0 if total_steps % 2 == 0 else 1, total_steps+1, 2):
            total += step_counts[i]

        return total

    print("part 1: ", get_possible_positions(64))

    def get_possible_positions2(total_steps):
        seen = set()

        q = deque([(start)])
        step_counts = [len(q)]
        seen.add(start)

        for i in range(total_steps):
            posLen = len(q)

            for _ in range(posLen):
                pos = q.popleft()

                for dir in dirs:
                    npos = (pos[0]+dir[0], pos[1]+dir[1])

                    if validPos2(npos) and npos not in seen:
                        q.append(npos)
                        seen.add(npos)

            step_counts.append(len(q))

        total = 0
        print(step_counts)
        for i in range(0 if total_steps % 2 == 0 else 1, total_steps+1, 2):
            total += step_counts[i]

        return total
    
    for i in [1000, 26501365][:1]:
        print('part 2: ', get_possible_positions2(i))
            