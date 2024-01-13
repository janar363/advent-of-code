import sys
from copy import deepcopy

def Hash(sequence):
    current_val = 0
    for ch in sequence:
        current_val += ord(ch)
        current_val *= 17
        current_val %= 256

    return current_val

for arg in sys.argv[1:]:
    print('\n', arg)
    with open(arg) as f:
        sequences = f.read().strip().split(',')

    total = 0
    for sequence in sequences:
        total += Hash(sequence)

    print("part 1: ", total)

    boxes = {}
    for i in range(256):
        boxes[i] = [[], []]

    for sequence in sequences:
        operation = '-' if '-' in sequence else '='

        name = sequence.split(operation)[0]

        hash = Hash(name)

        if operation == '=':
            if name not in boxes[hash][0]:
                boxes[hash][0].append(name)
                boxes[hash][1].append(int(sequence.split(operation)[1]))
            else:
                idx = boxes[hash][0].index(name)
                boxes[hash][1][idx] = int(sequence.split(operation)[1])
        else:
            if name in boxes[hash][0]:
                idx = boxes[hash][0].index(name)
                boxes[hash][0].pop(idx)
                boxes[hash][1].pop(idx)
    
    total_2 = 0
    for i in range(256):
        if boxes[i][0] != []:
            cur_power = 0
            for idx, val in enumerate(boxes[i][1]):
                cur_power = (i+1) * (idx+1) * val 

                total_2 += cur_power
            
    print("part 2: ", total_2)