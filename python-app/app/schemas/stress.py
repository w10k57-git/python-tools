"""Stress analysis calculation schemas."""

from pydantic import BaseModel, Field


class TensileStressRequest(BaseModel):
    """Request model for tensile stress calculation."""

    force: float = Field(..., description="Applied force in Newtons")
    area: float = Field(..., gt=0, description="Cross-sectional area in m^2")


class TensileStressResponse(BaseModel):
    """Response model for tensile stress calculation."""

    force: float
    area: float
    stress: float = Field(..., description="Tensile stress in Pascals")
    stress_mpa: float = Field(..., description="Tensile stress in MPa")


class ShearStressRequest(BaseModel):
    """Request model for shear stress calculation."""

    force: float = Field(..., description="Shear force in Newtons")
    area: float = Field(..., gt=0, description="Shear area in m^2")


class ShearStressResponse(BaseModel):
    """Response model for shear stress calculation."""

    force: float
    area: float
    shear_stress: float = Field(..., description="Shear stress in Pascals")
    shear_stress_mpa: float = Field(..., description="Shear stress in MPa")


class VonMisesStressRequest(BaseModel):
    """Request model for Von Mises stress calculation."""

    sigma_x: float = Field(..., description="Normal stress in x-direction (Pascals)")
    sigma_y: float = Field(..., description="Normal stress in y-direction (Pascals)")
    tau_xy: float = Field(..., description="Shear stress in xy-plane (Pascals)")


class VonMisesStressResponse(BaseModel):
    """Response model for Von Mises stress calculation."""

    sigma_x: float
    sigma_y: float
    tau_xy: float
    von_mises_stress: float = Field(..., description="Von Mises stress in Pascals")
    von_mises_stress_mpa: float = Field(..., description="Von Mises stress in MPa")


class SafetyFactorRequest(BaseModel):
    """Request model for safety factor calculation."""

    yield_strength: float = Field(
        ..., gt=0, description="Material yield strength in Pascals"
    )
    applied_stress: float = Field(..., gt=0, description="Applied stress in Pascals")


class SafetyFactorResponse(BaseModel):
    """Response model for safety factor calculation."""

    yield_strength: float
    applied_stress: float
    safety_factor: float = Field(..., description="Factor of safety (dimensionless)")
    status: str = Field(
        ..., description="Safety status: 'SAFE', 'MARGINAL', or 'UNSAFE'"
    )
