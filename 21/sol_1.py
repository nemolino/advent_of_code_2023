from collections import deque

with open('21/input.txt') as f:
    M = tuple(map(lambda x: tuple(x.strip()), f.readlines()))

n_rows, n_cols = len(M), len(M[0])

VISITED = set()
Q = deque()
res = set()

for i in range(n_rows):
    for j in range(n_cols):
        if M[i][j] == 'S':
            p = i,j,0           # 3rd field is the distance from S
            VISITED.add(p)
            Q.append(p)

def update_structures(p_i, p_j, p_dist):
    p = p_i,p_j,p_dist
    if p not in VISITED:
        VISITED.add(p)
        Q.append(p)

while Q:

    p_i, p_j, p_dist = Q.popleft()

    if p_dist == 64:
        res.add(tuple([p_i, p_j]))
        continue

    if p_i-1 >= 0 and M[p_i-1][p_j] != '#':
        update_structures(p_i-1, p_j, p_dist+1)

    if p_i+1 < n_rows and M[p_i+1][p_j] != '#':
        update_structures(p_i+1, p_j, p_dist+1)

    if p_j-1 >= 0 and M[p_i][p_j-1] != '#':
        update_structures(p_i, p_j-1, p_dist+1)

    if p_j+1 < n_cols and M[p_i][p_j+1] != '#':
        update_structures(p_i, p_j+1, p_dist+1)

print('part1 :', len(res))