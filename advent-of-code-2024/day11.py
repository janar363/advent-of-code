from collections import defaultdict
with open("input") as file:
    a = [int(num) for num in file.read().strip().split()]

print(a)
visited = {}
for i in range(25):
    # print(f"{i}th blink")
    newA = []
    for num in a:
        visited
        if num == 0:
            newA.append(1)
        elif len(str(num)) % 2 == 0:
            num = str(num)
            newA.append(int(num[:len(num)//2])) 
            newA.append(int(num[len(num)//2:]))
        else:
            newA.append(num * 2024)
    a = newA

print("part1 : ", len(a))

with open("input") as file:
    a = [int(num) for num in file.read().strip().split()]

count = defaultdict(int, {num: 1 for num in a})
# print(count)

for i in range(75):
    # print(f"{i}th blink : {sum(v for _, v in count.items())}")
    tCount = defaultdict(int)

    if(tCount == count): print("true")
    
    for num, _ in count.items():
        if num == 0:
            tCount[1] += count[num]
        elif len(str(num)) % 2 == 0:
            snum = str(num)
            tCount[int(snum[:len(snum)//2])] += count[num]
            tCount[int(snum[len(snum)//2:])] += count[num]
        else:
            tCount[num * 2024] += count[num]
            
    count = tCount.copy()

print("part2 : ", sum([v for _, v in count.items()]))
    
