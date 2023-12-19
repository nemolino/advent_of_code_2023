import numpy as np
from more_itertools import locate

with open('14/input.txt') as f:
    input = np.array(list(map(lambda x: list(x.strip()), f.readlines())))

res = 0
for col in input.transpose():

    c = list(col[:])
    indexes = list(locate(c, lambda x: x == '#'))
    
    if len(indexes) == 0:
        c = sorted(c, reverse=True)
    else:
        c = sorted(c[:indexes[0]], reverse=True) + c[indexes[0]:]
        for i in range(len(indexes)-1):
            c = c[:indexes[i]+1] + sorted(c[indexes[i]+1:indexes[i+1]], reverse=True) + c[indexes[i+1]:]
        c = c[:indexes[-1]+1] + sorted(c[indexes[-1]+1:], reverse=True)
    
    res += sum(len(c)-i if el == 'O' else 0 for i,el in enumerate(c))

    
print('part1 :',res)