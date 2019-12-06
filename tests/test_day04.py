from day04 import *


def test_day04_part1():
    assert check_adjacent("1234567") == False
    assert check_adjacent("1234577") == True

    assert check_increasing("1234577") == True
    assert check_increasing("321") == False
    assert check_increasing("1111") == True

    assert is_valid_password("111111") == True
    assert is_valid_password("223450") == False
    assert is_valid_password("123789") == False

def test_day04_part2():
    assert check_pairs("1111") == False
    assert check_pairs("11223344") == True

    assert is_valid_password2("112233") == True
    assert is_valid_password2("123444") == False
    assert is_valid_password2("111122") == True
