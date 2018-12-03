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

    def is_overlapped(self, c):
        return (
            self.x1 < c.x2 and
            self.x2 > c.x1 and
            self.y1 < c.y2 and
            self.y2 > c.y1)


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

    for i in range(0, len(input)):
        c1 = input[i]

        is_overlapped = False

        for j in range(0, len(input)):
            if i == j: continue

            c2 = input[j]

            if c1.is_overlapped(c2):
                is_overlapped = True
                break

        if is_overlapped == False:
            return c1.id

    return None


if __name__ == "__main__":
    input = get_input('D:\\repos\\adventofcode2018\\AOC03\\input.io')

    parsed_input = list(map(Claim.parse, input))

    result1 = solve1(parsed_input) #result1 => 107820
    print(f'The result is: {result1}')

    result2 = solve2(parsed_input) # result 2 => 661
    print(f'The result is: {result2}')
