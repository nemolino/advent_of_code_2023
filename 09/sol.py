import numpy as np

with open('09/input.txt') as f:
    input = f.readlines()


def extrapolate(seq):

    seq = np.array(seq)
    next_value = seq[-1]            # part1
    first_values = [seq[0]]         # part2
    while any(x != 0 for x in seq):
        seq = np.diff(seq)
        next_value += seq[-1]       # part1
        first_values.append(seq[0]) # part2

    # part2
    backward_value = 0
    for i in range(len(first_values)-2,-1,-1):
        backward_value = first_values[i] - backward_value

    return next_value, backward_value


results = [extrapolate(list(map(lambda x: int(x), l.strip().split()))) 
          for l in input]

print('part1 :', sum(r[0] for r in results))
print('part2 :', sum(r[1] for r in results))