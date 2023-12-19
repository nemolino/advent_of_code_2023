### this problem was quite hard

with open('05/input.txt') as f:
    input = f.read().split('\n\n')

seeds = list(map(lambda x: int(x), input[0].split(': ')[1].split()))
seeds = [tuple([seeds[i], seeds[i]+seeds[i+1]]) for i in range(0,len(seeds),2)]

# every seed is [start, end)
# every rule is ([src_start,src_end), to_add)

for map_step in input[1:]:

    rules = [tuple(map(lambda y: int(y), x.split())) for x in map_step.split('\n')[1:]]
    
    for i in range(len(rules)):
        rules[i] = tuple([tuple([rules[i][1],
                                 rules[i][1]+rules[i][2]]), 
                                rules[i][0]-rules[i][1]])
    updated_seeds = []

    for r in rules:

        src_start, src_end = r[0]
        shift = r[1]

        for i in range(len(seeds)): 

            if seeds[i] is not None:

                if seeds[i][0] >= src_start and seeds[i][1] < src_end:

                    # range del seed contenuto interamente nel range della regola
                    #   rrrrrrrrrrrrrr
                    #       sssss

                    updated_seeds.append(tuple([seeds[i][0]+shift, 
                                                seeds[i][1]+shift]))
                    seeds[i] = None

                elif seeds[i][0] < src_start and src_start <= seeds[i][1] < src_end:

                    # fine range del seed contenuta parzialmente nel range della regola
                    #      rrrrrrrrrrr
                    #   ssssssss

                    updated_seeds.append(tuple([src_start+shift, 
                                                seeds[i][1]+shift]))
                    seeds[i] = tuple([seeds[i][0], src_start-1])

                elif seeds[i][1] >= src_end and src_start <= seeds[i][0] < src_end:

                    # inizio range del seed contenuto parzialmente nel range della regola
                    #   rrrrrrrrrrr
                    #          ssssssss

                    updated_seeds.append(tuple([seeds[i][0]+shift, 
                                                src_end+shift]))
                    seeds[i] = tuple([src_end, seeds[i][1]])

    seeds = list(filter(lambda x: x is not None, seeds))
    seeds.extend(updated_seeds)

print('part2 :', min(seeds, key=lambda x: x[0])[0])   
