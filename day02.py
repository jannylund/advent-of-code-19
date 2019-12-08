from timeit import default_timer as timer
from utils.time import get_time

# This could use the common intcode implementation but it's slower because of the parameter check. :/
def intcode(code, pos=0):
    opcode = code[pos]
    if opcode == 99:
        return code

    in1 = code[pos+1]
    in2 = code[pos+2]
    out = code[pos+3]
    if opcode == 1:
        code[out] = code[in1] + code[in2]
    elif opcode == 2:
        code[out] = code[in1] * code[in2]

    return intcode(code, pos+4)


def compute(program, noun, verb):
    program[1] = noun
    program[2] = verb
    return intcode(program.copy())[0]


if __name__ == "__main__":
    with open('input/day02.txt') as f:
        program = [int(c) for c in f.readline().strip().split(",")]

    start = timer()
    print("result day 02 part 1: {} in {}".format(compute(program, 12, 2), get_time(start)))

    start = timer()
    output = 19690720  # desired output.
    for noun in range(0, 100):
        for verb in range(0, 100):
            if compute(program, noun, verb) == output:
                print("result day 02 part 2: {} in {}".format(100 * noun + verb, get_time(start)))
