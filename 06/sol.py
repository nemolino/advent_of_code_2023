from math import floor, ceil, sqrt

def calculate(T,D):
    res = 1
    for i in range(len(T)):
        delta = sqrt(T[i]**2 - 4*D[i])
        x1 = (T[i] - delta) / 2
        x2 = (T[i] + delta) / 2
        x1 = x1 + 1 if x1 % 1 == 0 else ceil(x1)
        x2 = x2 - 1 if x2 % 1 == 0 else floor(x2)
        res *= (x2 - x1 + 1)
    return res

T = [45,98,83,73]
D = [295,1734,1278,1210]
print('part1 :', calculate(T,D))

T = [45988373]
D = [295173412781210]
print('part2 :', calculate(T,D))