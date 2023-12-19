import re

with open('01/input.txt') as f:
    lines = f.readlines()

REGEX = r'\d'
res = sum(int(re.search(REGEX, l).group()) * 10 + 
          int(re.search(REGEX, l[::-1]).group()) 
          for l in lines)

print('part1:', res)

str_to_int = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9,
              'eno':1, 'owt':2, 'eerht':3, 'ruof':4, 'evif':5, 'xis':6, 'neves':7, 'thgie':8, 'enin':9}

REGEX_FIRST = r'\d|one|two|three|four|five|six|seven|eight|nine'
REGEX_LAST  = r'\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin'

sum = 0
for l in lines:

    first_digit = re.search(REGEX_FIRST, l).group()
    last_digit = re.search(REGEX_LAST, l[::-1]).group()
    
    first_digit = int(first_digit) if len(first_digit) == 1 else str_to_int[first_digit]
    last_digit = int(last_digit)   if len(last_digit) == 1  else str_to_int[last_digit]

    sum += first_digit * 10 + last_digit

print('part2:', sum)