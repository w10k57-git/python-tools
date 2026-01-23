"""Tests for stress analysis calculation endpoints."""

import pytest
from app.main import app
from httpx import ASGITransport, AsyncClient


class TestStressCalculations:
    """Test stress analysis calculation endpoints."""

    @pytest.mark.asyncio
    async def test_tensile_stress_calculation(self):
        """Test tensile stress calculation."""
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
        ) as client:
            response = await client.post(
                "/api/v1/stress/tensile",
                json={"force": 10000, "area": 0.001},
            )
        assert response.status_code == 200
        data = response.json()
        assert data["stress"] == pytest.approx(10000000, rel=0.01)
        assert data["stress_mpa"] == pytest.approx(10.0, rel=0.01)

    @pytest.mark.asyncio
    async def test_tensile_stress_compression(self):
        """Test compressive stress (negative force)."""
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
        ) as client:
            response = await client.post(
                "/api/v1/stress/tensile",
                json={"force": -5000, "area": 0.0005},
            )
        assert response.status_code == 200
        data = response.json()
        assert data["stress"] < 0  # Compression

    @pytest.mark.asyncio
    async def test_tensile_stress_invalid_area(self):
        """Test tensile stress with invalid area."""
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
        ) as client:
            response = await client.post(
                "/api/v1/stress/tensile",
                json={"force": 10000, "area": 0},
            )
        assert response.status_code == 422

    @pytest.mark.asyncio
    async def test_shear_stress_calculation(self):
        """Test shear stress calculation."""
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
        ) as client:
            response = await client.post(
                "/api/v1/stress/shear",
                json={"force": 5000, "area": 0.0005},
            )
        assert response.status_code == 200
        data = response.json()
        assert data["shear_stress"] == pytest.approx(10000000, rel=0.01)
        assert data["shear_stress_mpa"] == pytest.approx(10.0, rel=0.01)

    @pytest.mark.asyncio
    async def test_von_mises_stress_calculation(self):
        """Test Von Mises stress calculation."""
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
        ) as client:
            response = await client.post(
                "/api/v1/stress/von-mises",
                json={"sigma_x": 100e6, "sigma_y": 50e6, "tau_xy": 25e6},
            )
        assert response.status_code == 200
        data = response.json()
        assert "von_mises_stress" in data
        assert "von_mises_stress_mpa" in data
        assert data["von_mises_stress"] > 0

    @pytest.mark.asyncio
    async def test_von_mises_stress_uniaxial(self):
        """Test Von Mises stress for uniaxial tension."""
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
        ) as client:
            response = await client.post(
                "/api/v1/stress/von-mises",
                json={"sigma_x": 100e6, "sigma_y": 0, "tau_xy": 0},
            )
        assert response.status_code == 200
        data = response.json()
        # For uniaxial stress, Von Mises should equal the applied stress
        assert data["von_mises_stress"] == pytest.approx(100e6, rel=0.01)

    @pytest.mark.asyncio
    async def test_safety_factor_safe(self):
        """Test safety factor calculation - safe condition."""
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
        ) as client:
            response = await client.post(
                "/api/v1/stress/safety-factor",
                json={"yield_strength": 250e6, "applied_stress": 100e6},
            )
        assert response.status_code == 200
        data = response.json()
        assert data["safety_factor"] == pytest.approx(2.5, rel=0.01)
        assert data["status"] == "SAFE"

    @pytest.mark.asyncio
    async def test_safety_factor_marginal(self):
        """Test safety factor calculation - marginal condition."""
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
        ) as client:
            response = await client.post(
                "/api/v1/stress/safety-factor",
                json={"yield_strength": 250e6, "applied_stress": 200e6},
            )
        assert response.status_code == 200
        data = response.json()
        assert data["safety_factor"] == pytest.approx(1.25, rel=0.01)
        assert data["status"] == "MARGINAL"

    @pytest.mark.asyncio
    async def test_safety_factor_unsafe(self):
        """Test safety factor calculation - unsafe condition."""
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
        ) as client:
            response = await client.post(
                "/api/v1/stress/safety-factor",
                json={"yield_strength": 250e6, "applied_stress": 300e6},
            )
        assert response.status_code == 200
        data = response.json()
        assert data["safety_factor"] < 1.0
        assert data["status"] == "UNSAFE"

    @pytest.mark.asyncio
    async def test_safety_factor_invalid_input(self):
        """Test safety factor with invalid input."""
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
        ) as client:
            response = await client.post(
                "/api/v1/stress/safety-factor",
                json={"yield_strength": -250e6, "applied_stress": 100e6},
            )
        assert response.status_code == 422
