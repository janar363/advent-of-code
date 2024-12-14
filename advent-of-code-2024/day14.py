with open("input") as file:
    pvs = []
    for line in file.readlines():
        pvs.append([list(map(int, each.split(','))) for each in line.strip().split('p=')[1].split(' v=')])

t = 100
q1 = q2 = q3 = q4 = 0
x = 101 // 2
y = 103 // 2
for i in range(len(pvs)):
    p, v = pvs[i]

    pvs[i] = [[(p[0] + v[0] * t) % 101, (p[1] + v[1] * t) % 103], v]

    p, _ = pvs[i]

    if 0 <= p[0] < 50 and 0 <= p[1] < 51: q1 += 1
    if 0 <= p[0] < 50 and 52 <= p[1] < 103: q2 += 1
    if 51 <= p[0] < 101 and 0 <= p[1] < 51: q3 += 1
    if 51 <= p[0] < 101 and 52 <= p[1] < 103: q4 += 1

print(q1* q2* q3* q4)

T = 10000

# def print_grid(ps):
#     grid = [['.' for j in range(103)]for i in range(101)]
#     for p in ps:
#         grid[p[0][0]][p[0][1]] = '#'

#     for i in range(101):
#         print(''.join([grid[i][j] for j in range(101)]))

#     print()
#     print()
#     for j in range(101):
#         print(''.join([grid[i][j] for i in range(101)]))

    
m = 0
ans = 0
for t in range(1, T):
    with open("input") as file:
        pvs = []
        for line in file.readlines():
            pvs.append([list(map(int, each.split(','))) for each in line.strip().split('p=')[1].split(' v=')])
    part2 = set()
    for i in range(len(pvs)):
        p, v = pvs[i]

        pvs[i] = [[(p[0] + v[0] * t) % 101, (p[1] + v[1] * t) % 103], v]
        part2.add((pvs[i][0][0], pvs[i][0][1]))

    if len(part2) > m:
        m = len(part2)
        ans = t


print(ans)


