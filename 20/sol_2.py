from collections import deque
from numpy import lcm

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

"""
idea:   brute-force does not work
        input forms the graph represented in input_graph.png
        looking at the graph you can derive that rx receives L when 
        the nodes &bn &rt &gp and &cz simultaneously send L
        if we analyze the button presses in which any of this nodes outputs L
        we note that there is periodicity 
        we store in SENT the first 3 indexes of the presses in which the nodes sent L 
"""

SENT = {'bn':[],'rt':[],'gp':[],'cz':[]}

n_button_presses = 0
while True:

    n_button_presses += 1

    Q = Q_start.copy()

    while Q:

        p_type, dest, sender = Q.popleft()

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

                    ###
                    if to_send == 'L' and dest in ['bn','rt','gp','cz']:
                        if n_button_presses not in SENT[dest]:
                            SENT[dest].append(n_button_presses)
                    ###

            case _:     raise AssertionError()

    if all(len(SENT[k]) >= 3 for k in SENT):
        break

"""
{
    'bn': [3889, 7778, 11667], -> bn sends L every 3889 presses
    'rt': [4021, 8042, 12063], -> rt sends L every 4021 presses
    'gp': [3881, 7762, 11643], -> gp sends L every 3881 presses
    'cz': [4013, 8026, 12039]  -> cz sends L every 4013 presses
 }

they simultaneously send L for the first time at press mcm(3889,4021,3881,4013)

"""

print('part2 :', lcm.reduce([SENT[k][0] for k in SENT]))