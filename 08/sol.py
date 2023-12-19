import numpy as np

with open('08/input.txt') as f:
    input = f.readlines()

instructions = input[0].strip()
nodes = {}

for l in input[2:]:
    nodes[l[0:3]] = l[7:10], l[12:15]

def solve_part1(nodes):

    count, i = 0, 0
    cur = 'AAA'
    while cur != 'ZZZ':
        cur = nodes[cur][0] if instructions[i] == 'L' else nodes[cur][1]
        count += 1
        i = (i+1) % len(instructions)

    return count

def solve_part2(nodes):

    cur = tuple([k for k in nodes if k[-1] == 'A'])
    pattern = [[] for _ in cur]

    for i,c in enumerate(cur):

        count, j = 0, 0

        while True: 
            
            c = nodes[c][0] if instructions[j] == 'L' else nodes[c][1]
            count += 1
            j = (j+1) % len(instructions)

            if c[-1] == 'Z':

                new = tuple([c,j,count])
                
                if len(pattern[i]) > 0 and any(p[0] == new[0] and p[1] == new[1] 
                                            for p in pattern[i]):
                    break

                pattern[i].append(new)
    
    # for i,p in enumerate(pattern): print(f'pattern {i}: {p}')

    return np.lcm.reduce([p[0][2] for p in pattern])

print('part1:', solve_part1(nodes))
print('part2:', solve_part2(nodes))