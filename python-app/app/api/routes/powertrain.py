"""Powertrain calculation endpoints."""

from fastapi import APIRouter

from app.schemas.powertrain import (
    GearRatioRequest,
    GearRatioResponse,
    PowerRequest,
    PowerResponse,
    TorqueRequest,
    TorqueResponse,
)
from app.services import powertrain_service

router = APIRouter(prefix="/api/v1/powertrain", tags=["powertrain"])


@router.post("/gear-ratio", response_model=GearRatioResponse)
async def calculate_gear_ratio(request: GearRatioRequest):
    """
    Calculate gear ratio and speed reduction.

    The gear ratio is defined as the ratio of driven teeth to driver teeth.
    A gear ratio > 1 means speed reduction (torque multiplication).
    A gear ratio < 1 means speed increase (torque reduction).
    """
    return powertrain_service.calculate_gear_ratio(
        request.driver_teeth, request.driven_teeth
    )


@router.post("/torque", response_model=TorqueResponse)
async def calculate_torque(request: TorqueRequest):
    """
    Calculate output torque considering gear ratio and efficiency.

    Output torque = Input torque × Gear ratio × Efficiency

    Efficiency accounts for mechanical losses (friction, etc.)
    """
    return powertrain_service.calculate_torque_output(
        request.input_torque, request.gear_ratio, request.efficiency
    )


@router.post("/power", response_model=PowerResponse)
async def calculate_power(request: PowerRequest):
    """
    Calculate power from torque and RPM.

    Power = Torque × Angular velocity

    Returns power in both Watts and horsepower.
    """
    return powertrain_service.calculate_power(request.torque, request.rpm, request.unit)
