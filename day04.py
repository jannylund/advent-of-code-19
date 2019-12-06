from collections import Counter
from timeit import default_timer as timer

from utils.time import get_time


# Check that we are not decreasing.
def check_increasing(digit):
    last = None
    for i in str(digit):
        if last is not None and i < last:
            return False
        last = i
    return True


# Check that max 2 adjacent are the same.
def check_adjacent(digit):
    return max(Counter(str(digit)).values()) >= 2


# Check that at least 2 adjacent are the same.
def check_pairs(digit):
    return 2 in Counter(str(digit)).values()


def is_valid_password(digit):
    return check_increasing(digit) and check_adjacent(digit)


def is_valid_password2(digit):
    return check_increasing(digit) and check_pairs(digit)


if __name__ == "__main__":
    with open('input/day04.txt') as f:
        d_min, d_max = f.readline().split("-")

    start = timer()
    valid_passwords = []
    for d in range(int(d_min), int(d_max)+1):
        if is_valid_password(d):
            valid_passwords.append(d)

    print("result day 04 part 1: {} in {}".format(len(valid_passwords), get_time(start)))

    start = timer()
    valid_passwords = []
    for d in range(int(d_min), int(d_max)+1):
        if is_valid_password2(d):
            valid_passwords.append(d)

    print("result day 04 part 2: {} in {}".format(len(valid_passwords), get_time(start)))
