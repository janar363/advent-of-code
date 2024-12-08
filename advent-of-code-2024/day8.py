with open('input') as file:
    antenas = []
    grid = []
    for line in file.readlines():
        r = []
        line = line.strip()
        for i in range(len(line)):
            if line[i] != '.': antenas.append((len(grid), i))
            r.append(line[i])

        grid.append(r)




part1 = set()

for a1 in range(len(antenas)):
            for a2 in range(a1+1, len(antenas)):
                if grid[antenas[a1][0]][antenas[a1][1]] != grid[antenas[a2][0]][antenas[a2][1]]:
                    continue

                dr = antenas[a1][0] - antenas[a2][0]
                dc = antenas[a1][1] - antenas[a2][1]

                if 0 <= antenas[a1][0] + dr < len(grid) and 0 <= antenas[a1][1] + dc < len(grid[0]): 
                     part1.add((antenas[a1][0] + dr, antenas[a1][1] + dc))
                if 0 <= antenas[a2][0] - dr < len(grid) and 0 <= antenas[a2][1] - dc < len(grid[0]): 
                     part1.add((antenas[a2][0] - dr, antenas[a2][1] - dc))

print(len(part1))

part2 = set()
for a1 in range(len(antenas)):
    for a2 in range(a1+1, len(antenas)):
        if grid[antenas[a1][0]][antenas[a1][1]] != grid[antenas[a2][0]][antenas[a2][1]]:
            continue

        dr = antenas[a1][0] - antenas[a2][0]
        dc = antenas[a1][1] - antenas[a2][1]

        inGrid = True
        i = 0
        while inGrid:
            if 0 <= antenas[a1][0] + dr * i < len(grid) and 0 <= antenas[a1][1] + dc * i < len(grid[0]): 
                 part2.add((antenas[a1][0] + dr * i, antenas[a1][1] + dc * i))
            else:
                break

            i += 1

        inGrid = True
        i = 0
        while inGrid:
            if 0 <= antenas[a2][0] - dr * i < len(grid) and 0 <= antenas[a2][1] - dc * i < len(grid[0]): 
                 part2.add((antenas[a2][0] - dr * i, antenas[a2][1] - dc * i))
            else:
                 break
            
            i += 1

print("part2 : ", len(part2))