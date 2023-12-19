with open('02/input.txt') as f:
    lines = f.readlines()

D = {'red' : 12, 'green' : 13, 'blue' : 14 }

def analyze(subsets):
    is_valid = True
    D_MAX = {'red' : 0, 'green' : 0, 'blue' : 0 }
    for s in subsets.split('; '):
        for e in s.strip().split(', '):
            n, color = e.split()
            if int(n) > D[color]:
                is_valid = False
            D_MAX[color] = max(D_MAX[color], int(n))
    return (is_valid, D_MAX['red'] * D_MAX['green'] * D_MAX['blue'])


sum_1, sum_2 = 0, 0
for l in lines:
    game_id, subsets = l.split(': ') 
    is_valid, power = analyze(subsets)
    if is_valid:
        sum_1 += int(game_id[5:])
    sum_2 += power


print('part1:', sum_1)
print('part2:', sum_2)