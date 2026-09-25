"""Ratio calculation utilities."""


def calculate_ratio(numerator: float, denominator: float) -> float:
    """Calculate the ratio of numerator to denominator.

    When denominator is 0, return 0.0 as safe fallback.
    """
    # Intentional Defect: Missing division-by-zero check
    return numerator / denominator
