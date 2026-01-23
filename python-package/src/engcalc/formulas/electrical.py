"""Electrical engineering formulas."""

from typing import Optional


def ohms_law(
    voltage: Optional[float] = None,
    current: Optional[float] = None,
    resistance: Optional[float] = None,
) -> float:
    """Calculate unknown value using Ohm's Law: V = I × R

    Provide any two of the three parameters to calculate the third.

    Formula: V = I × R
    Where:
        V = Voltage (Volts)
        I = Current (Amperes)
        R = Resistance (Ohms)

    Args:
        voltage: Voltage in Volts (optional)
        current: Current in Amperes (optional)
        resistance: Resistance in Ohms (optional)

    Returns:
        The calculated value (voltage, current, or resistance)

    Raises:
        ValueError: If not exactly two parameters are provided

    Examples:
        >>> ohms_law(voltage=12, current=3)  # Calculate resistance
        4.0
        >>> ohms_law(voltage=12, resistance=4)  # Calculate current
        3.0
        >>> ohms_law(current=3, resistance=4)  # Calculate voltage
        12.0
    """
    provided = sum(x is not None for x in [voltage, current, resistance])

    if provided != 2:
        raise ValueError("Must provide exactly two of three parameters")

    if voltage is None:
        return current * resistance  # type: ignore
    elif current is None:
        return voltage / resistance  # type: ignore
    else:  # resistance is None
        return voltage / current  # type: ignore


def electrical_power(
    voltage: Optional[float] = None,
    current: Optional[float] = None,
    power: Optional[float] = None,
) -> float:
    """Calculate unknown value using Power formula: P = V × I

    Provide any two of the three parameters to calculate the third.

    Formula: P = V × I
    Where:
        P = Power (Watts)
        V = Voltage (Volts)
        I = Current (Amperes)

    Args:
        voltage: Voltage in Volts (optional)
        current: Current in Amperes (optional)
        power: Power in Watts (optional)

    Returns:
        The calculated value (power, voltage, or current)

    Raises:
        ValueError: If not exactly two parameters are provided

    Examples:
        >>> electrical_power(voltage=12, current=2)  # Calculate power
        24.0
        >>> electrical_power(power=24, current=2)  # Calculate voltage
        12.0
        >>> electrical_power(power=24, voltage=12)  # Calculate current
        2.0
    """
    provided = sum(x is not None for x in [voltage, current, power])

    if provided != 2:
        raise ValueError("Must provide exactly two of three parameters")

    if power is None:
        return voltage * current  # type: ignore
    elif voltage is None:
        return power / current  # type: ignore
    else:  # current is None
        return power / voltage  # type: ignore


def resistance_from_resistivity(
    resistivity: float, length: float, area: float
) -> float:
    """Calculate resistance from material properties.

    Formula: R = ρL/A
    Where:
        R = Resistance (Ohms)
        ρ = Resistivity (Ohm·meters)
        L = Length (meters)
        A = Cross-sectional area (square meters)

    Args:
        resistivity: Resistivity in Ohm·meters
        length: Length in meters
        area: Cross-sectional area in square meters

    Returns:
        Resistance in Ohms

    Examples:
        >>> round(resistance_from_resistivity(1.68e-8, 100, 1e-6), 2)
        1.68
    """
    return resistivity * length / area
