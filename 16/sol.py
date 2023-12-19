from enum import Enum
from collections import deque

with open('16/input.txt') as f:
    M = list(map(lambda x: list(x.strip()), f.readlines()))

n = len(M)

Dir = Enum('Dir', ['RIGHT', 'DOWN', 'LEFT', 'UP'])

class State:

    def __init__(self, i, j, dir):
        self.i = i
        self.j = j
        self.dir = dir

    def __str__(self):
        return f"i = {self.i}, j = {self.j}, dir = {self.dir}"


def simulate(i_start, j_start, dir_start):

    VISITED = set()
    VISITED_WITH_DIR = set()

    Q = deque([State(i=i_start,j=j_start,dir=dir_start)])

    while Q:

        s = Q.pop()

        while tuple([s.i, s.j, s.dir]) not in VISITED_WITH_DIR:

            if not (0 <= s.i < n and 0 <= s.j < n):
                break

            VISITED_WITH_DIR.add(tuple([s.i, s.j, s.dir]))
            VISITED.add(tuple([s.i, s.j]))

            match s.dir:

                case Dir.RIGHT:

                    match M[s.i][s.j]:
                        case '.'|'-':   s = State(s.i, s.j+1, s.dir)
                        case '/':       s = State(s.i-1, s.j, Dir.UP)
                        case '\\':      s = State(s.i+1, s.j, Dir.DOWN)
                        case '|':
                                        s = State(s.i-1, s.j, Dir.UP)
                                        Q.append(State(s.i+1, s.j, Dir.DOWN))

                case Dir.DOWN:

                    match M[s.i][s.j]:
                        case '.'|'|':   s = State(s.i+1, s.j, s.dir)
                        case '/':       s = State(s.i, s.j-1, Dir.LEFT)
                        case '\\':      s = State(s.i, s.j+1, Dir.RIGHT)
                        case '-':
                                        s = State(s.i, s.j-1, Dir.LEFT)
                                        Q.append(State(s.i, s.j+1, Dir.RIGHT))

                case Dir.LEFT:

                    match M[s.i][s.j]:
                        case '.'|'-':   s = State(s.i, s.j-1, s.dir)
                        case '/':       s = State(s.i+1, s.j, Dir.DOWN)
                        case '\\':      s = State(s.i-1, s.j, Dir.UP)
                        case '|':
                                        s = State(s.i-1, s.j, Dir.UP)
                                        Q.append(State(s.i+1, s.j, Dir.DOWN))

                case Dir.UP:

                    match M[s.i][s.j]:
                        case '.'|'|':   s = State(s.i-1, s.j, s.dir)
                        case '/':       s = State(s.i, s.j+1, Dir.RIGHT)
                        case '\\':      s = State(s.i, s.j-1, Dir.LEFT)
                        case '-':          
                                        s = State(s.i, s.j-1, Dir.LEFT)
                                        Q.append(State(s.i, s.j+1, Dir.RIGHT))
    return len(VISITED)

print('part1 :', simulate(0, 0, Dir.RIGHT))

print('part2 :',    max([   max(simulate(i,   0,   Dir.RIGHT) for i in range(n)),
                            max(simulate(0,   j,   Dir.DOWN ) for j in range(n)),
                            max(simulate(i,   n-1, Dir.LEFT ) for i in range(n)),
                            max(simulate(n-1, j,   Dir.UP   ) for j in range(n))
                        ]))