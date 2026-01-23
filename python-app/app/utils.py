"""Utility functions for the application."""


def pascals_to_mpa(pascals: float) -> float:
    """
    Convert Pascals to Megapascals.

    Args:
        pascals: Pressure in Pascals

    Returns:
        Pressure in MPa
    """
    return pascals / 1e6


def mpa_to_pascals(mpa: float) -> float:
    """
    Convert Megapascals to Pascals.

    Args:
        mpa: Pressure in MPa

    Returns:
        Pressure in Pascals
    """
    return mpa * 1e6


def meters_to_mm(meters: float) -> float:
    """
    Convert meters to millimeters.

    Args:
        meters: Length in meters

    Returns:
        Length in millimeters
    """
    return meters * 1000


def mm_to_meters(mm: float) -> float:
    """
    Convert millimeters to meters.

    Args:
        mm: Length in millimeters

    Returns:
        Length in meters
    """
    return mm / 1000


def watts_to_hp(watts: float) -> float:
    """
    Convert Watts to horsepower.

    Args:
        watts: Power in Watts

    Returns:
        Power in horsepower
    """
    return watts / 745.7


def hp_to_watts(hp: float) -> float:
    """
    Convert horsepower to Watts.

    Args:
        hp: Power in horsepower

    Returns:
        Power in Watts
    """
    return hp * 745.7
