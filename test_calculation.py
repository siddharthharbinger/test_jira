from calculation import calculate_ratio


def test_calculate_ratio_positive():
    assert calculate_ratio(10.0, 2.0) == 5.0


def test_calculate_ratio_zero_divisor():
    assert calculate_ratio(10.0, 0.0) == 0.0
