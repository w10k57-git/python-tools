"""Length conversion functions.

Supports conversions between meters, feet, and inches.
"""


def meters_to_feet(meters: float) -> float:
    """Convert meters to feet.

    Formula: ft = m × 3.28084

    Args:
        meters: Length in meters

    Returns:
        Length in feet

    Examples:
        >>> round(meters_to_feet(1.0), 2)
        3.28
        >>> round(meters_to_feet(10.0), 2)
        32.81
    """
    return meters * 3.28084


def feet_to_meters(feet: float) -> float:
    """Convert feet to meters.

    Formula: m = ft / 3.28084

    Args:
        feet: Length in feet

    Returns:
        Length in meters

    Examples:
        >>> round(feet_to_meters(3.28084), 2)
        1.0
    """
    return feet / 3.28084


def inches_to_meters(inches: float) -> float:
    """Convert inches to meters.

    Formula: m = in × 0.0254

    Args:
        inches: Length in inches

    Returns:
        Length in meters

    Examples:
        >>> inches_to_meters(39.37)
        0.999998
    """
    return inches * 0.0254


def meters_to_inches(meters: float) -> float:
    """Convert meters to inches.

    Formula: in = m / 0.0254

    Args:
        meters: Length in meters

    Returns:
        Length in inches

    Examples:
        >>> round(meters_to_inches(1.0), 2)
        39.37
    """
    return meters / 0.0254


def feet_to_inches(feet: float) -> float:
    """Convert feet to inches.

    Formula: in = ft × 12

    Args:
        feet: Length in feet

    Returns:
        Length in inches

    Examples:
        >>> feet_to_inches(1.0)
        12.0
        >>> feet_to_inches(5.5)
        66.0
    """
    return feet * 12


def inches_to_feet(inches: float) -> float:
    """Convert inches to feet.

    Formula: ft = in / 12

    Args:
        inches: Length in inches

    Returns:
        Length in feet

    Examples:
        >>> inches_to_feet(12.0)
        1.0
        >>> inches_to_feet(66.0)
        5.5
    """
    return inches / 12
