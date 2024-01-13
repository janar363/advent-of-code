import sys
from copy import deepcopy
import numpy as np
for arg in sys.argv[1:]:
    print('\n', arg)
    with open(arg) as f:
        cards = [(line.strip().split()[0], int(line.strip().split()[1])) for line in f.readlines()]
    
    # part 1 functions
    def get_type(card):
        count = []
        for ch in card[0]:
            count.append(card[0].count(ch))
        
        if 5 in count: return 7
        if 4 in count: return 6
        if 3 in count:
            if 2 in count: return 5
            else: return 4
        if count.count(2) == 4: return 3
        if 2 in count: return 2
        return 1

    def get_map(card):
        char_map = {'A': 'E', 'K': 'D', 'Q': 'C', 'J': 'B', 'T': 'A'}
        card_map = ""

        for ch in card[0]:
            if ch in char_map.keys():
                card_map += char_map[ch]
            else:
                card_map += ch

        return card_map

    def compare(card):
        card_type = get_type(card)
        card_map = get_map(card)

        return (card_type, card_map)

    # part 2 functions
    def get_type_part2(card):
        # same as part 1 but get count of cards without j
        # sort the counts
        # add the jcount to the max of counts
        jcount = card[0].count('J')
        
        hand_wihtout_j = ""
        for ch in card[0]:
            if ch != 'J':
                hand_wihtout_j += ch

        count = [hand_wihtout_j.count(ch) for ch in set(hand_wihtout_j)]
        count.sort(reverse=True)

        if jcount == 5:
            count = [jcount]
        else:
            count[0] += jcount

        # same as part 1
        if 5 in count: return 7
        if 4 in count: return 6
        if 3 in count:
            if 2 in count: return 5
            else: return 4
        if count[1] == 2: return 3
        if 2 in count: return 2
        return 1

    def get_map_part2(card):
        # same as part 1 but now J is mapped to 1 insted of B
        char_map = {'A': 'E', 'K': 'D', 'Q': 'C', 'J': '1', 'T': 'A'}
        card_map = ""

        for ch in card[0]:
            if ch in char_map.keys():
                card_map += char_map[ch]
            else:
                card_map += ch

        
        return card_map

    def compare_part2(card):
        card_type = get_type_part2(card)
        card_map = get_map_part2(card)

        return (card_type, card_map)

    # part 1
    cards.sort(key=compare)

    total = 0
    for id, card in enumerate(cards):
        total += card[1] * (id+1)

    # part 2
    cards.sort(key=compare_part2)

    total_2 = 0
    for id, card in enumerate(cards):
        total_2 += card[1] * (id+1)
    
    print('part 1: ', total)
    print('part 2: ', total_2)