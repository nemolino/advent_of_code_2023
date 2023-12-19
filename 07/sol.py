from collections import Counter

with open('07/input.txt') as f:
    input = f.readlines()

CARD_TO_INT = {'A':14, 'K':13, 'Q':12, 'J':11, 'T':10}

FREQ_1ST_TO_STRENGTH = {
    5: lambda _: 7,
    4: lambda _: 6,
    3: lambda freq_2nd: 5 if freq_2nd == 2 else 4,
    2: lambda freq_2nd: 3 if freq_2nd == 2 else 2,
    1: lambda _: 1
}

def solve(input, PART_2 = None):

    if PART_2 is None: raise ValueError('solve: specify if it is PART_2')

    hands = []
    for line in input:
        cards, bid = line.strip().split()
        bid = int(bid)
        cards = list(map(lambda c: CARD_TO_INT[c] if c in CARD_TO_INT else int(c), cards))

        # *****************************************************************
        if PART_2:

            indexes_to_replace = []
            J_count = cards.count(11)
            if J_count > 0:
                cards_without_J = list(filter(lambda x: x != 11, cards))
                if len(cards_without_J) != 0:

                    c = sorted(Counter(cards_without_J).most_common(), 
                            key=lambda x: (x[1], x[0]), 
                            reverse=True)
                    cards_without_J_1st_most_common = c[0][0]

                    for i,c in enumerate(cards):
                        if c == 11: 
                            cards[i] = cards_without_J_1st_most_common
                            indexes_to_replace.append(i)

                else:
                    cards = [14] * 5
                    indexes_to_replace = list(range(0,5))
        # *****************************************************************

        strength = None
        c = Counter(cards).most_common(2)
        freq_1st_most_common = c[0][1]
        freq_2nd_most_common = c[1][1] if len(c) > 1 else 0
        strength = FREQ_1ST_TO_STRENGTH[freq_1st_most_common](freq_2nd_most_common)

        # *****************************************************************
        if PART_2: 
            for i in indexes_to_replace: cards[i] = 1
        # *****************************************************************

        hands.append(tuple([[strength] + cards, bid]))

    return sum((i+1) * h[1] for i,h in enumerate(sorted(hands, key=lambda x: x[0])))

print('part1:', solve(input, PART_2 = False))
print('part2:', solve(input, PART_2 = True))