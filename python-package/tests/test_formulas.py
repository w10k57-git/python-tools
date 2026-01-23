"""Tests for engineering formulas."""

import pytest
from engcalc.formulas.electrical import electrical_power, ohms_law
from engcalc.formulas.thermodynamics import (
    flow_rate,
    heat_capacity,
    ideal_gas_law,
    reynolds_number,
)


class TestOhmsLaw:
    """Test Ohm's Law calculations."""

    def test_calculate_resistance(self):
        assert ohms_law(voltage=12, current=3) == 4.0

    def test_calculate_current(self):
        assert ohms_law(voltage=12, resistance=4) == 3.0

    def test_calculate_voltage(self):
        assert ohms_law(current=3, resistance=4) == 12.0

    def test_requires_two_parameters(self):
        with pytest.raises(ValueError, match="exactly two"):
            ohms_law(voltage=12)

    def test_requires_only_two_parameters(self):
        with pytest.raises(ValueError, match="exactly two"):
            ohms_law(voltage=12, current=3, resistance=4)


class TestElectricalPower:
    """Test electrical power calculations."""

    def test_calculate_power(self):
        assert electrical_power(voltage=12, current=2) == 24.0

    def test_calculate_voltage(self):
        assert electrical_power(power=24, current=2) == 12.0

    def test_calculate_current(self):
        assert electrical_power(power=24, voltage=12) == 2.0


class TestIdealGasLaw:
    """Test Ideal Gas Law calculations."""

    def test_calculate_temperature(self):
        # Standard conditions: 1 mole at 1 atm, 22.4L
        result = ideal_gas_law(pressure=101325, volume=0.0224, moles=1, R=8.314)
        assert abs(result - 273.15) < 0.5

    def test_requires_three_parameters(self):
        with pytest.raises(ValueError, match="exactly three"):
            ideal_gas_law(pressure=101325, volume=0.0224)


class TestHeatCapacity:
    """Test heat capacity calculations."""

    def test_water_heating(self):
        # Heat 1kg of water by 10°C
        result = heat_capacity(1.0, 4186, 10)
        assert result == 41860.0


class TestReynoldsNumber:
    """Test Reynolds number calculation."""

    def test_reynolds_number(self):
        result = reynolds_number(
            density=1000, velocity=2, diameter=0.1, viscosity=0.001
        )
        assert result == 200000.0


class TestFlowRate:
    """Test flow rate calculation."""

    def test_flow_rate(self):
        assert flow_rate(velocity=2.0, area=0.5) == 1.0
