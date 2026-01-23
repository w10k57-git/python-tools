"""Beam mechanics calculation endpoints."""

from fastapi import APIRouter, HTTPException

from app.schemas.beam import (
    BeamDeflectionRequest,
    BeamDeflectionResponse,
    BeamStressRequest,
    BeamStressResponse,
    BendingMomentRequest,
    BendingMomentResponse,
)
from app.services import beam_service

router = APIRouter(prefix="/api/v1/beam", tags=["beam"])


@router.post("/deflection", response_model=BeamDeflectionResponse)
async def calculate_deflection(request: BeamDeflectionRequest):
    """
    Calculate maximum beam deflection.

    Supports two support types:
    - simply_supported: Beam supported at both ends with center load
    - cantilever: Beam fixed at one end with load at free end

    Returns deflection in both meters and millimeters.
    """
    return beam_service.calculate_deflection(
        request.load,
        request.length,
        request.elastic_modulus,
        request.moment_of_inertia,
        request.support_type,
    )


@router.post("/bending-moment", response_model=BendingMomentResponse)
async def calculate_bending_moment(request: BendingMomentRequest):
    """
    Calculate bending moment at a specific location on the beam.

    The bending moment varies along the beam length depending on
    the support type and load configuration.
    """
    if request.distance > request.length:
        raise HTTPException(
            status_code=400, detail="Distance cannot exceed beam length"
        )

    return beam_service.calculate_bending_moment(
        request.load, request.length, request.distance, request.support_type
    )


@router.post("/stress", response_model=BeamStressResponse)
async def calculate_beam_stress(request: BeamStressRequest):
    """
    Calculate bending stress in a beam.

    Uses the flexure formula: σ = (M × c) / I

    where:
    - M = bending moment
    - c = distance from neutral axis
    - I = second moment of area

    Returns stress in both Pascals and MPa.
    """
    return beam_service.calculate_beam_stress(
        request.bending_moment,
        request.distance_from_neutral,
        request.moment_of_inertia,
    )
