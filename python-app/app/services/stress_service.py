"""Stress analysis calculation service."""

import math

from app.schemas.stress import (
    TensileStressResponse,
    ShearStressResponse,
    VonMisesStressResponse,
    SafetyFactorResponse,
)


def calculate_tensile_stress(force: float, area: float) -> TensileStressResponse:
    """
    Calculate tensile (or compressive) stress.

    Formula: σ = F / A

    Args:
        force: Applied force in Newtons (positive for tension, negative for compression)
        area: Cross-sectional area in m^2

    Returns:
        TensileStressResponse with all calculated values
    """
    stress = force / area

    return TensileStressResponse(
        force=force,
        area=area,
        stress=stress,
        stress_mpa=stress / 1e6,
    )


def calculate_shear_stress(force: float, area: float) -> ShearStressResponse:
    """
    Calculate shear stress.

    Formula: τ = V / A

    Args:
        force: Shear force in Newtons
        area: Shear area in m^2

    Returns:
        ShearStressResponse with all calculated values
    """
    shear_stress = force / area

    return ShearStressResponse(
        force=force,
        area=area,
        shear_stress=shear_stress,
        shear_stress_mpa=shear_stress / 1e6,
    )


def calculate_von_mises(
    sigma_x: float, sigma_y: float, tau_xy: float
) -> VonMisesStressResponse:
    """
    Calculate Von Mises equivalent stress for plane stress condition.

    Formula: σ_v = √(σ_x² - σ_x×σ_y + σ_y² + 3×τ_xy²)

    Args:
        sigma_x: Normal stress in x-direction (Pascals)
        sigma_y: Normal stress in y-direction (Pascals)
        tau_xy: Shear stress in xy-plane (Pascals)

    Returns:
        VonMisesStressResponse with all calculated values
    """
    von_mises_stress = math.sqrt(
        sigma_x**2 - sigma_x * sigma_y + sigma_y**2 + 3 * tau_xy**2
    )

    return VonMisesStressResponse(
        sigma_x=sigma_x,
        sigma_y=sigma_y,
        tau_xy=tau_xy,
        von_mises_stress=von_mises_stress,
        von_mises_stress_mpa=von_mises_stress / 1e6,
    )


def calculate_safety_factor(
    yield_strength: float, applied_stress: float
) -> SafetyFactorResponse:
    """
    Calculate factor of safety.

    Formula: SF = σ_yield / σ_applied

    Args:
        yield_strength: Material yield strength in Pascals
        applied_stress: Applied stress in Pascals

    Returns:
        SafetyFactorResponse with all calculated values
    """
    safety_factor = yield_strength / applied_stress

    # Determine safety status
    if safety_factor >= 2.0:
        status = "SAFE"
    elif safety_factor >= 1.0:
        status = "MARGINAL"
    else:
        status = "UNSAFE"

    return SafetyFactorResponse(
        yield_strength=yield_strength,
        applied_stress=applied_stress,
        safety_factor=safety_factor,
        status=status,
    )
