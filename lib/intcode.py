from functools import lru_cache

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


@lru_cache(maxsize=None)
def split_instruction(instruction):
    opcode = instruction % 10
    mode_p1 = int(instruction / 100) % 10
    mode_p2 = int(instruction / 1000) % 10
    return opcode, mode_p1, mode_p2


def intcode(code, pos=None, input=1, output=None):
    if pos is None or output is None:
        pos = 0
        output = []

    if code[pos] == 99:
        return (code, output)
    opcode, mode_p1, mode_p2 = split_instruction(code[pos])

    if opcode is OPCODE_ADD:
        step = 4
        p1 = get_value(pos+1, code, mode_p1)
        p2 = get_value(pos+2, code, mode_p2)
        out = code[pos+3]
        code[out] = p1 + p2

    elif opcode is OPCODE_MULTIPLY:
        step = 4
        p1 = get_value(pos+1, code, mode_p1)
        p2 = get_value(pos+2, code, mode_p2)
        out = code[pos+3]
        code[out] = p1 * p2

    elif opcode is OPCODE_SAVE_INPUT:
        step = 2
        out = code[pos+1]
        code[out] = input

    elif opcode is OPCODE_PRINT_OUTPUT:
        step = 2
        p1 = get_value(pos+1, code, mode_p1)
        output.append(p1)

    elif opcode is OPCODE_JUMP_IF_TRUE:
        step = 3
        p1 = get_value(pos+1, code, mode_p1)
        p2 = get_value(pos+2, code, mode_p2)
        if p1 != 0:
            step = 0
            pos = p2

    elif opcode is OPCODE_JUMP_IF_FALSE:
        step = 3
        p1 = get_value(pos+1, code, mode_p1)
        p2 = get_value(pos+2, code, mode_p2)
        if p1 == 0:
            step = 0
            pos = p2

    elif opcode is OPCODE_LESS_THAN:
        step = 4
        p1 = get_value(pos+1, code, mode_p1)
        p2 = get_value(pos+2, code, mode_p2)
        out = code[pos+3]
        code[out] = int(p1 < p2)

    elif opcode is OPCODE_EQUALS:
        step = 4
        p1 = get_value(pos+1, code, mode_p1)
        p2 = get_value(pos+2, code, mode_p2)
        out = code[pos+3]
        code[out] = int(p1 == p2)

    return intcode(code, pos+step, input, output)


def compute_output(program, i):
    return intcode(code=program.copy(), input=i)[1]
