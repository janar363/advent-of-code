with open('input') as f:
    cData = f.read().strip()

def part1(Data):
    Data = [mulOpr for mulOpr in Data.split('mul') if len(mulOpr) > 0 and mulOpr[0] == '(' and ')' in mulOpr]

    Data = [oprnd[1:].split(')')[0] for oprnd in Data if "," in oprnd]

    Data = [int(num.split(',')[0]) * int(num.split(',')[1]) for num in Data if num.split(',')[0].isnumeric() and  1 <= len(num.split(',')[0]) <= 3 and num.split(',')[1].isnumeric() and 1 <= len(num.split(',')[1]) <= 3]

    return sum(Data)

print("part1 : ", part1(cData))

cData = cData.split("don't()")

part2 = part1(cData[0])

for i in range(1, len(cData)):
    if 'do()' in cData[i]:
        for eachDo in cData[i].split('do()')[1:]:
            part2 += part1(eachDo)

print("part2 : ", part2)
