"""Health check endpoint."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/health", tags=["health"])
async def health_check():
    """
    Health check endpoint.

    Returns:
        Status message indicating the API is running
    """
    return {"status": "healthy", "service": "Mechanical Engineering API"}
