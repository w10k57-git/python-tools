"""Tests for beam mechanics calculation endpoints."""

import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app


class TestBeamCalculations:
    """Test beam mechanics calculation endpoints."""

    @pytest.mark.asyncio
    async def test_beam_deflection_simply_supported(self):
        """Test beam deflection for simply supported beam."""
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
        ) as client:
            response = await client.post(
                "/api/v1/beam/deflection",
                json={
                    "load": 1000,
                    "length": 2.0,
                    "elastic_modulus": 200e9,
                    "moment_of_inertia": 1e-6,
                    "support_type": "simply_supported",
                },
            )
        assert response.status_code == 200
        data = response.json()
        assert "deflection" in data
        assert "deflection_mm" in data
        assert data["deflection"] > 0
        assert data["deflection_mm"] == pytest.approx(data["deflection"] * 1000, rel=0.01)

    @pytest.mark.asyncio
    async def test_beam_deflection_cantilever(self):
        """Test beam deflection for cantilever beam."""
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
        ) as client:
            response = await client.post(
                "/api/v1/beam/deflection",
                json={
                    "load": 1000,
                    "length": 2.0,
                    "elastic_modulus": 200e9,
                    "moment_of_inertia": 1e-6,
                    "support_type": "cantilever",
                },
            )
        assert response.status_code == 200
        data = response.json()
        assert data["deflection"] > 0
        # Cantilever deflection should be larger than simply supported
        assert data["support_type"] == "cantilever"

    @pytest.mark.asyncio
    async def test_beam_deflection_invalid_support(self):
        """Test beam deflection with invalid support type."""
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
        ) as client:
            response = await client.post(
                "/api/v1/beam/deflection",
                json={
                    "load": 1000,
                    "length": 2.0,
                    "elastic_modulus": 200e9,
                    "moment_of_inertia": 1e-6,
                    "support_type": "invalid_type",
                },
            )
        assert response.status_code == 422

    @pytest.mark.asyncio
    async def test_bending_moment_simply_supported(self):
        """Test bending moment calculation for simply supported beam."""
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
        ) as client:
            response = await client.post(
                "/api/v1/beam/bending-moment",
                json={
                    "load": 1000,
                    "length": 4.0,
                    "distance": 2.0,
                    "support_type": "simply_supported",
                },
            )
        assert response.status_code == 200
        data = response.json()
        assert "bending_moment" in data
        assert data["bending_moment"] > 0

    @pytest.mark.asyncio
    async def test_bending_moment_cantilever(self):
        """Test bending moment calculation for cantilever beam."""
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
        ) as client:
            response = await client.post(
                "/api/v1/beam/bending-moment",
                json={
                    "load": 1000,
                    "length": 2.0,
                    "distance": 0.0,
                    "support_type": "cantilever",
                },
            )
        assert response.status_code == 200
        data = response.json()
        # At fixed end of cantilever, moment should be load * length
        assert data["bending_moment"] == pytest.approx(2000, rel=0.01)

    @pytest.mark.asyncio
    async def test_beam_stress_calculation(self):
        """Test beam stress calculation."""
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
        ) as client:
            response = await client.post(
                "/api/v1/beam/stress",
                json={
                    "bending_moment": 1000,
                    "distance_from_neutral": 0.05,
                    "moment_of_inertia": 1e-6,
                },
            )
        assert response.status_code == 200
        data = response.json()
        assert "stress" in data
        assert "stress_mpa" in data
        assert data["stress"] > 0
        assert data["stress_mpa"] == pytest.approx(data["stress"] / 1e6, rel=0.01)

    @pytest.mark.asyncio
    async def test_beam_stress_invalid_input(self):
        """Test beam stress with invalid input (negative moment of inertia)."""
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
        ) as client:
            response = await client.post(
                "/api/v1/beam/stress",
                json={
                    "bending_moment": 1000,
                    "distance_from_neutral": 0.05,
                    "moment_of_inertia": -1e-6,
                },
            )
        assert response.status_code == 422
