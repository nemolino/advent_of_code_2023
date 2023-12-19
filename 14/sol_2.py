from more_itertools import locate

with open('14/input.txt') as f:
    M = list(map(lambda x: list(x.strip()), f.readlines()))

n = len(M) # M è una matrice quadrata

# D = dict()
res = 0

def move_circles(l, reverse):

    indexes = list(locate(l, lambda x: x == '#'))
        
    if len(indexes) == 0:
        l = sorted(l, reverse=reverse)
    else:
        l = sorted(l[:indexes[0]], reverse=reverse) + l[indexes[0]:]
        for i in range(len(indexes)-1):
            l = l[:indexes[i]+1] + sorted(l[indexes[i]+1:indexes[i+1]], reverse=reverse) + l[indexes[i+1]:]
        l = l[:indexes[-1]+1] + sorted(l[indexes[-1]+1:], reverse=reverse)
    
    return l


for n_cycle in range(1000000000):

    # NORTH
    for j in range(n):

        col = [M[i][j] for i in range(n)]
        col = move_circles(col, True)
        for i in range(n):
            M[i][j] = col[i]

    # WEST
    for i in range(n):

        row = [M[i][j] for j in range(n)]
        row = move_circles(row, True)
        for j in range(n):
            M[i][j] = row[j]

    # SOUTH
    for j in range(n):

        col = [M[i][j] for i in range(n)]
        col = move_circles(col, False)
        for i in range(n):
            M[i][j] = col[i]
    
    # EAST
    for i in range(n):

        row = [M[i][j] for j in range(n)]
        row = move_circles(row, False)
        for j in range(n):
            M[i][j] = row[j]


    ## some stuff to find out the periodicity of the resulting matrix
    ## I discovered that after the cycle 1000000000
    ## the configuration will be the same as after the cycle 118

    """
    print('after',n_cycle+1)
    
    tuple_M = tuple([tuple(M[i]) for i in range(n)])
    h = hash(tuple_M)
    if h in D: 
        print(n_cycle+1, 'same as', D[h])
        #break
    else: 
        D[h] = n_cycle+1
    """
    
    if n_cycle+1 == 118:
        
        for j in range(n):
            col = [M[i][j] for i in range(n)]
            res += sum(n-k if el == 'O' else 0 for k,el in enumerate(col))
        break
    
print('part2 :', res)