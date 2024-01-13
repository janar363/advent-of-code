import sys
from copy import deepcopy

def cycle():
    global grid
    
    for _ in range(4):
        
        grid = tuple("".join(row) for row in list(zip(*grid)))

        grid = tuple('#'.join(["".join(sorted(list(section), reverse=True)) for section in row.split('#')]) for row in grid)

        grid = tuple(row[::-1] for row in grid)


for arg in sys.argv[1:]:
    print('\n', arg)
    with open(arg) as f:
        grid = tuple(line.strip() for line in f.readlines())

    initial_grid = deepcopy(grid)

    grid = ["".join(row) for row in list(zip(*grid))]

    grid = ['#'.join(["".join(sorted(list(section), reverse=True)) for section in row.split('#')]) for row in grid]
    
    print("part 1: ",sum([row.count('O') * (len(grid) - r)  for r, row in enumerate(list(zip(*grid)))]))

    dp = {}
    grid = deepcopy(initial_grid)
    dp[grid] = 0
    
    i = 0
    while i >= 0:
        i += 1
        cycle()
        
        if grid in dp:
            dp[grid].append(i)
            break

        dp[grid] = [i]

    min_iteration = dp[grid][0] - 1 + (1000000000 - (dp[grid][0] - 1)) % (dp[grid][1]-dp[grid][0])

    grid = initial_grid
    for i in range(min_iteration):
        cycle()

    print("part 2: ", sum([row.count('O') * (len(grid) - r) for r, row in enumerate(grid)]))


    