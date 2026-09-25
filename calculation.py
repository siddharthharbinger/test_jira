"""Ratio calculation utilities."""


def calculate_ratio(numerator: float, denominator: float) -> float:
    """Calculate the ratio of numerator to denominator.

    """
    if denominator == 0:
        return 0.0
    return numerator / denominator
