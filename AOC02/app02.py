from itertools import groupby

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
    pass


if __name__ == "__main__":

    #input = ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']

    input = get_input('D:\\repos\\adventofcode2018\\AOC02\\input01.io')

    result1 = solve1(input) #result1 => 7776
    print(f'The result is: {result1}')

    #result2 = solve2(input) # result 2 => 57538
    #print(f'The result is: {result2}')
