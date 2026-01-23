"""Pressure conversion functions.

Supports conversions between PSI, Bar, Pascal, and kPa.
"""


def psi_to_bar(psi: float) -> float:
    """Convert PSI (pounds per square inch) to Bar.

    Formula: bar = psi × 0.0689476

    Args:
        psi: Pressure in PSI

    Returns:
        Pressure in Bar

    Examples:
        >>> round(psi_to_bar(14.7), 4)
        1.0135
    """
    return psi * 0.0689476


def bar_to_psi(bar: float) -> float:
    """Convert Bar to PSI.

    Formula: psi = bar / 0.0689476

    Args:
        bar: Pressure in Bar

    Returns:
        Pressure in PSI

    Examples:
        >>> round(bar_to_psi(1.0), 2)
        14.5
    """
    return bar / 0.0689476


def bar_to_pascal(bar: float) -> float:
    """Convert Bar to Pascal.

    Formula: Pa = bar × 100000

    Args:
        bar: Pressure in Bar

    Returns:
        Pressure in Pascal

    Examples:
        >>> bar_to_pascal(1.0)
        100000.0
    """
    return bar * 100000


def pascal_to_bar(pascal: float) -> float:
    """Convert Pascal to Bar.

    Formula: bar = Pa / 100000

    Args:
        pascal: Pressure in Pascal

    Returns:
        Pressure in Bar

    Examples:
        >>> pascal_to_bar(100000)
        1.0
    """
    return pascal / 100000


def pascal_to_kpa(pascal: float) -> float:
    """Convert Pascal to kilopascal.

    Formula: kPa = Pa / 1000

    Args:
        pascal: Pressure in Pascal

    Returns:
        Pressure in kPa

    Examples:
        >>> pascal_to_kpa(1000)
        1.0
    """
    return pascal / 1000


def kpa_to_pascal(kpa: float) -> float:
    """Convert kilopascal to Pascal.

    Formula: Pa = kPa × 1000

    Args:
        kpa: Pressure in kPa

    Returns:
        Pressure in Pascal

    Examples:
        >>> kpa_to_pascal(1.0)
        1000.0
    """
    return kpa * 1000


def psi_to_pascal(psi: float) -> float:
    """Convert PSI to Pascal.

    Args:
        psi: Pressure in PSI

    Returns:
        Pressure in Pascal
    """
    return bar_to_pascal(psi_to_bar(psi))


def pascal_to_psi(pascal: float) -> float:
    """Convert Pascal to PSI.

    Args:
        pascal: Pressure in Pascal

    Returns:
        Pressure in PSI
    """
    return bar_to_psi(pascal_to_bar(pascal))
