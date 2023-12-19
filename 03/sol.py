import re

with open('03/input.txt') as f:
    lines = f.readlines()
    
D = {}
for i,l in enumerate(lines):
    for m in re.finditer(r'\d+', l):
        D[(i, m.span()[0])] = int(m.group())
D2 = D.copy()

mat = list(map(lambda x: list(x.strip()), lines))
N = len(mat)

FOUND = set()

res1, res2 = 0, 0
for i in range(N):
    for j in range(N):
        if mat[i][j] not in '.0123456789':

            for adj_j, adj_i in ((j-1, i-1), (j, i-1),   (j+1, i-1),
                                 (j-1, i  ),             (j+1, i  ),
                                 (j-1, i+1), (j, i+1),   (j+1, i+1)):
                
                if 0 <= adj_i < N and 0 <= adj_j < N and mat[adj_i][adj_j] in '0123456789':

                        while True:

                            if adj_j-1 < 0 or mat[adj_i][adj_j-1] not in '0123456789':

                                if (adj_i, adj_j) in D:
                                    res1 += D[(adj_i, adj_j)]
                                    del(D[(adj_i, adj_j)])

                                if mat[i][j] == '*' and (adj_i, adj_j) in D2:
                                        FOUND.add((adj_i, adj_j))

                                break
                            
                            adj_j -= 1
            
            if len(FOUND) == 2:
                res2 += D2[FOUND.pop()] * D2[FOUND.pop()]
            FOUND.clear()

print('part1:', res1)
print('part2:', res2)