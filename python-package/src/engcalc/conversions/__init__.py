"""Unit conversion functions for engineering calculations."""

from engcalc.conversions.temperature import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    celsius_to_kelvin,
    kelvin_to_celsius,
    fahrenheit_to_kelvin,
    kelvin_to_fahrenheit,
)
from engcalc.conversions.pressure import (
    psi_to_bar,
    bar_to_psi,
    bar_to_pascal,
    pascal_to_bar,
    pascal_to_kpa,
    kpa_to_pascal,
    psi_to_pascal,
    pascal_to_psi,
)
from engcalc.conversions.length import (
    meters_to_feet,
    feet_to_meters,
    inches_to_meters,
    meters_to_inches,
    feet_to_inches,
    inches_to_feet,
)

__all__ = [
    # Temperature
    "celsius_to_fahrenheit",
    "fahrenheit_to_celsius",
    "celsius_to_kelvin",
    "kelvin_to_celsius",
    "fahrenheit_to_kelvin",
    "kelvin_to_fahrenheit",
    # Pressure
    "psi_to_bar",
    "bar_to_psi",
    "bar_to_pascal",
    "pascal_to_bar",
    "pascal_to_kpa",
    "kpa_to_pascal",
    "psi_to_pascal",
    "pascal_to_psi",
    # Length
    "meters_to_feet",
    "feet_to_meters",
    "inches_to_meters",
    "meters_to_inches",
    "feet_to_inches",
    "inches_to_feet",
]
