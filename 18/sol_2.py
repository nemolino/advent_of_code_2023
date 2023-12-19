# idea : look at the maths explained in resource_01.png and resource_02.png

with open('18/input.txt') as f:
    input = list(map(lambda x: x.strip().split()[2][2:-1], f.readlines()))

for i,el in enumerate(input):
    dir, step = el[-1], el[:-1]
    if   dir == '0': dir = 'R'
    elif dir == '1': dir = 'D'
    elif dir == '2': dir = 'L'
    else:            dir = 'U'
    step = int('0x'+step, base=16)
    input[i] = dir, step

border_points = 0
p = [0,0]
VERTICES = [tuple(p)]

for l in input:

    dir, step = l
    border_points += step

    match dir:
        case 'U': p[0] -= step
        case 'D': p[0] += step
        case 'R': p[1] += step
        case 'L': p[1] -= step

    VERTICES.append(tuple(p)) 

VERTICES = VERTICES[:-1]

n = len(VERTICES)
A =  abs(sum((VERTICES[i][0] * VERTICES[(i+1)%n][1] - 
              VERTICES[(i+1)%n][0] * VERTICES[i][1]) 
              for i in range(n))) / 2

interior_points = A - border_points/2 + 1

print('part2 :', int(border_points + interior_points))