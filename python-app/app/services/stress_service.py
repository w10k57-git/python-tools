"""Stress analysis calculation service."""

import math


def calculate_tensile_stress(force: float, area: float) -> float:
    """
    Calculate tensile (or compressive) stress.

    Formula: σ = F / A

    Args:
        force: Applied force in Newtons (positive for tension, negative for compression)
        area: Cross-sectional area in m^2

    Returns:
        Stress in Pascals
    """
    stress = force / area
    return stress


def calculate_shear_stress(force: float, area: float) -> float:
    """
    Calculate shear stress.

    Formula: τ = V / A

    Args:
        force: Shear force in Newtons
        area: Shear area in m^2

    Returns:
        Shear stress in Pascals
    """
    shear_stress = force / area
    return shear_stress


def calculate_von_mises(sigma_x: float, sigma_y: float, tau_xy: float) -> float:
    """
    Calculate Von Mises equivalent stress for plane stress condition.

    Formula: σ_v = √(σ_x² - σ_x×σ_y + σ_y² + 3×τ_xy²)

    Args:
        sigma_x: Normal stress in x-direction (Pascals)
        sigma_y: Normal stress in y-direction (Pascals)
        tau_xy: Shear stress in xy-plane (Pascals)

    Returns:
        Von Mises stress in Pascals
    """
    von_mises_stress = math.sqrt(
        sigma_x**2 - sigma_x * sigma_y + sigma_y**2 + 3 * tau_xy**2
    )
    return von_mises_stress


def calculate_safety_factor(yield_strength: float, applied_stress: float) -> dict:
    """
    Calculate factor of safety.

    Formula: SF = σ_yield / σ_applied

    Args:
        yield_strength: Material yield strength in Pascals
        applied_stress: Applied stress in Pascals

    Returns:
        Dictionary with safety_factor and status
    """
    safety_factor = yield_strength / applied_stress

    # Determine safety status
    if safety_factor >= 2.0:
        status = "SAFE"
    elif safety_factor >= 1.0:
        status = "MARGINAL"
    else:
        status = "UNSAFE"

    return {
        "safety_factor": safety_factor,
        "status": status,
    }
