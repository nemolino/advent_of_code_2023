with open('11/input.txt') as f:
    M = list(map(lambda x: list(x.strip()), f.readlines()))

n = len(M)

galaxies = []
for i in range(n):
    for j in range(n):
        if M[i][j] == '#':
            galaxies.append(tuple([i,j]))

empty_rows = []
for i in range(n):
    if '#' not in M[i]:
        empty_rows.append(i)

empty_cols = []
for j in range(n):
    for i in range(n):
        if M[i][j] == '#': 
            break
    else:
        empty_cols.append(j)


def calculate_distance(g1, g2, part2=None):

    if part2 is None: raise ValueError()
    inc = 1 if part2 == False else 999999

    r1,r2 = min(g1[0],g2[0]), max(g1[0],g2[0])
    c1,c2 = min(g1[1],g2[1]), max(g1[1],g2[1])

    dist = r2 - r1 + c2 - c1

    for r in empty_rows: 
        if r1 < r < r2: dist += inc

    for c in empty_cols:
        if c1 < c < c2: dist += inc
    
    return dist


res1 = sum(calculate_distance(galaxies[i],galaxies[j], False) 
          for i in range(len(galaxies)) 
          for j in range(i+1, len(galaxies)))

print('part1 :',res1)


res2 = sum(calculate_distance(galaxies[i],galaxies[j], True) 
          for i in range(len(galaxies)) 
          for j in range(i+1, len(galaxies)))

print('part2 :',res2)