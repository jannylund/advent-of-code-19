from timeit import default_timer as timer
from utils.time import get_time


def calc_fuel(mass):
    return max(mass // 3 - 2, 0)


def calc_fuel_recursive(mass):
    fuel = calc_fuel(mass)
    if fuel > 0:
        return fuel + calc_fuel_recursive(fuel)
    return fuel


if __name__ == "__main__":
    with open('input/day01.txt') as f:
        modules = [int(m) for m in f.read().splitlines()]

    start = timer()
    module_fuel = [calc_fuel(m) for m in modules]
    print("result day 01 part 1: {} in {}".format(sum(module_fuel), get_time(start)))

    start = timer()
    module_fuel_recursive = [calc_fuel_recursive(m) for m in modules]
    print("result day 01 part 2: {} in {}".format(sum(module_fuel_recursive), get_time(start)))
