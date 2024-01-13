import sys
from collections import deque

for arg in sys.argv[1:]:
    print('\n', arg)
    with open(arg) as f:
        grid = [list(line.strip()) for line in f.readlines()]

    north, east, south, west = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    map = {
        '|' : [north, south],
        '-' : [east, west],
        'F' : [east, south],
        '7' : [south, west],
        'L' : [north, east],
        'J' : [north, west],
        'S' : [north, east, west, south],
        '.' : []
    }

    def has_north(pos):
        if north not in map[grid[pos[0]][pos[1]]]: return False

        val = grid[pos[0]+north[0]][pos[1]+north[1]]
        if south in map[val]: return True
        return False
    
    def has_south(pos):
        if south not in map[grid[pos[0]][pos[1]]]: return False

        val = grid[pos[0]+south[0]][pos[1]+south[1]]
        if north in map[val]: return True
        return False

    def has_east(pos):
        if east not in map[grid[pos[0]][pos[1]]]: return False

        val = grid[pos[0]+east[0]][pos[1]+east[1]]
        if west in map[val]: return True
        return False

    def has_west(pos):
        if west not in map[grid[pos[0]][pos[1]]]: return False

        val = grid[pos[0]+west[0]][pos[1]+west[1]]
        if east in map[val]: return True
        return False

    def set_start():
        start_pipe = '7'

        if has_north(start) and has_south(start):
            start_pipe = '|'
            print('has north and south')
        elif has_north(start) and has_east(start):
            start_pipe = 'L'
        elif has_north(start) and has_west(start):
            start_pipe = 'J'
        elif has_east(start) and has_west(start):
            start_pipe = '-'
        elif has_east(start) and has_south(start):
            start_pipe = 'F'
        
        grid[start[0]][start[1]] = start_pipe

    def get_dirs(node):
        ndirs = []

        if has_north(node): ndirs.append(north)
        if has_east(node): ndirs.append(east)
        if has_south(node): ndirs.append(south)
        if has_west(node): ndirs.append(west)

        return ndirs

    visited = set([])
    def get_max_node():
        queue = deque()

        queue.append((start, 0))
        max_node = 0
        while len(queue) != 0:
            node = queue.popleft()
            ndirs = get_dirs(node[0])
            visited.add(node[0])

            for ndir in ndirs:
                nextNode = (node[0][0]+ndir[0], node[0][1]+ndir[1])

                if nextNode not in visited:
                    queue.append((nextNode, node[1]+1))
            
            if node[1] > max_node:
                max_node = node[1]

        return max_node

    def is_inside(pos):
        x = pos[0]
        y = pos[1]-1
        count = {'L': 0, 'F': 0, 'J': 0, '7': 0, '|': 0, '-': 0, '.': 0}
        while y >= 0:
            if (x, y) in visited:
                count[grid[x][y]] += 1
            y -= 1

        return (count['|'] + max(count['F'], count['J']) + max(count['L'], count['7'])) % 2



    def get_inside_nodes():
        inside_count = 0
        for i, _ in enumerate(grid):
            for j, _ in enumerate(grid[0]):
                if (i, j) not in visited and is_inside((i, j)): inside_count += 1

        return inside_count

    for id, line in enumerate(grid):
        if 'S' in line:
            start = (id, line.index('S'))

    set_start()


    print('part 1: ', get_max_node())
    print('part 2: ', get_inside_nodes())
