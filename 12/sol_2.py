from functools import lru_cache

with open('12/input.txt') as f:
    input = list(map(lambda x: x.strip(), f.readlines()))


def count_arrangements(record, pattern):

    record += '.'
    pattern = tuple(map(lambda x: '#' * x + '.', pattern))
    LEN_RECORD = len(record)
    LEN_PATTERN = len(pattern)
    MAX_TOTAL_SHIFT = LEN_RECORD - sum(len(p) for p in pattern)

    def match(str_record, str_pattern):

        #assert len(str_record) == len(str_pattern)
        
        for i in range(len(str_record)):
            if (str_pattern[i] == '.' and str_record[i] == '#') or (str_pattern[i] == '#' and str_record[i] == '.'):
                return False
        return True
    
    assert match('?#.','##.') == True
    assert match('.#.','##.') == False
    assert match('???','##.') == True

    @lru_cache
    def f(record_idx, pattern_idx, available_shift): 

        #print(record_idx)

        #print(record_idx, pattern_idx, available_shift)

        assert available_shift >= 0

        if record_idx >= LEN_RECORD:
            return 1 if pattern_idx >= LEN_PATTERN else 0
            
        if pattern_idx >= LEN_PATTERN:
            return 0 if '#' in record[record_idx:] else 1

        l = len(pattern[pattern_idx])
        s = 0
        for shift in range(0, available_shift+1):

            x = record_idx+shift

            if match(record[x:x+l], pattern[pattern_idx]):
                
                s += f(x+l, 
                       pattern_idx+1, 
                       available_shift-shift)

            if record[x] == '#': 
                break

        return s
        
    return f(0,
             0,
             MAX_TOTAL_SHIFT)

res = 0
for l in input:

    record, pattern = l.split()
    pattern = tuple(map(lambda x: int(x), pattern.split(',')))

    record = (record + '?') * 4 + record
    pattern *= 5

    res += count_arrangements(record, pattern)
    
print('part2 :',res)