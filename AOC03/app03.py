import re

def get_input(filename):
    with open(filename) as f:
        return [x.strip() for x in f.readlines()]


class Claim(object):

    def __init__(self, id: int, x: int, y: int, w: int, h: int):
        self.id = id
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h


    @staticmethod
    def parse(line):
        p = re.compile('#(\d*)\s@\s(\d*),(\d*):\s(\d*)x(\d*)')
        x = p.match(line)

        return Claim(int(x[1]), int(x[2]), int(x[3]), int(x[4]), int(x[5]))


def solve1(input):

    common = set()
    overlap = set()
    result = 0

    for claim in input:
        for x in range(claim.x1, claim.x2):
            for y in range(claim.y1, claim.y2):
                p = (x, y)

                if p in common and p not in overlap:
                    overlap.add(p)
                    result += 1

                if p not in common:
                    common.add(p)

    return result

def solve2(input):
    return None


if __name__ == "__main__":
    input = get_input('D:\\repos\\adventofcode2018\\AOC03\\input.io')
    parsed_input = list(map(Claim.parse, input))

    result1 = solve1(parsed_input) #result1 => 107820
    print(f'The result is: {result1}')

    result2 = solve2(input) # result 2 =>
    print(f'The result is: {result2}')
