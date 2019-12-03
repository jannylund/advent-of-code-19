from day03 import manhattan_distance, get_coords, parse, find_common, least_steps


def test_day03_part1():
    assert parse("R2") == ['R2']
    assert parse("R2,U2") == ['R2', 'U2']

    assert get_coords(parse("R2"), [(0, 0)]) == [(0, 0), (1, 0), (2, 0)]
    assert get_coords(parse("R2,U2"), [(0, 0)]) == [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]

    assert find_common([(0, 0), (0, 1), (0, 2)], [(0, 0), (1, 1), (0, 2)]) == [(0, 0), (0, 2)]

    assert manhattan_distance("R8,U5,L5,D3", "U7,R6,D4,L4") == 6

    assert manhattan_distance("R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83") == 159
    assert manhattan_distance("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7") == 135


def test_day03_part2():
    assert least_steps("R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83") == 610
    assert least_steps("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7") == 410
