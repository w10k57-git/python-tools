"""Tests for temperature conversion functions."""

from engcalc.conversions.temperature import (
    celsius_to_fahrenheit,
    celsius_to_kelvin,
    fahrenheit_to_celsius,
    fahrenheit_to_kelvin,
    kelvin_to_celsius,
    kelvin_to_fahrenheit,
)


class TestCelsiusFahrenheit:
    """Test Celsius-Fahrenheit conversions."""

    def test_celsius_to_fahrenheit_freezing(self):
        assert celsius_to_fahrenheit(0) == 32.0

    def test_celsius_to_fahrenheit_boiling(self):
        assert celsius_to_fahrenheit(100) == 212.0

    def test_fahrenheit_to_celsius_freezing(self):
        assert fahrenheit_to_celsius(32) == 0.0

    def test_fahrenheit_to_celsius_boiling(self):
        assert fahrenheit_to_celsius(212) == 100.0

    def test_celsius_to_fahrenheit_negative(self):
        assert celsius_to_fahrenheit(-40) == -40.0


class TestCelsiusKelvin:
    """Test Celsius-Kelvin conversions."""

    def test_celsius_to_kelvin_freezing(self):
        assert celsius_to_kelvin(0) == 273.15

    def test_celsius_to_kelvin_boiling(self):
        assert celsius_to_kelvin(100) == 373.15

    def test_kelvin_to_celsius_freezing(self):
        assert kelvin_to_celsius(273.15) == 0.0

    def test_kelvin_to_celsius_boiling(self):
        assert kelvin_to_celsius(373.15) == 100.0


class TestFahrenheitKelvin:
    """Test Fahrenheit-Kelvin conversions."""

    def test_fahrenheit_to_kelvin(self):
        result = fahrenheit_to_kelvin(32)
        assert abs(result - 273.15) < 0.01

    def test_kelvin_to_fahrenheit(self):
        result = kelvin_to_fahrenheit(273.15)
        assert abs(result - 32.0) < 0.01


class TestRoundTrip:
    """Test round-trip conversions."""

    def test_celsius_fahrenheit_round_trip(self):
        original = 25.0
        result = fahrenheit_to_celsius(celsius_to_fahrenheit(original))
        assert abs(result - original) < 0.0001

    def test_celsius_kelvin_round_trip(self):
        original = 25.0
        result = kelvin_to_celsius(celsius_to_kelvin(original))
        assert abs(result - original) < 0.0001
