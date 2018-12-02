
def get_input(filename):
    with open(filename) as f:
        content = f.readlines()

    return [x.strip() for x in content]

def solve1(input):
    result = 0

    for x in input:
        result += int(x)

    return result

if __name__ == "__main__":

    input1 = get_input('D:\\repos\\adventofcode2018\\AOC01\\in01.io')

    result = solve1(input1)

    print(f'The result is: {result}')
