with open('input') as f:
    grid = [r.strip() for r in f.readlines()]

total = 0

def is_part_number(ridx, visited):
    # print(visited)
    for cidx in visited:
        if ridx != 0 and grid[ridx-1][cidx] != '.' and not grid[ridx-1][cidx].isalnum(): return True
        if ridx != 0 and cidx != 0 and grid[ridx-1][cidx-1] != '.' and not grid[ridx-1][cidx-1].isalnum(): return True
        if ridx != 0 and cidx != len(grid[0])-1 and grid[ridx-1][cidx+1] != '.' and not grid[ridx-1][cidx+1].isalnum(): return True

        if ridx != len(grid)-1 and grid[ridx+1][cidx] != '.' and not grid[ridx+1][cidx].isalnum(): return True
        if ridx != len(grid)-1 and cidx != 0 and grid[ridx+1][cidx-1] != '.' and not grid[ridx+1][cidx-1].isalnum(): return True
        if ridx != len(grid)-1 and cidx != len(grid[0])-1 and grid[ridx+1][cidx+1] != '.' and not grid[ridx+1][cidx+1].isalnum(): return True

        if cidx != 0 and grid[ridx][cidx-1] != '.' and not grid[ridx][cidx-1].isalnum(): return True
        if cidx != len(grid[0])-1 and grid[ridx][cidx+1] != '.' and not grid[ridx][cidx+1].isalnum(): return True

        
    return False

def is_gear_number(ridx, visited):
    # print(visited)
    for cidx in visited:
        if ridx != 0 and grid[ridx-1][cidx] == '*': return True, (ridx-1, cidx)
        if ridx != 0 and cidx != 0 and grid[ridx-1][cidx-1] == '*': return True, (ridx-1, cidx-1)
        if ridx != 0 and cidx != len(grid[0])-1 and grid[ridx-1][cidx+1] == '*': return True, (ridx-1, cidx+1)

        if ridx != len(grid)-1 and grid[ridx+1][cidx] == '*': return True, (ridx+1, cidx)
        if ridx != len(grid)-1 and cidx != 0 and grid[ridx+1][cidx-1] == '*' and not grid[ridx+1][cidx-1].isalnum(): return True, (ridx+1, cidx-1)
        if ridx != len(grid)-1 and cidx != len(grid[0])-1 and grid[ridx+1][cidx+1] == '*': return True, (ridx+1, cidx+1)

        if cidx != 0 and grid[ridx][cidx-1] == '*': return True, (ridx, cidx-1)
        if cidx != len(grid[0])-1 and grid[ridx][cidx+1] == '*': return True, (ridx, cidx+1)

        
    return False, (-1, -1)


gear = {}

for r, row in enumerate(grid):
    visited = set([])
    for c, col in enumerate(grid[r]):
        cur = set([])
        if c not in visited and grid[r][c].isnumeric():
            temp = c
            num = ""
            while temp < len(grid[0]) and grid[r][temp].isnumeric():
                visited.add(temp)
                cur.add(temp)
                num += grid[r][temp]
                temp += 1
            
            if is_part_number(r, cur): 
                total += int(num)

            is_gear_num, gear_idx = is_gear_number(r, cur)

            if is_gear_num:
                if gear_idx not in gear.keys():
                    gear[gear_idx] = []
                gear[gear_idx].append(int(num))
                
total_2 = 0

for _, nums in gear.items():
    if len(nums) == 2:
        total_2 += nums[0] * nums[1]
    

print("part 1: ", total)
print("part 2: ", total_2)
