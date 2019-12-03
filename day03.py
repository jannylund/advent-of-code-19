from timeit import default_timer as timer
from utils.time import get_time


def parse(wire):
    return wire.split(",")


# Generate coordinates from wire string.
def get_coords(wire, acc):
    if not wire:
        return acc

    direction = wire[0][0]
    distance = int(wire[0][1:])
    x, y = acc[-1]

    for d in range(1, distance+1):
        if direction == "R":
            acc.append((x+d, y))
        elif direction == "L":
            acc.append((x-d, y))
        elif direction == "U":
            acc.append((x, y+d))
        elif direction == "D":
            acc.append((x, y-d))

    return get_coords(wire[1:], acc)


# Find all the intersections (including 0,0)
def find_common(wire1, wire2):
    return list(set(wire1) & set(wire2))


# Find the intersection with closest distance from 0,0
def manhattan_distance(wire1, wire2):
    w1 = get_coords(parse(wire1), [(0, 0)])
    w2 = get_coords(parse(wire2), [(0, 0)])

    distance = None
    for x, y in find_common(w1[1:], w2[1:]): # ignore 0,0 in both
        d = abs(x) + abs(y)
        if distance is None or d < distance:
            distance = d
    return distance


# Find the intersection with shortest total steps
def least_steps(wire1, wire2):
    w1 = get_coords(parse(wire1), [(0, 0)])
    w2 = get_coords(parse(wire2), [(0, 0)])

    # Find the one closest to point zero.
    steps = None
    for intersection in find_common(w1[1:], w2[1:]): # ignore 0,0 in both
        s = w1.index(intersection) + w2.index(intersection)
        if steps is None or s < steps:
            steps = s

    return steps


if __name__ == "__main__":
    with open('input/day03.txt') as f:
        lines = f.read().splitlines()

    start = timer()
    print("result day 03 part 1: {} in {}".format(manhattan_distance(lines[0], lines[1]), get_time(start)))

    start = timer()
    print("result day 03 part 2: {} in {}".format(least_steps(lines[0], lines[1]), get_time(start)))
