import sys
for arg in sys.argv[1:]:
    print()
    with open(arg) as f:
        times, dists = [[int(val) for val in line.strip().split(':')[1].strip().split()] for line in f.readlines()]

    total = 1
    for idx, dist in enumerate(dists):
        race_time = times[idx]
        count = 0
        for holding_time in range(0, race_time//2+1):
            true_race_time = race_time - holding_time
            if true_race_time * holding_time > dist:
                
                total *= 1 + race_time - holding_time * 2 
                break
        
        # total *= count * 2 if race_time % 2 == 1 else count * 2 - 1
    with open(arg) as f:
        times, dists = [[int("".join(line.strip().split(':')[1].strip().split()))] for line in f.readlines()]

    total_2 = 1
    for idx, dist in enumerate(dists):
        race_time = times[idx]
        count = 0
        for holding_time in range(0, race_time//2+1):
            true_race_time = race_time - holding_time
            if true_race_time * holding_time > dist:
                
                total_2 *= 1 + race_time - holding_time * 2 
                break

    
    print('part 1: ', total)
    print('part 2: ', total_2)


















