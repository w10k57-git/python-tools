"""Powertrain calculation schemas."""

from pydantic import BaseModel, Field


class GearRatioRequest(BaseModel):
    """Request model for gear ratio calculation."""

    driver_teeth: int = Field(..., gt=0, description="Number of teeth on driver gear")
    driven_teeth: int = Field(..., gt=0, description="Number of teeth on driven gear")


class GearRatioResponse(BaseModel):
    """Response model for gear ratio calculation."""

    driver_teeth: int
    driven_teeth: int
    gear_ratio: float = Field(..., description="Calculated gear ratio (driven/driver)")
    speed_reduction: float = Field(
        ..., description="Speed reduction factor (1/gear_ratio)"
    )


class TorqueRequest(BaseModel):
    """Request model for torque calculation."""

    input_torque: float = Field(..., gt=0, description="Input torque in Nm")
    gear_ratio: float = Field(..., gt=0, description="Gear ratio")
    efficiency: float = Field(
        default=0.95, gt=0, le=1.0, description="Mechanical efficiency (0-1)"
    )


class TorqueResponse(BaseModel):
    """Response model for torque calculation."""

    input_torque: float
    gear_ratio: float
    efficiency: float
    output_torque: float = Field(..., description="Output torque in Nm")


class PowerRequest(BaseModel):
    """Request model for power calculation."""

    torque: float = Field(..., description="Torque in Nm")
    rpm: float = Field(..., gt=0, description="Rotational speed in RPM")
    unit: str = Field(
        default="watts", description="Output unit: 'watts' or 'horsepower'"
    )


class PowerResponse(BaseModel):
    """Response model for power calculation."""

    torque: float
    rpm: float
    power_watts: float = Field(..., description="Power in Watts")
    power_hp: float = Field(..., description="Power in horsepower")
    unit: str
