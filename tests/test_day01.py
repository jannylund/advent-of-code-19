from day01 import calc_fuel, calc_fuel_recursive

def test_day01_part1():
    assert calc_fuel(12) == 2
    assert calc_fuel(14) == 2
    assert calc_fuel(1969) == 654
    assert calc_fuel(100756) == 33583

def test_day01_part2():
    assert calc_fuel_recursive(12) == 2
    assert calc_fuel_recursive(1969) == 966
    assert calc_fuel_recursive(100756) == 50346
