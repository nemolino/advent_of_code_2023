from itertools import combinations
from more_itertools import locate

with open('12/input.txt') as f:
    input = list(map(lambda x: x.strip(), f.readlines()))


def count_arrangements(record, pattern):

    # indexes of all occurrences of '?'
    indexes = tuple(locate(record, lambda x: x == '?'))

    # number of positions to fill with asterisk
    k = sum(pattern) - record.count('#')

    record = list(record)
    count = 0

    for comb in combinations(indexes, k): 

        # create arrangement substituting ? characters
        for i in range(len(record)):
            if record[i] == '?':
                record[i] = '#' if i in comb else '.'

        # check arrangement against pattern
        cur_pattern = []
        count_successive = 0
        for c in record:
            if c == '#': 
                count_successive += 1
            elif c == '.' and count_successive > 0:
                cur_pattern.append(count_successive)
                count_successive = 0
        if count_successive > 0:
            cur_pattern.append(count_successive)
        
        if tuple(cur_pattern) == pattern:
            count += 1

        # restore original arrangement re-inserting ? characters
        for i in indexes: 
            record[i] = '?'

    return count
    

res = 0
for l in input:

    record, pattern = l.split()
    pattern = tuple(map(lambda x: int(x), pattern.split(',')))
    res += count_arrangements(record, pattern)
    
print('part1 :',res)