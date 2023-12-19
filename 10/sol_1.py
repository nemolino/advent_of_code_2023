with open('10/input.txt') as f:
    M = list(map(lambda x: list(x.strip()), f.readlines()))

n = len(M) 

# find S position
for i in range(n):
    flag = False
    for j in range(n):
        if M[i][j] == 'S':
            s_pos = [i,j]
            flag = True
            break
    if flag: break

# guardando l'input si vede che da S si può andare a dx o sotto

#   LJL
#   7S-
#   J|L     

prev_pos = s_pos[:]
cur_pos = [s_pos[0], s_pos[1]+1]    # partiamo andando a dx
distance = 1

while cur_pos != s_pos:
    
    x = cur_pos[:]

    match M[cur_pos[0]][cur_pos[1]]:

        case "|": 
            if prev_pos[0] == cur_pos[0]-1: cur_pos[0] += 1
            else:                           cur_pos[0] -= 1

        case "-": 
            if prev_pos[1] == cur_pos[1]-1: cur_pos[1] += 1
            else:                           cur_pos[1] -= 1
    
        case "L": 
            if prev_pos[0] == cur_pos[0]-1: cur_pos[1] += 1
            else:                           cur_pos[0] -= 1

        case "J": 
            if prev_pos[0] == cur_pos[0]-1: cur_pos[1] -= 1
            else:                           cur_pos[0] -= 1

        case "7":
            if prev_pos[0] == cur_pos[0]+1: cur_pos[1] -= 1
            else:                           cur_pos[0] += 1

        case "F": 
            if prev_pos[0] == cur_pos[0]+1: cur_pos[1] += 1 
            else:                           cur_pos[0] += 1

        case _: raise AssertionError('unexpected')

    prev_pos = x
    distance += 1

print('part1 :', distance//2)