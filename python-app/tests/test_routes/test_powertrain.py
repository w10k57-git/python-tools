"""Tests for powertrain calculation endpoints."""

import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app


class TestPowertrainCalculations:
    """Test powertrain calculation endpoints."""

    @pytest.mark.asyncio
    async def test_gear_ratio_calculation(self):
        """Test gear ratio endpoint."""
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
        ) as client:
            response = await client.post(
                "/api/v1/powertrain/gear-ratio",
                json={"driver_teeth": 20, "driven_teeth": 60},
            )
        assert response.status_code == 200
        data = response.json()
        assert data["gear_ratio"] == 3.0
        assert data["speed_reduction"] == pytest.approx(0.333, rel=0.01)

    @pytest.mark.asyncio
    async def test_gear_ratio_invalid_input(self):
        """Test gear ratio with invalid input."""
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
        ) as client:
            response = await client.post(
                "/api/v1/powertrain/gear-ratio",
                json={"driver_teeth": -10, "driven_teeth": 60},
            )
        assert response.status_code == 422

    @pytest.mark.asyncio
    async def test_torque_calculation(self):
        """Test torque output calculation."""
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
        ) as client:
            response = await client.post(
                "/api/v1/powertrain/torque",
                json={"input_torque": 100, "gear_ratio": 3.0, "efficiency": 0.95},
            )
        assert response.status_code == 200
        data = response.json()
        assert data["output_torque"] == pytest.approx(285.0, rel=0.01)

    @pytest.mark.asyncio
    async def test_torque_default_efficiency(self):
        """Test torque calculation with default efficiency."""
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
        ) as client:
            response = await client.post(
                "/api/v1/powertrain/torque",
                json={"input_torque": 100, "gear_ratio": 2.0},
            )
        assert response.status_code == 200
        data = response.json()
        assert data["efficiency"] == 0.95
        assert data["output_torque"] == pytest.approx(190.0, rel=0.01)

    @pytest.mark.asyncio
    async def test_power_calculation(self):
        """Test power calculation."""
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
        ) as client:
            response = await client.post(
                "/api/v1/powertrain/power",
                json={"torque": 100, "rpm": 3000, "unit": "watts"},
            )
        assert response.status_code == 200
        data = response.json()
        assert "power_watts" in data
        assert "power_hp" in data
        assert data["power_watts"] > 0
        assert data["power_hp"] > 0

    @pytest.mark.asyncio
    async def test_power_conversion(self):
        """Test power unit conversion."""
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
        ) as client:
            response = await client.post(
                "/api/v1/powertrain/power",
                json={"torque": 100, "rpm": 5252, "unit": "horsepower"},
            )
        assert response.status_code == 200
        data = response.json()
        # At 5252 RPM with 100 lb-ft, power should be approximately 100 HP
        # But we're using Nm, so the relationship is different
        assert data["power_hp"] == pytest.approx(
            data["power_watts"] / 745.7, rel=0.01
        )
