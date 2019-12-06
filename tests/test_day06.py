from day06 import *


def test_day06_part1():
    m = "COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L".split("\n")
    t = get_parent_tree(m)

    assert get_parent(t, "B") == "COM"
    assert get_parent(t, "COM") == None
    assert get_parent(t, "F") == "E"

    assert get_parents(t, "COM") == []
    assert get_parents(t, "B") == ["COM"]
    assert get_parents(t, "H") == ["G", "B", "COM"]

    assert calc_orbits(t) == 42


def test_day06_part2():
    m = "COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L\nK)YOU\nI)SAN".split("\n")
    t = get_parent_tree(m)
    assert get_moves(t, "YOU", "SAN") == 4
