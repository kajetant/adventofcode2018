from itertools import chain
import operator

def get_input(filename):
    with open(filename) as f:
        return [x.strip() for x in f.readlines()]


def react_polymer(polymer):

    def should_destroy(a, b):
        return a != b and (a.lower() == b or a.upper() == b)

    i = 0

    while i < len(polymer) - 1:

        if not should_destroy(polymer[i], polymer[i+1]):
            i += 1
            continue

        polymer = list(chain(polymer[:i], polymer[i+2:]))

        i = i - 1 if i > 0 else 0

    return polymer


def solve1(polymer):
    return len(react_polymer(polymer))

def solve2(polymer):

    letters = set(map(lambda x: x.lower(), polymer))
    results = dict(map(lambda x: (x, 0), letters))

    for k in letters:
        results[k] = len(react_polymer(list(filter(lambda x: x != k and x != k.upper(), polymer))))

    return min(results.items(), key=operator.itemgetter(1))


if __name__ == "__main__":
    input = get_input('D:\\repos\\adventofcode2018\\AOC05\\input.io')

    result1 = solve1(list(input[0])) #result1 => 10250
    print(f'The result is: {result1}')

    result2 = solve2(list(input[0])) # result 2 => 6188
    print(f'The result is: {result2}')
