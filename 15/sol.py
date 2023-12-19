with open('15/input.txt') as f:
    seq = f.read().strip().split(',')

def compute_hash(string):
    cur = 0
    for c in string:
        cur = ((cur + ord(c)) * 17) % 256
    return cur

print('part1:', sum(compute_hash(string) for string in seq))

BOXES = [[] for _ in range(256)]

for string in seq:
    
    if string[-1] == '-':   # - operation
        
        label = string[:-1]
        box_number = compute_hash(label)

        for i,el in enumerate(BOXES[box_number]):
            if el[0] == label:
                BOXES[box_number] = BOXES[box_number][:i] + BOXES[box_number][i+1:]
                break

    else:                   # = operation
        
        label, focal_length = string.split('=')
        box_number = compute_hash(label)
        
        entry = tuple([label, int(focal_length)])

        for i,el in enumerate(BOXES[box_number]):
            if el[0] == label:
                BOXES[box_number][i] = entry
                break
        else:
            BOXES[box_number].append(entry)

res = sum((i+1) * (j+1) * el[1] for i,box in enumerate(BOXES) 
                                    for j,el in enumerate(box))

print('part2:', res)