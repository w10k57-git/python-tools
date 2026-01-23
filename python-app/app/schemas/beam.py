"""Beam mechanics calculation schemas."""

from pydantic import BaseModel, Field
from typing import Literal


class BeamDeflectionRequest(BaseModel):
    """Request model for beam deflection calculation."""

    load: float = Field(..., gt=0, description="Applied load in Newtons")
    length: float = Field(..., gt=0, description="Beam length in meters")
    elastic_modulus: float = Field(
        ..., gt=0, description="Elastic modulus (E) in Pascals"
    )
    moment_of_inertia: float = Field(
        ..., gt=0, description="Second moment of area (I) in m^4"
    )
    support_type: Literal["simply_supported", "cantilever"] = Field(
        ..., description="Type of beam support"
    )


class BeamDeflectionResponse(BaseModel):
    """Response model for beam deflection calculation."""

    load: float
    length: float
    elastic_modulus: float
    moment_of_inertia: float
    support_type: str
    deflection: float = Field(..., description="Maximum deflection in meters")
    deflection_mm: float = Field(..., description="Maximum deflection in millimeters")


class BendingMomentRequest(BaseModel):
    """Request model for bending moment calculation."""

    load: float = Field(..., gt=0, description="Applied load in Newtons")
    length: float = Field(..., gt=0, description="Beam length in meters")
    distance: float = Field(
        ..., ge=0, description="Distance from support in meters"
    )
    support_type: Literal["simply_supported", "cantilever"] = Field(
        ..., description="Type of beam support"
    )


class BendingMomentResponse(BaseModel):
    """Response model for bending moment calculation."""

    load: float
    length: float
    distance: float
    support_type: str
    bending_moment: float = Field(..., description="Bending moment in Nm")


class BeamStressRequest(BaseModel):
    """Request model for beam stress calculation."""

    bending_moment: float = Field(..., description="Bending moment in Nm")
    distance_from_neutral: float = Field(
        ..., gt=0, description="Distance from neutral axis (c) in meters"
    )
    moment_of_inertia: float = Field(
        ..., gt=0, description="Second moment of area (I) in m^4"
    )


class BeamStressResponse(BaseModel):
    """Response model for beam stress calculation."""

    bending_moment: float
    distance_from_neutral: float
    moment_of_inertia: float
    stress: float = Field(..., description="Bending stress in Pascals")
    stress_mpa: float = Field(..., description="Bending stress in MPa")
