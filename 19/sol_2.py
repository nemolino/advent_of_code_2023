from collections import deque

with open('19/input.txt') as f:
    workflows, _ = f.read().split('\n\n')

N = dict()

for w in workflows.split('\n'):
    id, rule = w[:-1].split('{')
    N[id] = rule

def generate_children_nodes(s):

    result = []

    rng_x, rng_m, rng_a, rng_s = s[1], s[2], s[3], s[4]
    rule = N[s[0]].split(',')

    for r in rule[:-1]:
        cond, return_value = r.split(':')
        test_value = int(cond[2:])
        match r[0]:

            case 'x':
                if r[1] == '>':
                    new_rng_x = [test_value+1, rng_x[1]] 
                    rng_x[1] = test_value
                else: # r[1] == '<':
                    new_rng_x = [rng_x[0], test_value-1] 
                    rng_x[0] = test_value
                result.append([return_value, new_rng_x, rng_m[:], rng_a[:], rng_s[:]])

            case 'm':
                if r[1] == '>':
                    new_rng_m = [test_value+1, rng_m[1]]
                    rng_m[1] = test_value
                else: # r[1] == '<':
                    new_rng_m = [rng_m[0], test_value-1] 
                    rng_m[0] = test_value
                result.append([return_value, rng_x[:], new_rng_m, rng_a[:], rng_s[:]])

            case 'a':
                if r[1] == '>':
                    new_rng_a = [test_value+1, rng_a[1]] 
                    rng_a[1] = test_value
                else: # r[1] == '<':
                    new_rng_a = [rng_a[0], test_value-1] 
                    rng_a[0] = test_value
                result.append([return_value, rng_x[:], rng_m[:], new_rng_a, rng_s[:]])

            case 's':
                if r[1] == '>':
                    new_rng_s = [test_value+1, rng_s[1]]
                    rng_s[1] = test_value
                else: # r[1] == '<':
                    new_rng_s = [rng_s[0], test_value-1]
                    rng_s[0] = test_value
                result.append([return_value, rng_x[:], rng_m[:], rng_a[:], new_rng_s])
        
    result.append([rule[-1], rng_x, rng_m, rng_a, rng_s])
    return result


res = 0
Q = deque()
Q.append(['in',[1,4000],[1,4000],[1,4000],[1,4000]])

while Q:
    node = Q.pop()
    if node[0] == 'A':
        res += ((node[1][1] - node[1][0] + 1) * 
                (node[2][1] - node[2][0] + 1) * 
                (node[3][1] - node[3][0] + 1) * 
                (node[4][1] - node[4][0] + 1))
    elif node[0] != 'R':
        to_append = generate_children_nodes(node)
        for x in to_append:
            Q.append(x)

print('part2 :', res)