with open('04/input.txt') as f:
    lines = f.readlines()

count_card = [1] * len(lines)
count_matching = [0] * len(lines)

for i,l in enumerate(lines):
    winning, played = l[10:].strip().split(' | ')
    count_matching[i] = len(set(winning.split()) & set(played.split()))

print('part1 :', sum(2**(c-1) if c > 0 else 0 for c in count_matching))

for i,c in enumerate(count_matching):
    if c > 0:
        for j in range(i+1, i+1+c):
            count_card[j] += count_card[i]

print('part2 :', sum(count_card))