import sys
import math

for arg in sys.argv[1:]:
    print('\n', arg)
    with open(arg) as f:
        directions, routes = f.read().split('\n\n')

    map = {}
    startLocations = []
    endLocations = []
    for route in routes.split('\n'):

        location = route.split(' = ')[0]
        nextroutes = route.split(' = ')[1][1:-1].split(', ')
        
        map[location] = nextroutes

        if location[-1] == 'A':
            startLocations.append(location)
        elif location[-1] == 'Z':
            endLocations.append(location)
    
    def part1():
        cur = "AAA"
        dest = "ZZZ"

        steps = 0
        while cur != dest:
            nextDir = directions[steps%len(directions)]

            if nextDir == 'L':
                cur = map[cur][0]
            else:
                cur = map[cur][1]
            
            
            steps += 1
        return steps
    
    def get_steps(start):
        cur = start

        steps = 0
        while cur[-1] != 'Z':
            nextDir = directions[steps%len(directions)]

            if nextDir == 'L':
                cur = map[cur][0]
            else:
                cur = map[cur][1]
            
            
            steps += 1
        return steps

    steps = []
    for loc in startLocations:
        steps.append(get_steps(loc))

    lcm = steps[0]
    for step in steps[1:]:
        lcm = math.lcm(lcm, step)

    print("part 1: ", 0)
    print('part 2: ', lcm)

        
