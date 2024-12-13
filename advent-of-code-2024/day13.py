with open('input') as file:
    ms = []
    ps = []
    for line in file.readlines():
        if line[0] == 'B':
            ms.append([int(each.strip().split('+')[1]) for each in line.strip().split(':')[1].strip().split(',')])
        elif line[0] == 'P': 
            ps.append([int(each.strip().split('=')[1]) for each in line.strip().split(':')[1].strip().split(',')])

def check_integer_solution(a1, b1, c1, a2, b2, c2):
    dy = b1 * a2 - b2 * a1 
    dc = c1 * a2 - c2 * a1
    ys = dc/dy

    if ys.is_integer():
        dy = b1 * ys - b2 * ys
        dc = c1 - c2
        dx = a1 - a2
        xs = (dc - dy) / dx

        if xs.is_integer(): return True, xs, ys

    return False, None, None

part1 = 0
for i in range(0, len(ms), 2):
    a, b = ms[i:i+2]
    p = ps[i//2]

    has_sol, x, y = check_integer_solution(a[0], b[0], p[0], a[1], b[1], p[1])

    if has_sol: part1 += x * 3 + y

print(part1)


with open('input') as file:
    ms = []
    ps = []
    for line in file.readlines():
        if line[0] == 'B':
            ms.append([int(each.strip().split('+')[1]) for each in line.strip().split(':')[1].strip().split(',')])
        elif line[0] == 'P': 
            ps.append([int(each.strip().split('=')[1])+10000000000000 for each in line.strip().split(':')[1].strip().split(',')])

# print(ps)

part2 = 0
for i in range(0, len(ms), 2):
    a, b = ms[i:i+2]
    p = ps[i//2]

    has_sol, x, y = check_integer_solution(a[0], b[0], p[0], a[1], b[1], p[1])

    if has_sol: 
        part2 += x * 3 + y
        # print(f"{i//2+1} has sol")

print(part2)

