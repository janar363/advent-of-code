with open('input') as f:
    lines = [line.strip() for line in f.readlines()]

total = 0
my_cards = {}
for line in lines:
    winings = 0
    winings_c = 0
    card_num, nums = line.split(':')
    card_num = int(card_num.split()[1])
    my_cards.setdefault(card_num, 0)
    my_cards[card_num] += 1

    win_nums, my_nums = nums.strip().split(' | ')

    win_nums = set([int(n) for n in win_nums.split()])
    my_nums = [int(n) for n in my_nums.split()]

    for my_num in my_nums:
        if my_num in win_nums:
            winings_c += 1
            if winings == 0:
                winings = 1
            else:
                winings *= 2

    for wining_card in range(card_num+1, card_num+winings_c+1):
        my_cards.setdefault(wining_card, 0)
        my_cards[wining_card] += my_cards[card_num]

    total += winings

total_2 = 0
for _, my_card_count in my_cards.items():
    total_2 += my_card_count


print("part 1: ", total)
print("part 2: ", total_2)
    