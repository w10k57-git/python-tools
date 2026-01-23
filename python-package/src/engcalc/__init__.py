"""Engineering calculations library for unit conversions and formulas.

This package provides:
- Unit conversions (temperature, pressure, length)
- Electrical formulas (Ohm's Law, Power)
- Thermodynamics formulas (Ideal Gas Law, Heat Capacity, Reynolds Number)
- Physical constants

Examples:
    >>> from engcalc.conversions import celsius_to_fahrenheit
    >>> celsius_to_fahrenheit(100)
    212.0

    >>> from engcalc.formulas import ohms_law
    >>> ohms_law(voltage=12, resistance=4)  # Calculate current
    3.0

    >>> from engcalc.constants import GRAVITY
    >>> GRAVITY
    9.80665
"""

from engcalc import conversions, formulas, constants

__version__ = "0.1.0"

__all__ = ["conversions", "formulas", "constants"]
