import time
import datetime


start_time = time.time() 

# input start

section_c = 0

with open('day5.txt') as f:
    lines = f.readlines()

seeds = []
seed_soil_map = []
soil_to_fertilize = []
fetilize_to_water = []
water_to_light = []
light_to_temp = []
temp_to_humidity = []
humidity_to_location = []
for i in range(len(lines)):

    line = lines[i]
    if i == 0:
        seeds = [int(num) for num in line.split(':')[1].strip().split(' ')]
    else:
        if line[0].isalpha():
            section_c += 1
            continue
        elif section_c == 1 and line[0].isnumeric():
            seed_start = int(line.split(' ')[1])
            soil_start = int(line.split(' ')[0])
            ss_range = int(line.split(' ')[2])
            seed_soil_map.append([(seed_start, seed_start+ss_range-1), (soil_start, soil_start+ss_range-1)])

        elif section_c == 2 and line[0].isnumeric():
            soil_start = int(line.split(' ')[1])
            fertilize_start = int(line.split(' ')[0])
            sf_range = int(line.split(' ')[2])
            soil_to_fertilize.append([(soil_start, soil_start+sf_range-1), (fertilize_start, fertilize_start+sf_range-1)])

        elif section_c == 3 and line[0].isnumeric():
            fertilize_start = int(line.split(' ')[1])
            water_start = int(line.split(' ')[0])
            fw_range = int(line.split(' ')[2])

            fetilize_to_water.append([(fertilize_start, fertilize_start+fw_range-1), (water_start, water_start+fw_range-1)])

        elif section_c == 4 and line[0].isnumeric():
            water_start = int(line.split(' ')[1]) 
            light_start = int(line.split(' ')[0])
            wl_range = int(line.split(' ')[2])

            water_to_light.append([(water_start, water_start+wl_range-1), (light_start, light_start+wl_range-1)])
        elif section_c == 5 and line[0].isalnum():
            light_start = int(line.split(' ')[1]) 
            temp_start = int(line.split(' ')[0])
            lt_range = int(line.split(' ')[2])

            light_to_temp.append([(light_start, light_start+lt_range-1), (temp_start, temp_start+lt_range-1)])

        elif section_c == 6 and line[0].isnumeric():
            temp_start = int(line.split(' ')[1])
            humidity_start = int(line.split(' ')[0])
            th_range = int(line.split(' ')[2])

            temp_to_humidity.append([(temp_start, temp_start+th_range-1), (humidity_start, humidity_start+th_range-1)])

        elif section_c == 7:
            humidity_start = int(line.split(' ')[1]) 
            location_start = int(line.split(' ')[0]) 
            hl_range = int(line.split(' ')[2]) 

            humidity_to_location.append([(humidity_start, humidity_start+hl_range-1), (location_start, location_start+hl_range-1)])

# input end

seed_ranges = []
for i in range(0, len(seeds), 2):
    seed_ranges.append((seeds[i], seeds[i]+seeds[i+1]-1))


seed_ranges = set(seed_ranges)
def sort_tuples(tuples):
    return sorted(tuples, key=lambda x: x[0][0])

# print("seed_ranges = ", seed_ranges)
maps = [seed_soil_map, soil_to_fertilize, fetilize_to_water, water_to_light, light_to_temp, temp_to_humidity, humidity_to_location]

# mapping seed ranges to loc ranges

for map_idx in range(len(maps)):
    current_map = sort_tuples(maps[map_idx])
    # print("current sorted map = ", current_map)
    soil_ranges = []

    for seed_range in seed_ranges:
        
        r_idx = 0
        balance = True
        for ssr in current_map:
            if r_idx == 0 and seed_range[0] >= ssr[0][0] and seed_range[0] <= ssr[0][1]:
                if seed_range[1] >= ssr[0][0] and seed_range[1] <= ssr[0][1]:
                    soil_ranges.append((ssr[1][0]+seed_range[0] - ssr[0][0], ssr[1][0]+seed_range[1]-ssr[0][0]))
                    balance = False
                    break
                elif seed_range[1] >= ssr[0][0] and seed_range[1] >= ssr[0][1]:
                    soil_ranges.append((ssr[1][0] + seed_range[0] - ssr[0][0], ssr[1][1]))


                r_idx += 1
            
            if r_idx == 1 and seed_range[1] >= ssr[0][0] and seed_range[1] >= ssr[0][1] and seed_range[0] < ssr[0][0] and seed_range[0] < ssr[0][1]:
                soil_ranges.append(ssr[1])
            elif r_idx == 1 and seed_range[1] >= ssr[0][0] and seed_range[1] <= ssr[0][1]:
                soil_ranges.append((ssr[1][0], ssr[1][0]+seed_range[1]-ssr[0][0]))
                balance = False
                break  
            

        if balance:
            if current_map[0][0][0] > seed_range[0]:
                if current_map[0][0][0] <= seed_range[1]:
                    soil_ranges.append((seed_range[0], current_map[0][0][0]-1))
                else:
                    soil_ranges.append(seed_range)
            elif current_map[-1][0][1] < seed_range[0]:
                soil_ranges.append(seed_range)
            else:
                soil_ranges.append((current_map[-1][0][1] + 1, seed_range[1]))

    seed_ranges = set(soil_ranges)


seed_ranges = list(seed_ranges)

min = 0
for i in range(len(seed_ranges)):
    loc_range = seed_ranges[i]

    if i == 0:
        min = loc_range[0]
    
    if min > loc_range[0]:
        min = loc_range[0]

    print(f"curretn min = ", min)

print("min location = ", min)

end_time = time.time()
elapsed_time = end_time - start_time

print("Elapsed time: %f seconds" % elapsed_time)