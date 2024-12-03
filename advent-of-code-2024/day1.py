l = []
r = []
with open('input') as f:
    lines = f.readlines()
    for line in lines:
        l.append(int(line.split()[0]))
        r.append(int(line.split()[1]))

part1 = 0
l.sort()
r.sort()
for i in range(0, len(l)):
    part1 += abs(l[i] - r[i])
print("part 1 : ", part1)


part2 = 0

for i in range(0, len(l)):
    part2 += l[i] * r.count(l[i])

print("part 2 : ", part2)
