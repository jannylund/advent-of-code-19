from timeit import default_timer as timer

from utils.time import get_time


def get_parent_tree(m):
    t = dict()
    for o in m:
        p, c = o.split(")")
        t[c] = p
    return t


def get_parent(t, o):
    if o in t:
        return t[o]
    return None


def get_parents(t, o):
    result = []
    while True:
        p = get_parent(t, o)
        if p is None:
            return result
        else:
            result.append(p)
        o = p
    return result


def calc_orbits(t):
    orbits = 0
    for o in t.keys():
        orbits += len(get_parents(t, o))
    return orbits


def get_moves(t, o1, o2):
    y = set(get_parents(t, o1))
    s = set(get_parents(t, o2))
    return len(y.union(s) - y.intersection(s))


if __name__ == "__main__":
    with open('input/day06.txt') as f:
        m = f.read().splitlines()
    t = get_parent_tree(m)
    start = timer()
    print("result day 06 part 1: {} in {}".format(calc_orbits(t), get_time(start)))

    start = timer()
    print("result day 06 part 2: {} in {}".format(get_moves(t, "YOU", "SAN"), get_time(start)))
