import sys
from copy import deepcopy
from collections import deque
from heapq import heappush, heappop

for arg in sys.argv[1:]:
    print('\n', arg)
    
    with open(arg) as f:
        instructions = [tuple(data if not data[0].isnumeric() else int(data) for data in line.strip().split()) for line in f.readlines()]

    def get_next_cood(cur, instruction):
        if instruction[0] in 'R0': return (cur[0], cur[1] + instruction[1])
        if instruction[0] in 'D1': return (cur[0] + instruction[1], cur[1])
        if instruction[0] in 'L2': return (cur[0], cur[1] - instruction[1])
        if instruction[0] in 'U3': return (cur[0] - instruction[1], cur[1])
        

    def get_vol(instructions):
        borderPts = 0
        coods = []
        cur = (0, 0)

        for instruction in instructions:
            borderPts += instruction[1]
            coods.append(get_next_cood(cur, instruction))
            cur = coods[-1]

        # shoelace theorm to find inner area = 1/2 sum(xi * yi+1 - xi+1 * yi)
        innerArea = 0
        for i, _ in enumerate(coods):
            innerArea += coods[i][0] * coods[(i+1)%len(coods)][1] - coods[(i+1)%len(coods)][0] * coods[i][1]
        
        innerArea = abs(innerArea) // 2

        # picks theorms to find inner points = innerarea - borderpoints / 2 + 1
        innerPts = innerArea - borderPts // 2 + 1

        return borderPts + innerPts

    print("part 1: ", get_vol(instructions))

    new_instructions = [[inst[2].split('#')[1][5:6], int(inst[2].split('#')[1][:5], 16)] for inst in instructions]

    print("part 2: ", get_vol(new_instructions))