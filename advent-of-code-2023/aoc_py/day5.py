from copy import deepcopy
with open('input') as f:
    seeds, *rest = [line for line in f.read().split('\n\n')]

seeds = [int(seed) for seed in seeds.strip().split(':')[1].split()]

start = deepcopy(seeds)
ranges = []
for r in rest:
    cur_range = []
    for line in r.split('\n')[1:]:
        dest, source, delta = map(int, line.split())
        cur_range.append((dest, source, delta))
    ranges.append(sorted(cur_range, key=lambda x: x[1]))

for idx, seed in enumerate(start):
    for category in ranges:
        for dest, source, delta in category:
            if source <= seed < source + delta:
                seed = dest + seed - source
                start[idx] = seed
                break

seeds = [(seeds[sid], seeds[sid] + seeds[sid+1]) for sid in range(0, len(seeds), 2)]
range_in = deepcopy(seeds)

for cid, category in enumerate(ranges):
    
    next_in = []
    
    for seed_range in range_in:
        for dest, source, delta in category:
            if seed_range[0] < source <= seed_range[1] and source <= seed_range[1] < source + delta:
                next_in.append((dest, dest + seed_range[1] - source))
                range_in.append((seed_range[0], source-1))
                break

            if source <= seed_range[0] < source + delta and source <= seed_range[1] < source + delta:
                next_in.append((dest+seed_range[0]-source, dest+seed_range[1]-source))
                break

            if source <= seed_range[0] < source + delta and seed_range[0] < source + delta <= seed_range[1]:
                next_in.append((dest+seed_range[0]-source, dest+delta))
                range_in.append((source+delta, seed_range[1]))
                break
        else:
            next_in.append(seed_range)

    range_in = next_in


print("part 1: ", min(start))
print("part 2: ", sorted(range_in, key=lambda x: x[0])[0][0])