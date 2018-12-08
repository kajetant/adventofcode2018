import re
from itertools import count, groupby, product
from functools import reduce
from datetime import datetime
import operator
from typing import List


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


def dist(a: Point, b: Point):
    return abs(a.x - b.x) + abs(a.y - b.y)

def get_input(filename):
    with open(filename) as f:
        return [x.strip() for x in f.readlines()]

def parse_line(line):
    r = re.compile('(\d+),\s(\d+)')
    d = r.match(line).groups()

    return Point(int(d[0]), int(d[1]))


def solve1(points: List[Point]):

    min_x = min(points, key=lambda p: p.x).x
    min_y = min(points, key=lambda p: p.y).y
    max_x = max(points, key=lambda p: p.x).x
    max_y = max(points, key=lambda p: p.y).y

    area_by_point = [0 for i in range(0, len(points))]

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            distances = [(i, dist(points[i], Point(x, y))) for i in range(0, len(points))]

            closest_points = sorted([(k, list(group)) for k, group in groupby(sorted(distances, key=lambda x:x[1]), key=lambda x: x[1])], key=lambda x: x[0])[0]

            if len(closest_points[1]) == 1:
                point_id = closest_points[1][0][0]

                if x == min_x or y == min_y or x == max_x or y == max_y:
                    area_by_point[point_id] = -1
                else:
                    area_by_point[point_id] += 1

    return max(area_by_point)


def solve2(points: List[Point]):

    safe_distance = 10000

    min_x = min(points, key=lambda p: p.x).x
    min_y = min(points, key=lambda p: p.y).y
    max_x = max(points, key=lambda p: p.x).x
    max_y = max(points, key=lambda p: p.y).y

    area_by_point = [0 for i in range(0, len(points))]
    safe_area = 0

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):

            distances = [(i, dist(points[i], Point(x, y))) for i in range(0, len(points))]

            total_distance = sum([x[1] for x in distances])

            if total_distance < safe_distance:
                safe_area += 1

    return safe_area


if __name__ == "__main__":
    input = get_input('D:\\repos\\adventofcode2018\\AOC06\\input.io')

    parsed_input = list(map(parse_line, input))

    result1 = solve1(parsed_input) #result1 => 3687
    print(f'The result is: {result1}')

    result2 = solve2(parsed_input) # result 2 => 40134
    print(f'The result is: {result2}')
