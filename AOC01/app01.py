
def get_input(filename):
    with open(filename) as f:
        content = f.readlines()

    return [x.strip() for x in content]

def solve1(input):
    result = 0

    for x in input:
        result += int(x)

    return result


def solve2(input):
    # input is circular - may be needed to reiterate over and over again
    length = len(input)

    occurences = set()
    occurences.add(0)

    ix = -1
    curr_value = 0

    while True:

        ix = 0 if ix == length - 1 else ix + 1

        curr_value += int(input[ix])

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
