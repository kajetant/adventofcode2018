import re
from itertools import count, groupby
from functools import reduce
from datetime import datetime
import operator

def get_input(filename):
    with open(filename) as f:
        return [x.strip() for x in f.readlines()]


def parse_line(line):
    r = re.compile('\[(?P<timestamp>(.*))\]\s(Guard\s\#(?P<guard>(\d+))\s)*(?P<action>(begins\sshift|wakes\sup|falls\sasleep))')
    d = r.match(line).groupdict()

    timestamp = datetime.strptime(d['timestamp'], '%Y-%m-%d %H:%M')
    guard_id = int(d['guard']) if d['guard'] is not None else None
    action = d['action']

    return Action(timestamp, guard_id, action)


class Action(object):
    def __init__(self, timestamp, guard_id, action):
        self.timestamp = timestamp
        self.guard_id = guard_id
        self.action = action


def solve1(input):

    sleep_map = {}
    active_guard = 0

    for i in range(0, len(input)-1):
        if input[i].action == 'begins shift': active_guard = input[i].guard_id
        elif input[i].action == 'falls asleep': pass
        elif input[i].action == 'wakes up':

            start = input[i-1].timestamp.minute
            stop = input[i].timestamp.minute
            sleep_time = stop - start

            if not active_guard in sleep_map.keys():
                sleep_map[active_guard] = [0 for j in range(0, 59)]

            for m in range(start, stop):
                sleep_map[active_guard][m] += 1

    new_map = dict([(guard_id, sum(minutes_asleep)) for guard_id, minutes_asleep in sleep_map.items()])

    most_asleep_guard = max(new_map.items(), key=operator.itemgetter(1))[0]

    most_asleep_minute = sleep_map[most_asleep_guard].index(max(sleep_map[most_asleep_guard]))

    return most_asleep_guard * most_asleep_minute


def solve2(input):
    pass

if __name__ == "__main__":

    input = """[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up""".split('\n')

    input = get_input('D:\\repos\\adventofcode2018\\AOC04\\input.io')

    parsed_input = sorted((map(parse_line, input)), key=lambda x: x.timestamp)

    result1 = solve1(parsed_input) #result1 => 65489
    print(f'The result is: {result1}')

    result2 = solve2(parsed_input) # result 2 =>
    print(f'The result is: {result2}')
