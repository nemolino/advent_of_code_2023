from collections import deque

with open('20/input.txt') as f:
    input = list(map(lambda x: x.strip(), f.readlines()))

N = dict()
Q_start = deque()

for l in input:
    component, outputs = l.split(' -> ')
    outputs = tuple(outputs.split(', '))
    if component == 'broadcaster':
        for dest in outputs:
            Q_start.append(tuple(['L',dest,component]))
    elif component[0] == '%':
        N[component[1:]] = ['%', 'OFF', outputs]
    elif component[0] == '&':
        N[component[1:]] = ['&', dict(), outputs]
    else: 
        raise AssertionError()

for k in N:
    outputs = N[k][2]
    for o in outputs:
        # it possible that some o is not in N, 
        # these are untyped nodes 
        if o in N and N[o][0] == '&':
            N[o][1][k] = 'L'

countL, countH = 0, 0

for _ in range(1000):

    countL += 1 # counting L pulse from button to broadcaster
    Q = Q_start.copy()

    while Q:

        p_type, dest, sender = Q.popleft()

        match p_type:
            case 'L':   countL += 1
            case 'H':   countH += 1
            case _:     raise AssertionError()

        if dest not in N: 
            continue
        
        match N[dest][0]:

            case '%':   # flip-flop

                if p_type == 'L':
                    N[dest][1] = 'ON' if N[dest][1] == 'OFF' else 'OFF'
                    to_send = 'L' if N[dest][1] == 'OFF' else 'H'
                    for o in N[dest][2]:
                        Q.append(tuple([to_send,o,dest]))

            case '&':   # conjunction

                N[dest][1][sender] = p_type
                to_send = 'L' if all(v == 'H' for v in N[dest][1].values()) else 'H'
                for o in N[dest][2]:
                    Q.append(tuple([to_send,o,dest]))
            
            case _:     raise AssertionError()


print('part1 :', countH * countL)