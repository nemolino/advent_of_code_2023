# idea : flood fill algorithm

import numpy as np
from collections import deque

with open('18/input.txt') as f:
    input = list(map(lambda x: x.strip(), f.readlines()))

for i,l in enumerate(input):
    dir, step, _ = l.split() 
    input[i] = dir, int(step)

cur_pos = [0, 0]
PATH = set()
PATH.add(tuple(cur_pos))

for l in input:
    dir, step = l
    match dir:
        case 'U':
            for _ in range(1,step+1):
                cur_pos[0] -= 1
                PATH.add(tuple(cur_pos))
        case 'D':
            for _ in range(1,step+1):
                cur_pos[0] += 1
                PATH.add(tuple(cur_pos))
        case 'R':
            for _ in range(1,step+1):
                cur_pos[1] += 1
                PATH.add(tuple(cur_pos))
        case 'L':
            for _ in range(1,step+1):
                cur_pos[1] -= 1
                PATH.add(tuple(cur_pos))
        case _: 
            raise AssertionError()    

max_i = max(t[0] for t in PATH)
min_i = min(t[0] for t in PATH)
max_j = max(t[1] for t in PATH)
min_j = min(t[1] for t in PATH)

n_rows = max_i - min_i + 1 + 2
n_cols = max_j - min_j + 1 + 2

M = np.zeros((n_rows,n_cols), dtype=np.int8)
for t in PATH:
    M[t[0]+1-min_i ][t[1]+1-min_j] = 1

start_j = 0
for j in range(n_cols):
    if M[2][j] == 1: 
        start_j = j+1
        break
# (2, start_j) is an interior point of the polygon

VISITED = set()
Q = deque()
Q.append([2,start_j])

while Q:
    
    i,j = Q.pop()
    
    VISITED.add(tuple[i,j])

    M[i][j] = 1

    if M[i-1,j] == 0 and tuple([i-1,j]) not in VISITED: Q.append([i-1,j])
    if M[i+1,j] == 0 and tuple([i+1,j]) not in VISITED: Q.append([i+1,j])
    if M[i,j-1] == 0 and tuple([i,j-1]) not in VISITED: Q.append([i,j-1])
    if M[i,j+1] == 0 and tuple([i,j+1]) not in VISITED: Q.append([i,j+1])

print('part1 :', len(PATH)+len(VISITED))