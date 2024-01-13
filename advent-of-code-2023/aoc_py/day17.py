import sys
from copy import deepcopy
from collections import deque
from heapq import heappush, heappop

up, right, down, left = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def validPos(pos):
    if pos[0] < 0 or pos[0] >= len(heat_map): return False
    if pos[1] < 0 or pos[1] >= len(heat_map[0]): return False

    return True

for arg in sys.argv[1:]:
    print('\n', arg)
    
    with open(arg) as f:
        heat_map = [list(map(int, line.strip())) for line in f.readlines()]

    # part 1
    def get_min_heat(max_steps, min_steps):
        pq = [(0, (0, 0), right, 0)]
        heappush(pq, (0, (0, 0), down, 0))

        end = (len(heat_map)-1, len(heat_map[0])-1)
        ans = 0
        seen = set()

        while pq:
            hl, pos, dir, steps = heappop(pq)

            if pos == end:
                ans = hl
                break

            if (pos, dir, steps) in seen:
                continue
            else:
                seen.add((pos, dir, steps))

            if steps != max_steps:
                npos = (pos[0]+dir[0], pos[1]+dir[1])
                if validPos(npos):
                    heappush(pq, (hl+heat_map[npos[0]][npos[1]], npos, dir, steps + 1))

            if steps >= min_steps:
                for ndir in [left, right] if dir in [up, down] else [up, down]:
                    npos = (pos[0]+ndir[0], pos[1]+ndir[1])
                    if validPos(npos):
                        heappush(pq, (hl+heat_map[npos[0]][npos[1]], npos, ndir, 1))

        return ans
    
    print("part 1: ", get_min_heat(3, 0))
    print("part 2: ", get_min_heat(10, 4))

    