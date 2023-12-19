with open('05/input.txt') as f:
    input = f.read().split('\n\n')

seeds = list(map(lambda x: int(x), input[0].split(': ')[1].split()))

for map_step in input[1:]:

    rules = [tuple(map(lambda y: int(y), x.split())) 
                for x in map_step.split('\n')[1:]]
        
    for i,s in enumerate(seeds):
        for dest_range_start, src_range_start, range_len in rules:
            if src_range_start <= s < src_range_start + range_len:
                seeds[i] -= (src_range_start - dest_range_start) 

print('part1 :', min(seeds))