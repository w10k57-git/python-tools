"""Thermodynamics formulas."""

from typing import Optional


def ideal_gas_law(
    pressure: Optional[float] = None,
    volume: Optional[float] = None,
    moles: Optional[float] = None,
    temperature: Optional[float] = None,
    R: float = 8.314,
) -> float:
    """Calculate unknown value using Ideal Gas Law: PV = nRT

    Provide any three of the four parameters to calculate the fourth.

    Formula: PV = nRT
    Where:
        P = Pressure (Pascals)
        V = Volume (cubic meters)
        n = Number of moles
        R = Gas constant (8.314 J/(mol·K) by default)
        T = Temperature (Kelvin)

    Args:
        pressure: Pressure in Pascals (optional)
        volume: Volume in cubic meters (optional)
        moles: Number of moles (optional)
        temperature: Temperature in Kelvin (optional)
        R: Gas constant in J/(mol·K) (default: 8.314)

    Returns:
        The calculated value (pressure, volume, moles, or temperature)

    Raises:
        ValueError: If not exactly three parameters are provided

    Examples:
        >>> round(ideal_gas_law(pressure=101325, volume=0.0224, moles=1, R=8.314), 2)
        273.15
    """
    provided = sum(x is not None for x in [pressure, volume, moles, temperature])

    if provided != 3:
        raise ValueError("Must provide exactly three of four parameters")

    if pressure is None:
        return (moles * R * temperature) / volume  # type: ignore
    elif volume is None:
        return (moles * R * temperature) / pressure  # type: ignore
    elif moles is None:
        return (pressure * volume) / (R * temperature)  # type: ignore
    else:  # temperature is None
        return (pressure * volume) / (moles * R)  # type: ignore


def heat_capacity(mass: float, specific_heat: float, delta_temp: float) -> float:
    """Calculate heat energy using heat capacity formula.

    Formula: Q = mcΔT
    Where:
        Q = Heat energy (Joules)
        m = Mass (kilograms)
        c = Specific heat capacity (J/(kg·K))
        ΔT = Temperature change (Kelvin or Celsius)

    Args:
        mass: Mass in kilograms
        specific_heat: Specific heat capacity in J/(kg·K)
        delta_temp: Temperature change in K or °C

    Returns:
        Heat energy in Joules

    Examples:
        >>> heat_capacity(1.0, 4186, 10)  # Heat 1kg water by 10°C
        41860.0
    """
    return mass * specific_heat * delta_temp


def reynolds_number(
    density: float, velocity: float, diameter: float, viscosity: float
) -> float:
    """Calculate Reynolds number for fluid flow.

    Formula: Re = (ρvD)/μ
    Where:
        Re = Reynolds number (dimensionless)
        ρ = Fluid density (kg/m³)
        v = Flow velocity (m/s)
        D = Characteristic length/diameter (m)
        μ = Dynamic viscosity (Pa·s)

    Args:
        density: Fluid density in kg/m³
        velocity: Flow velocity in m/s
        diameter: Characteristic length in meters
        viscosity: Dynamic viscosity in Pa·s

    Returns:
        Reynolds number (dimensionless)

    Examples:
        >>> reynolds_number(1000, 2, 0.1, 0.001)
        200000.0
    """
    return (density * velocity * diameter) / viscosity


def flow_rate(velocity: float, area: float) -> float:
    """Calculate volumetric flow rate.

    Formula: Q = vA
    Where:
        Q = Volumetric flow rate (m³/s)
        v = Flow velocity (m/s)
        A = Cross-sectional area (m²)

    Args:
        velocity: Flow velocity in m/s
        area: Cross-sectional area in m²

    Returns:
        Volumetric flow rate in m³/s

    Examples:
        >>> flow_rate(2.0, 0.5)
        1.0
    """
    return velocity * area
