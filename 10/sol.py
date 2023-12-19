# idea for part 2 : look at the maths explained in resource_01.png and resource_02.png in day 18

with open('10/input.txt') as f:
    M = list(map(lambda x: list(x.strip()), f.readlines()))

# find S position
for i in range(len(M)):
    flag = False
    for j in range(len(M[0])):
        if M[i][j] == 'S':
            s_pos = [i,j]
            flag = True
            break
    if flag: break

# looking at input.txt we can see that from S you can go either right or down

#   LJL
#   7S-
#   J|L     

loop_tiles = [tuple(s_pos)]  # useful for part2

prev_pos = s_pos[:]
cur_pos = [s_pos[0], s_pos[1]+1]    # we start going right
distance = 1


while cur_pos != s_pos:
    
    x = cur_pos[:]

    loop_tiles.append(tuple(x))

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

V = []
for t in loop_tiles:
    if M[t[0]][t[1]] in ['L','F','J','7','S']:
        V.append(t)

n = len(V)
A =  abs(sum((V[i][0] * V[(i+1)%n][1] - 
              V[(i+1)%n][0] * V[i][1]) 
              for i in range(n))) / 2

print('part2 :', int(A+1-distance/2))