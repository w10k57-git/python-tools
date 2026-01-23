"""Powertrain calculation service."""

import math


def calculate_gear_ratio(driver_teeth: int, driven_teeth: int) -> dict:
    """
    Calculate gear ratio and speed reduction.

    Args:
        driver_teeth: Number of teeth on driver gear
        driven_teeth: Number of teeth on driven gear

    Returns:
        Dictionary with gear_ratio and speed_reduction
    """
    gear_ratio = driven_teeth / driver_teeth
    speed_reduction = 1 / gear_ratio

    return {
        "gear_ratio": gear_ratio,
        "speed_reduction": speed_reduction,
    }


def calculate_torque_output(
    input_torque: float, gear_ratio: float, efficiency: float = 0.95
) -> float:
    """
    Calculate output torque considering gear ratio and efficiency.

    Formula: T_out = T_in × GR × η

    Args:
        input_torque: Input torque in Nm
        gear_ratio: Gear ratio (driven/driver)
        efficiency: Mechanical efficiency (0-1), default 0.95

    Returns:
        Output torque in Nm
    """
    output_torque = input_torque * gear_ratio * efficiency
    return output_torque


def calculate_power(torque: float, rpm: float) -> dict:
    """
    Calculate power from torque and RPM.

    Formulas:
        - Power (Watts) = Torque (Nm) × Angular velocity (rad/s)
        - Angular velocity = RPM × 2π / 60
        - Power (HP) = Power (Watts) / 745.7

    Args:
        torque: Torque in Nm
        rpm: Rotational speed in RPM

    Returns:
        Dictionary with power_watts and power_hp
    """
    # Convert RPM to rad/s
    angular_velocity = rpm * 2 * math.pi / 60

    # Calculate power in Watts
    power_watts = torque * angular_velocity

    # Convert to horsepower
    power_hp = power_watts / 745.7

    return {
        "power_watts": power_watts,
        "power_hp": power_hp,
    }
