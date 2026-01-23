"""FastAPI application entry point."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import __version__
from app.config import settings
from app.api.routes import health, powertrain, beam, stress

app = FastAPI(
    title=settings.app_name,
    version=__version__,
    description="REST API for mechanical engineering calculations including powertrain analysis, beam mechanics, and stress analysis",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(health.router)
app.include_router(powertrain.router)
app.include_router(beam.router)
app.include_router(stress.router)


@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "name": settings.app_name,
        "version": __version__,
        "docs": "/docs",
        "health": "/health",
        "categories": {
            "powertrain": "/api/v1/powertrain",
            "beam": "/api/v1/beam",
            "stress": "/api/v1/stress",
        },
    }
