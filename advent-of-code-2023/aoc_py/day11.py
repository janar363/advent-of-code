import sys
from collections import deque

for arg in sys.argv[1:]:
    print('\n', arg)
    
    def get_sum_of_dist(expand_by):
        with open(arg) as f:
            grid = [list(line.strip()) for line in f.readlines()]

        def manhattan_dist(l1, l2):
            mdist = 0
            for i in range(l1[0]+1, l2[0]+1):
                mdist += grid[i][l1[1]]

            ystart = min(l1[1], l2[1]) + 1
            yend = max(l1[1], l2[1]) + 1

            for j in range(ystart, yend):
                mdist += grid[l2[0]][j]
            
            return mdist
        
        # expaning row wise
        for id, row in enumerate(grid):
            if row.count('#') == 0:
                grid[id] =  [expand_by for i in row]
        
        # expanding column wise
        for id, row in enumerate([list(reversed(r)) for r in zip(*grid)]):
            if row.count('#') == 0:
                for i, _ in enumerate(grid):
                    grid[i][id] = expand_by

        # updating grid with distances between nodes
        galaxy_locations = []
        for i, _ in enumerate(grid):
            for j, _ in enumerate(grid[0]):
                if grid[i][j] == '#': galaxy_locations.append((i, j))

                if grid[i][j] != expand_by: grid[i][j] = 1

        # calculating sum of dists
        total = 0
        for i in range(len(galaxy_locations)-1):
            for j in range(i+1, len(galaxy_locations)):
                cur = manhattan_dist(galaxy_locations[i], galaxy_locations[j])

                total += cur
        
        return total

 

    print("part 1: ", get_sum_of_dist(expand_by=2))
    print("part 2: ", get_sum_of_dist(expand_by=1000000))

