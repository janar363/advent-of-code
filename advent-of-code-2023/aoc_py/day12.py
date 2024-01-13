import sys

for arg in sys.argv[1:]:
    print('\n', arg)
    with open(arg) as f:
        lines = [line.strip() for line in f.readlines()]

    dp = {}
    def count_arrangements(pattren, records):
        
        if (pattren, records) in dp:
            return dp[(pattren, records)]

        if pattren == "":
            return 1 if len(records) == 0 else 0
        
        if len(records) == 0:
            return 1 if '#' not in pattren else 0
        
        count = 0
        if pattren[0] in '.?':
            count += count_arrangements(pattren[1:], records)

        if pattren[0] in '#?':
            if len(pattren) >= records[0] and '.' not in pattren[:records[0]] and (records[0] == len(pattren) or pattren[records[0]:][0] != '#'):
                count += count_arrangements(pattren[records[0]+1:], records[1:])

        dp[(pattren, records)] = count
        return count

    total = 0
    for line in lines:
        cur = count_arrangements(line.split()[0], tuple(map(int, line.split()[1].split(','))))
        total += cur

    print("part 1: ", total)

    total2 = 0
    for line in lines:
        cur = count_arrangements("?".join([line.split()[0]] * 5), tuple(map(int, line.split()[1].split(','))) * 5)
        total2 += cur
        

    
    print("part 2: ", total2)