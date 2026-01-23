"""Powertrain calculation service."""

import math

from app.schemas.powertrain import (
    GearRatioResponse,
    TorqueResponse,
    PowerResponse,
)


def calculate_gear_ratio(driver_teeth: int, driven_teeth: int) -> GearRatioResponse:
    """
    Calculate gear ratio and speed reduction.

    Args:
        driver_teeth: Number of teeth on driver gear
        driven_teeth: Number of teeth on driven gear

    Returns:
        GearRatioResponse with all calculated values
    """
    gear_ratio = driven_teeth / driver_teeth
    speed_reduction = 1 / gear_ratio

    return GearRatioResponse(
        driver_teeth=driver_teeth,
        driven_teeth=driven_teeth,
        gear_ratio=gear_ratio,
        speed_reduction=speed_reduction,
    )


def calculate_torque_output(
    input_torque: float, gear_ratio: float, efficiency: float = 0.95
) -> TorqueResponse:
    """
    Calculate output torque considering gear ratio and efficiency.

    Formula: T_out = T_in × GR × η

    Args:
        input_torque: Input torque in Nm
        gear_ratio: Gear ratio (driven/driver)
        efficiency: Mechanical efficiency (0-1), default 0.95

    Returns:
        TorqueResponse with all calculated values
    """
    output_torque = input_torque * gear_ratio * efficiency

    return TorqueResponse(
        input_torque=input_torque,
        gear_ratio=gear_ratio,
        efficiency=efficiency,
        output_torque=output_torque,
    )


def calculate_power(torque: float, rpm: float, unit: str = "watts") -> PowerResponse:
    """
    Calculate power from torque and RPM.

    Formulas:
        - Power (Watts) = Torque (Nm) × Angular velocity (rad/s)
        - Angular velocity = RPM × 2π / 60
        - Power (HP) = Power (Watts) / 745.7

    Args:
        torque: Torque in Nm
        rpm: Rotational speed in RPM
        unit: Output unit preference

    Returns:
        PowerResponse with all calculated values
    """
    # Convert RPM to rad/s
    angular_velocity = rpm * 2 * math.pi / 60

    # Calculate power in Watts
    power_watts = torque * angular_velocity

    # Convert to horsepower
    power_hp = power_watts / 745.7

    return PowerResponse(
        torque=torque,
        rpm=rpm,
        power_watts=power_watts,
        power_hp=power_hp,
        unit=unit,
    )
