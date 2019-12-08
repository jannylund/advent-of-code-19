import itertools
from timeit import default_timer as timer

from lib.intcode import *
from utils.time import get_time


def compute_thruster(program, phase):
    output = 0
    for i in range(len(phase)):
        result = compute_output(program, [phase[i], output])
        output = result[0]
    return output


def compute_max_thruster(program):
    max_output = 0
    max_phase = []

    for phase in itertools.permutations(range(5), 5):
        _output = 0
        for i in range(len(phase)):
            result = compute_output(program, [phase[i], _output])
            _output = result[0]
        if _output > max_output:
            max_output = _output
            max_phase = phase
    return (phase, max_output)


if __name__ == "__main__":
    with open('input/day07.txt') as f:
        program = [int(c) for c in f.readline().strip().split(",")]

    start = timer()
    print("result day 07 part 1: {} in {}".format(
        compute_max_thruster(program), get_time(start)))
