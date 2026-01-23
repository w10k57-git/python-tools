"""Temperature conversion functions.

Supports conversions between Celsius, Fahrenheit, and Kelvin.
"""


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit.

    Formula: °F = (°C × 9/5) + 32

    Args:
        celsius: Temperature in degrees Celsius

    Returns:
        Temperature in degrees Fahrenheit

    Examples:
        >>> celsius_to_fahrenheit(0)
        32.0
        >>> celsius_to_fahrenheit(100)
        212.0
    """
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius.

    Formula: °C = (°F - 32) × 5/9

    Args:
        fahrenheit: Temperature in degrees Fahrenheit

    Returns:
        Temperature in degrees Celsius

    Examples:
        >>> fahrenheit_to_celsius(32)
        0.0
        >>> fahrenheit_to_celsius(212)
        100.0
    """
    return (fahrenheit - 32) * 5 / 9


def celsius_to_kelvin(celsius: float) -> float:
    """Convert Celsius to Kelvin.

    Formula: K = °C + 273.15

    Args:
        celsius: Temperature in degrees Celsius

    Returns:
        Temperature in Kelvin

    Examples:
        >>> celsius_to_kelvin(0)
        273.15
        >>> celsius_to_kelvin(100)
        373.15
    """
    return celsius + 273.15


def kelvin_to_celsius(kelvin: float) -> float:
    """Convert Kelvin to Celsius.

    Formula: °C = K - 273.15

    Args:
        kelvin: Temperature in Kelvin

    Returns:
        Temperature in degrees Celsius

    Examples:
        >>> kelvin_to_celsius(273.15)
        0.0
        >>> kelvin_to_celsius(373.15)
        100.0
    """
    return kelvin - 273.15


def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    """Convert Fahrenheit to Kelvin.

    Args:
        fahrenheit: Temperature in degrees Fahrenheit

    Returns:
        Temperature in Kelvin
    """
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))


def kelvin_to_fahrenheit(kelvin: float) -> float:
    """Convert Kelvin to Fahrenheit.

    Args:
        kelvin: Temperature in Kelvin

    Returns:
        Temperature in degrees Fahrenheit
    """
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))
