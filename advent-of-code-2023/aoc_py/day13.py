import sys
from copy import deepcopy

def get_diff(top, bottom):
    diff = 0
    for id, _ in enumerate(top):
        if top[id] == bottom[id]: continue

        for j, _ in enumerate(top[id]):
            if top[id][j] != bottom[id][j]:
                diff += 1
    
    return diff

def get_count2(grid):
    h = 0

    for r in range(1, len(grid)):
        top = grid[:r][::-1]

        bottom = grid[r:]

        if get_diff(top[:len(bottom)], bottom[:len(top)]) == 1:
            h = len(top)
            break

    return h

def get_count(grid):
    h = 0

    for r in range(1, len(grid)):
        top = grid[:r][::-1]

        bottom = grid[r:]

        if top[:len(bottom)] == bottom[:len(top)]:
            h = len(top)
            break

    return h

for arg in sys.argv[1:]:
    print('\n', arg)
    with open(arg) as f:
        grids = [[r.strip() for r in grid.split('\n')] for grid in f.read().split('\n\n')]


    tv = th = 0
    for grid in grids:
        th += get_count(grid)

        tv += get_count(list(zip(*grid)))

    print("part 1: ", tv + 100 * th)

    tv = th = 0
    for grid in grids:
        th += get_count2(grid)

        tv += get_count2(list(zip(*grid)))

    print("part 2: ", tv + 100 * th)


    