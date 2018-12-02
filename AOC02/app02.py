from itertools import groupby, filterfalse

def get_input(filename):
    with open(filename) as f:
        return [x.strip() for x in f.readlines()]

def solve1(input):

    counters = [0 , 0]

    for box_id in input:
        freq = dict((k, len(list(g))) for k, g in groupby(sorted(box_id)))

        if any( v == 2  for _, v in freq.items()):
            counters[0] += 1

        if any( v == 3 for _, v in freq.items()):
            counters[1] += 1


    return counters[0] * counters[1]


def solve2(input):

    def are_similar(a: str, b: str):
        if len(a) != len(b):
            return False

        diff = 0

        for i in range(0, len(a)):
            if a[i] == b[i]:
                continue
            else:
                diff += 1

            if diff > 1:
                return False

        return True

    def get_common(a: str, b: str):
        return ''.join(filter(lambda x: x is not None, [(yield a[i] if a[i] == b[i] else None) for i in range(0, len(a))]))

    for i in range(0, len(input) - 1):
        a = input[i]

        for j in range(i + 1, len(input)):
            b = input[j]

            if are_similar(a, b) == True:
                return get_common(a, b)

    return None


if __name__ == "__main__":
    input = get_input('D:\\repos\\adventofcode2018\\AOC02\\input01.io')

    result1 = solve1(input) #result1 => 7776
    print(f'The result is: {result1}')

    result2 = solve2(input) # result 2 => wlkigsqyfecjqqmnxaktdrhbz
    print(f'The result is: {result2}')
