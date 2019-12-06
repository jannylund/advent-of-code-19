from collections import Counter
from timeit import default_timer as timer
from utils.time import get_time

OPCODE_ADD = 1
OPCODE_MULTIPLY = 2
OPCODE_SAVE_INPUT = 3
OPCODE_PRINT_OUTPUT = 4
OPCODE_JUMP_IF_TRUE = 5
OPCODE_JUMP_IF_FALSE = 6
OPCODE_LESS_THAN = 7
OPCODE_EQUALS = 8


def get_value(pos, code, mode):
    if mode == 0:
        return code[code[pos]]
    else:
        return code[pos]


def split_instruction(instruction):
    opcode = instruction % 10
    mode_p1 = int(instruction / 100) % 10
    mode_p2 = int(instruction / 1000) % 10
    return opcode, mode_p1, mode_p2


def intcode(code, input=1, pos=None, output=None):
    if pos is None:
        pos = 0
    if output is None:
        output = []

    instruction = code[pos]
    if instruction == 99:
        return (code, output)
    opcode, mode_p1, mode_p2 = split_instruction(instruction)

    if opcode is OPCODE_ADD or opcode is OPCODE_MULTIPLY:
        step = 4
        p1 = get_value(pos+1, code, mode_p1)
        p2 = get_value(pos+2, code, mode_p2)
        out = code[pos+3]
        if opcode is OPCODE_ADD:
            code[out] = p1 + p2
        else:
            code[out] = p1 * p2

    elif opcode is OPCODE_SAVE_INPUT:
        step = 2
        out = code[pos+1]
        code[out] = input

    elif opcode is OPCODE_PRINT_OUTPUT:
        step = 2
        p1 = get_value(pos+1, code, mode_p1)
        output.append(p1)

    # Jump if true (non-zero)
    elif opcode is OPCODE_JUMP_IF_TRUE or opcode is OPCODE_JUMP_IF_FALSE:
        p1 = get_value(pos+1, code, mode_p1)
        p2 = get_value(pos+2, code, mode_p2)
        step = 3
        if (opcode == OPCODE_JUMP_IF_TRUE and p1 != 0) or (opcode == OPCODE_JUMP_IF_FALSE and p1 == 0):
            pos = p2
            step = 0

    elif opcode is OPCODE_LESS_THAN or opcode is OPCODE_EQUALS:
        step = 4
        p1 = get_value(pos+1, code, mode_p1)
        p2 = get_value(pos+2, code, mode_p2)
        out = code[pos+3]

        if opcode is OPCODE_LESS_THAN:
            code[out] = int(p1 < p2)

        else:
            code[out] = int(p1 == p2)

    return intcode(code, input, pos+step, output)


if __name__ == "__main__":
    with open('input/day05.txt') as f:
        program = [int(c) for c in f.readline().strip().split(",")]

    start = timer()
    result = intcode(program.copy(), 1)[1]
    size = len(result)
    zeroes = Counter(result).get(0)

    if zeroes < size - 1:
        print("ERROR: Not all tests returned zero.")

    print("result day 05 part 1: {} in {}".format(max(Counter(result).keys()), get_time(start)))

    start = timer()
    result = intcode(program.copy(), 5)[1]
    size = len(result)
    print("result day 05 part 2: {} in {}".format(max(Counter(result).keys()), get_time(start)))
