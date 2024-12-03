lvls = []

with open('input') as f:
    for line in f.readlines():
        lvls.append([int(num) for num in line.split()])

part1 = len(lvls)
part2 = len(lvls)

def failCheck(lvl):
    inc = True
    if lvl[0] > lvl[1]:
        inc = True
    else:
        inc = False
    for i in range(len(lvl)-1):
        if not (inc == (lvl[i] > lvl[i+1]) and  1<= abs(lvl[i] - lvl[i+1]) <= 3):
            return True
    return False
        
def failCheck2(lvl):

    if failCheck(lvl):
        for i in range(0, len(lvl)):
            if failCheck(lvl[:i] + lvl[i+1:]) == False:
                return False
        return True

    return False

for lvl in lvls:
    if failCheck(lvl):
            part1 -= 1
    if failCheck2(lvl):
        part2 -= 1


print("part 1: ", part1)
print("part 2: ", part2)