"""Tests for pressure conversion functions."""

from engcalc.conversions.pressure import (
    bar_to_pascal,
    bar_to_psi,
    kpa_to_pascal,
    pascal_to_bar,
    pascal_to_kpa,
    psi_to_bar,
)


class TestPSIBar:
    """Test PSI-Bar conversions."""

    def test_psi_to_bar(self):
        result = psi_to_bar(14.7)
        assert abs(result - 1.0135) < 0.001

    def test_bar_to_psi(self):
        result = bar_to_psi(1.0)
        assert abs(result - 14.5) < 0.1


class TestBarPascal:
    """Test Bar-Pascal conversions."""

    def test_bar_to_pascal(self):
        assert bar_to_pascal(1.0) == 100000.0

    def test_pascal_to_bar(self):
        assert pascal_to_bar(100000) == 1.0


class TestPascalKPA:
    """Test Pascal-kPa conversions."""

    def test_pascal_to_kpa(self):
        assert pascal_to_kpa(1000) == 1.0

    def test_kpa_to_pascal(self):
        assert kpa_to_pascal(1.0) == 1000.0


class TestRoundTrip:
    """Test round-trip conversions."""

    def test_psi_bar_round_trip(self):
        original = 14.7
        result = bar_to_psi(psi_to_bar(original))
        assert abs(result - original) < 0.0001
