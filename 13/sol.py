with open('13/input.txt') as f:
    input = f.read().split("\n\n")

T = [2**i for i in range(25)] # precomputing some powers of 2

def check_symmetry(ids):

    symmetries = []

    for i in range(1,len(ids)):
        
        idx_sx, idx_dx = i-1, i

        while ids[idx_sx] == ids[idx_dx]:
            idx_dx += 1
            idx_sx -= 1
            if idx_sx < 0 or idx_dx >= len(ids):
                symmetries.append(i)
                break
    
    if len(symmetries) == 1: return symmetries[0]
    if len(symmetries) > 1: return symmetries
    return None

res1, res2 = 0,0

for pattern in input:

    m = list(map(lambda x: list(x), pattern.split("\n")))

    row_id = [sum(T[i] if el == '#' else 0 for (i,el) in enumerate(row)) for row in m]
    old_type_of_symmetry = ''
    symm = check_symmetry(row_id) 
    # assert type(symm) != list
    if symm is not None: 
        res1 += symm * 100
        old_type_of_symmetry = f'row{symm}'
    else:
        col_id = [sum(T[i] if m[i][j] == '#' else 0 for i in range(len(m))) for j in range(len(m[0]))]
        symm = check_symmetry(col_id)
        # assert type(symm) != list
        # assert symm is not None
        res1 += symm
        old_type_of_symmetry = f'col{symm}'


    # part2

    break_all = False
    for i in range(len(m)):
        for j in range(len(m[0])):

            m[i][j] = '.' if m[i][j] == '#' else '#'

            row_id = [sum(T[i] if el == '#' else 0 for (i,el) in enumerate(row)) for row in m]
            symm = check_symmetry(row_id) 

            if type(symm) == list: 
                symm.remove(int(old_type_of_symmetry[3:]))
                symm = symm[0]

            if symm is not None and f'row{symm}' != old_type_of_symmetry: 
                res2 += symm * 100
                break_all = True
                break

            col_id = [sum(T[i] if m[i][j] == '#' else 0 for i in range(len(m))) for j in range(len(m[0]))]
            symm = check_symmetry(col_id)

            if type(symm) == list: 
                symm.remove(int(old_type_of_symmetry[3:]))
                symm = symm[0]
            
            if symm is not None and f'col{symm}' != old_type_of_symmetry: 
                res2 += symm
                break_all = True
                break
            
            m[i][j] = '.' if m[i][j] == '#' else '#'
        
        if break_all: break
    
    
print('part1 :',res1)
print('part2 :',res2)