from itertools import cycle

def get_input(filename):
    with open(filename) as f:
        return [x.strip() for x in f.readlines()]

def solve1(input):
    return sum([int(x) for x in input])


def solve2(input):
    occurences = set()
    occurences.add(0)
    curr_value = 0

    for x in cycle(input):
        curr_value += int(x)

        if curr_value in occurences:
            return curr_value
        else:
            occurences.add(curr_value)


if __name__ == "__main__":

    input = get_input('D:\\repos\\adventofcode2018\\AOC01\\in01.io')

    result1 = solve1(input) #result1 = 425
    print(f'The result is: {result1}')

    result2 = solve2(input) # result 2 => 57538
    print(f'The result is: {result2}')
