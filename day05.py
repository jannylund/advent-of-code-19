from collections import Counter
from timeit import default_timer as timer
from utils.time import get_time
from lib.intcode import *


if __name__ == "__main__":
    with open('input/day05.txt') as f:
        program = [int(c) for c in f.readline().strip().split(",")]

    start = timer()
    result = compute_output(program, 1)
    size = len(result)

    # Validate all tests returned zero.
    zeroes = Counter(result).get(0)
    if zeroes < size - 1:
        print("ERROR: Not all tests returned zero.")

    print("result day 05 part 1: {} in {}".format(max(Counter(result).keys()), get_time(start)))

    start = timer()
    result = compute_output(program, 5)
    size = len(result)
    print("result day 05 part 2: {} in {}".format(max(Counter(result).keys()), get_time(start)))
