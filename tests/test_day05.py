from day05 import *


def test_day05_part1():
    assert intcode([1, 0, 0, 0, 99]) == ([2, 0, 0, 0, 99], [])
    assert intcode([2, 3, 0, 3, 99]) == ([2, 3, 0, 6, 99], [])
    assert intcode([2, 4, 4, 5, 99, 0]) == ([2, 4, 4, 5, 99, 9801], [])
    assert intcode([1, 1, 1, 4, 99, 5, 6, 0, 99]) == (
        [30, 1, 1, 4, 2, 5, 6, 0, 99], [])
    assert intcode([3, 0, 99]) == ([1, 0, 99], [])
    assert intcode([3, 0, 4, 0, 99]) == ([1, 0, 4, 0, 99], [1])

    assert intcode([1002, 4, 3, 4, 33])[0] == [1002, 4, 3, 4, 99]


def test_day05_part2():
    # position mode test if equal to 8.
    assert intcode([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], 1)[1] == [0]
    assert intcode([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], 8)[1] == [1]
    assert intcode([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], 9)[1] == [0]

    # position mode test if less than 8
    assert intcode([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], 1)[1] == [1]
    assert intcode([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], 7)[1] == [1]
    assert intcode([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], 8)[1] == [0]
    assert intcode([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], 9)[1] == [0]

    # immediate mode test if equal to 8.
    assert intcode([3, 3, 1108, -1, 8, 3, 4, 3, 99], 1)[1] == [0]
    assert intcode([3, 3, 1108, -1, 8, 3, 4, 3, 99], 8)[1] == [1]
    assert intcode([3, 3, 1108, -1, 8, 3, 4, 3, 99], 9)[1] == [0]

    # immediate mode test if less than 8
    assert intcode([3, 3, 1107, -1, 8, 3, 4, 3, 99], 1)[1] == [1]
    assert intcode([3, 3, 1107, -1, 8, 3, 4, 3, 99], 7)[1] == [1]
    assert intcode([3, 3, 1107, -1, 8, 3, 4, 3, 99], 8)[1] == [0]
    assert intcode([3, 3, 1107, -1, 8, 3, 4, 3, 99], 9)[1] == [0]


    # jump tests.
    assert intcode([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], 0)[1] == [0]
    assert intcode([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], 1)[1] == [1]
    assert intcode([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], 2)[1] == [1]

    assert intcode([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], 0)[1] == [0]
    assert intcode([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], 1)[1] == [1]
    assert intcode([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], 2)[1] == [1]


