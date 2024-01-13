with open('input') as f:
    lines = f.readlines()

total = 0
total_2 = 0
test = {'red': 12, 'green': 13, 'blue':14}
for line in lines:
    game, plays = line.strip().split(':')
    actual = {'red': 0, 'green': 0, 'blue':0}
    for play in plays.split(';'):
        for color in play.split(','):
            color_data = color.strip().split()
            actual[color_data[1]] = max(actual[color_data[1]], int(color_data[0]))
    
    flag = 1
    power_cube = 1
    for color_key in test.keys():
        power_cube *= actual[color_key]
        if test[color_key] >= actual[color_key]:
            flag &= 1
        else:
            flag &= 0

    if flag:
        total += int(game.split()[1])

    # part 2
    total_2 += power_cube

print("part 1: ", total)
print("part 2: ", total_2)
