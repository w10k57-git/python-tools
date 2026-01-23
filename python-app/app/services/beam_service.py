"""Beam mechanics calculation service."""


def calculate_deflection(
    load: float,
    length: float,
    elastic_modulus: float,
    moment_of_inertia: float,
    support_type: str,
) -> float:
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
        Maximum deflection in meters
    """
    if support_type == "simply_supported":
        # Simply supported beam with center load
        deflection = (load * length**3) / (48 * elastic_modulus * moment_of_inertia)
    elif support_type == "cantilever":
        # Cantilever beam with end load
        deflection = (load * length**3) / (3 * elastic_modulus * moment_of_inertia)
    else:
        raise ValueError(f"Unknown support type: {support_type}")

    return deflection


def calculate_bending_moment(
    load: float, length: float, distance: float, support_type: str
) -> float:
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
        Bending moment in Nm
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

    return moment


def calculate_beam_stress(
    bending_moment: float, distance_from_neutral: float, moment_of_inertia: float
) -> float:
    """
    Calculate bending stress in a beam.

    Formula: σ = (M × c) / I

    Args:
        bending_moment: Bending moment in Nm
        distance_from_neutral: Distance from neutral axis (c) in meters
        moment_of_inertia: Second moment of area (I) in m^4

    Returns:
        Bending stress in Pascals
    """
    stress = (bending_moment * distance_from_neutral) / moment_of_inertia
    return stress
