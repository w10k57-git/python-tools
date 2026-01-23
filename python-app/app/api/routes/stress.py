"""Stress analysis calculation endpoints."""

from fastapi import APIRouter

from app.schemas.stress import (
    TensileStressRequest,
    TensileStressResponse,
    ShearStressRequest,
    ShearStressResponse,
    VonMisesStressRequest,
    VonMisesStressResponse,
    SafetyFactorRequest,
    SafetyFactorResponse,
)
from app.services import stress_service

router = APIRouter(prefix="/api/v1/stress", tags=["stress"])


@router.post("/tensile", response_model=TensileStressResponse)
async def calculate_tensile_stress(request: TensileStressRequest):
    """
    Calculate tensile or compressive stress.

    Formula: σ = F / A

    Positive force indicates tension, negative indicates compression.
    Returns stress in both Pascals and MPa.
    """
    stress = stress_service.calculate_tensile_stress(request.force, request.area)

    return TensileStressResponse(
        force=request.force,
        area=request.area,
        stress=stress,
        stress_mpa=stress / 1e6,
    )


@router.post("/shear", response_model=ShearStressResponse)
async def calculate_shear_stress(request: ShearStressRequest):
    """
    Calculate shear stress.

    Formula: τ = V / A

    Shear stress occurs when forces are applied parallel to a surface.
    Returns stress in both Pascals and MPa.
    """
    shear_stress = stress_service.calculate_shear_stress(request.force, request.area)

    return ShearStressResponse(
        force=request.force,
        area=request.area,
        shear_stress=shear_stress,
        shear_stress_mpa=shear_stress / 1e6,
    )


@router.post("/von-mises", response_model=VonMisesStressResponse)
async def calculate_von_mises_stress(request: VonMisesStressRequest):
    """
    Calculate Von Mises equivalent stress for plane stress condition.

    Formula: σ_v = √(σ_x² - σ_x×σ_y + σ_y² + 3×τ_xy²)

    Von Mises stress is used in failure prediction for ductile materials.
    Returns stress in both Pascals and MPa.
    """
    von_mises = stress_service.calculate_von_mises(
        request.sigma_x, request.sigma_y, request.tau_xy
    )

    return VonMisesStressResponse(
        sigma_x=request.sigma_x,
        sigma_y=request.sigma_y,
        tau_xy=request.tau_xy,
        von_mises_stress=von_mises,
        von_mises_stress_mpa=von_mises / 1e6,
    )


@router.post("/safety-factor", response_model=SafetyFactorResponse)
async def calculate_safety_factor(request: SafetyFactorRequest):
    """
    Calculate factor of safety.

    Formula: SF = σ_yield / σ_applied

    Safety status classification:
    - SAFE: SF >= 2.0
    - MARGINAL: 1.0 <= SF < 2.0
    - UNSAFE: SF < 1.0
    """
    result = stress_service.calculate_safety_factor(
        request.yield_strength, request.applied_stress
    )

    return SafetyFactorResponse(
        yield_strength=request.yield_strength,
        applied_stress=request.applied_stress,
        safety_factor=result["safety_factor"],
        status=result["status"],
    )
