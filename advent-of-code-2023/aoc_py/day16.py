import sys
from copy import deepcopy
from collections import deque

up, right, down, left = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def invalidPos(pos):
    if pos[0] < 0 or pos[0] >= len(contraption): return True
    if pos[1] < 0 or pos[1] >= len(contraption[0]): return True


    return False

for arg in sys.argv[1:]:
    print('\n', arg)
    
    with open(arg) as f:
        contraption = [[ch for ch in line.strip()] for line in f.readlines()]

    def start(pos, dir):    
        seen = set()
        queue = deque()

        queue.append((pos, dir))

        while not len(queue) == 0:
            
            pos = queue[0][0]
            dir = queue[0][1]

            if invalidPos(pos) or (pos, dir) in seen:
                queue.popleft()
                continue

            seen.add((pos, dir))
            queue.popleft()

            tile = contraption[pos[0]][pos[1]]

            if tile == '.' or (tile == '|' and dir in [up, down]) or (tile == '-' and dir in [left, right]):
                queue.append(((pos[0]+dir[0], pos[1]+dir[1]), dir))
            elif tile == '|':
                queue.append(((pos[0]+up[0], pos[1]+up[1]), up))
                queue.append(((pos[0]+down[0], pos[1]+down[1]), down))
            elif tile == '-':
                queue.append(((pos[0]+left[0], pos[1]+left[1]), left))
                queue.append(((pos[0]+right[0], pos[1]+right[1]), right))
            elif tile == '/':
                queue.append(((pos[0]-dir[1], pos[1]-dir[0]), (-dir[1], -dir[0])))
            elif tile == '\\':
                queue.append(((pos[0]+dir[1], pos[1]+dir[0]), (dir[1], dir[0])))
        
        activated_pos = {pos for pos, _ in seen}

        return len(activated_pos)
    
    print("part 1: ", start((0, 0), right))

    max_count = 0
    max_pos = (0, 0)
    for j in range(len(contraption[0])):
        cur_count = start((0, j), down)
        if cur_count > max_count:
            max_count = cur_count
            max_pos = (0, j)

    for j in range(len(contraption)):
        cur_count = start((j, len(contraption[0])-1), left)
        if cur_count > max_count:
            max_count = max_count
            max_pos = (j, len(contraption[0])-1)

    for j in range(len(contraption[0])):
        cur_count = start((len(contraption)-1, j), down)
        if cur_count > max_count:
            max_count = max_count
            max_pos = (len(contraption)-1, j)


    for j in range(len(contraption)):
        cur_count = start((j, 0), left)
        if cur_count > max_count:
            max_count = max_count
            max_pos = (j, 0)
            
    print("max count = ", max_count)
    print("max pos = ", max_pos)