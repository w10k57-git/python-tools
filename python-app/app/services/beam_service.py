"""Beam mechanics calculation service."""

from app.schemas.beam import (
    BeamDeflectionResponse,
    BendingMomentResponse,
    BeamStressResponse,
)


def calculate_deflection(
    load: float,
    length: float,
    elastic_modulus: float,
    moment_of_inertia: float,
    support_type: str,
) -> BeamDeflectionResponse:
    """
    Calculate maximum beam deflection.

    Formulas:
        - Simply supported (center load): δ = (F × L³) / (48 × E × I)
        - Cantilever (end load): δ = (F × L³) / (3 × E × I)

    Args:
        load: Applied load in Newtons
        length: Beam length in meters
        elastic_modulus: Young's modulus (E) in Pascals
        moment_of_inertia: Second moment of area (I) in m^4
        support_type: 'simply_supported' or 'cantilever'

    Returns:
        BeamDeflectionResponse with all calculated values
    """
    if support_type == "simply_supported":
        # Simply supported beam with center load
        deflection = (load * length**3) / (48 * elastic_modulus * moment_of_inertia)
    elif support_type == "cantilever":
        # Cantilever beam with end load
        deflection = (load * length**3) / (3 * elastic_modulus * moment_of_inertia)
    else:
        raise ValueError(f"Unknown support type: {support_type}")

    return BeamDeflectionResponse(
        load=load,
        length=length,
        elastic_modulus=elastic_modulus,
        moment_of_inertia=moment_of_inertia,
        support_type=support_type,
        deflection=deflection,
        deflection_mm=deflection * 1000,
    )


def calculate_bending_moment(
    load: float, length: float, distance: float, support_type: str
) -> BendingMomentResponse:
    """
    Calculate bending moment at a specific location.

    Formulas:
        - Simply supported (center load at distance x): M = (F × x) / 2 for x <= L/2
        - Cantilever (end load at distance x from fixed end): M = F × (L - x)

    Args:
        load: Applied load in Newtons
        length: Beam length in meters
        distance: Distance from support in meters
        support_type: 'simply_supported' or 'cantilever'

    Returns:
        BendingMomentResponse with all calculated values
    """
    if support_type == "simply_supported":
        # Simply supported beam with center load
        # Maximum moment at center
        if distance <= length / 2:
            moment = (load * distance) / 2
        else:
            moment = (load * (length - distance)) / 2
    elif support_type == "cantilever":
        # Cantilever beam with end load
        # Maximum moment at fixed end
        moment = load * (length - distance)
    else:
        raise ValueError(f"Unknown support type: {support_type}")

    return BendingMomentResponse(
        load=load,
        length=length,
        distance=distance,
        support_type=support_type,
        bending_moment=moment,
    )


def calculate_beam_stress(
    bending_moment: float, distance_from_neutral: float, moment_of_inertia: float
) -> BeamStressResponse:
    """
    Calculate bending stress in a beam.

    Formula: σ = (M × c) / I

    Args:
        bending_moment: Bending moment in Nm
        distance_from_neutral: Distance from neutral axis (c) in meters
        moment_of_inertia: Second moment of area (I) in m^4

    Returns:
        BeamStressResponse with all calculated values
    """
    stress = (bending_moment * distance_from_neutral) / moment_of_inertia

    return BeamStressResponse(
        bending_moment=bending_moment,
        distance_from_neutral=distance_from_neutral,
        moment_of_inertia=moment_of_inertia,
        stress=stress,
        stress_mpa=stress / 1e6,
    )
