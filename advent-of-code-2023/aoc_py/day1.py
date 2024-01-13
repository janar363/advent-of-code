with open('input') as f:
    lines = f.readlines()

total = 0
for line in lines:
    num = ""
    for ch in line:
        if ch.isnumeric():
            if num == '':
                num += ch * 2
            else:
                num = num[:1]+ch
        
    total += int(num)

print("part1 : ", total)

total = 0
numbers_spelled_out = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

for line in lines:
    num = ""
    for idx in range(len(line)):
        
        strs = []
        ch = line[idx]
        for s in [3, 4, 5]:
            if line[idx:min(idx+s, len(line))] in numbers_spelled_out:
                ch = f'{numbers_spelled_out.index(line[idx:min(idx+s, len(line))])+1}'
                break
        
        if ch.isnumeric():
            if num == '':
                num += ch * 2
            else:
                num = num[:1]+ch
        

    total += int(num)

print("part2 : ", total)