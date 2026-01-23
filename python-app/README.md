# Mechanical Engineering API

A production-ready FastAPI application for mechanical engineering calculations, featuring automatic OpenAPI documentation, Docker deployment, and comprehensive testing.

## Features

- **REST API**: FastAPI with automatic OpenAPI/Swagger documentation
- **Powertrain Calculations**: Gear ratios, torque transmission, and power calculations
- **Beam Mechanics**: Deflection, bending moment, and stress analysis
- **Stress Analysis**: Tensile/shear stress, Von Mises stress, and safety factors
- **Type Safety**: Pydantic models for request/response validation
- **Docker Ready**: Multi-stage Dockerfile with non-root user and health checks
- **Production Grade**: CORS middleware, structured logging, error handling
- **Hot Reload**: Development setup with docker-compose

## Installation

### Local Development

```bash
cd python-app

# Sync dependencies
uv sync --extra dev

# Run the application
uv run uvicorn app.main:app --reload

# Visit http://localhost:8000/docs for interactive API documentation
```

### Docker Deployment

```bash
# Build and run with docker-compose
docker-compose up --build

# Or build and run with Docker directly
docker build -t mech-eng-api .
docker run -p 8000:8000 mech-eng-api
```

## API Endpoints

### Health Check

```bash
GET /health
```

Returns service health status.

### Root Information

```bash
GET /
```

Returns API information and links to documentation.

## Powertrain Calculations

### Gear Ratio

Calculate gear ratio and speed reduction from gear teeth count.

```bash
POST /api/v1/powertrain/gear-ratio
Content-Type: application/json

{
  "driver_teeth": 20,
  "driven_teeth": 60
}

# Response
{
  "driver_teeth": 20,
  "driven_teeth": 60,
  "gear_ratio": 3.0,
  "speed_reduction": 0.333
}
```

**Formula**: `GR = N_driven / N_driver`

### Torque Output

Calculate output torque with gear ratio and efficiency.

```bash
POST /api/v1/powertrain/torque
Content-Type: application/json

{
  "input_torque": 100,
  "gear_ratio": 3.0,
  "efficiency": 0.95
}

# Response
{
  "input_torque": 100,
  "gear_ratio": 3.0,
  "efficiency": 0.95,
  "output_torque": 285.0
}
```

**Formula**: `T_out = T_in × GR × η`

### Power Calculation

Calculate power from torque and RPM.

```bash
POST /api/v1/powertrain/power
Content-Type: application/json

{
  "torque": 100,
  "rpm": 3000,
  "unit": "watts"
}

# Response
{
  "torque": 100,
  "rpm": 3000,
  "power_watts": 31415.93,
  "power_hp": 42.14,
  "unit": "watts"
}
```

**Formula**: `P = T × ω` (where ω = RPM × 2π / 60)

## Beam Mechanics

### Beam Deflection

Calculate maximum deflection for simply supported or cantilever beams.

```bash
POST /api/v1/beam/deflection
Content-Type: application/json

{
  "load": 1000,
  "length": 2.0,
  "elastic_modulus": 200e9,
  "moment_of_inertia": 1e-6,
  "support_type": "simply_supported"
}

# Response
{
  "load": 1000,
  "length": 2.0,
  "elastic_modulus": 200000000000,
  "moment_of_inertia": 1e-6,
  "support_type": "simply_supported",
  "deflection": 0.000833,
  "deflection_mm": 0.833
}
```

**Formulas**:
- Simply supported: `δ = (F × L³) / (48 × E × I)`
- Cantilever: `δ = (F × L³) / (3 × E × I)`

### Bending Moment

Calculate bending moment at a specific location on the beam.

```bash
POST /api/v1/beam/bending-moment
Content-Type: application/json

{
  "load": 1000,
  "length": 4.0,
  "distance": 2.0,
  "support_type": "simply_supported"
}

# Response
{
  "load": 1000,
  "length": 4.0,
  "distance": 2.0,
  "support_type": "simply_supported",
  "bending_moment": 1000.0
}
```

### Beam Stress

Calculate bending stress using the flexure formula.

```bash
POST /api/v1/beam/stress
Content-Type: application/json

{
  "bending_moment": 1000,
  "distance_from_neutral": 0.05,
  "moment_of_inertia": 1e-6
}

# Response
{
  "bending_moment": 1000,
  "distance_from_neutral": 0.05,
  "moment_of_inertia": 1e-6,
  "stress": 50000000,
  "stress_mpa": 50.0
}
```

**Formula**: `σ = (M × c) / I`

## Stress Analysis

### Tensile Stress

Calculate tensile or compressive stress.

```bash
POST /api/v1/stress/tensile
Content-Type: application/json

{
  "force": 10000,
  "area": 0.001
}

# Response
{
  "force": 10000,
  "area": 0.001,
  "stress": 10000000,
  "stress_mpa": 10.0
}
```

**Formula**: `σ = F / A`

### Shear Stress

Calculate shear stress.

```bash
POST /api/v1/stress/shear
Content-Type: application/json

{
  "force": 5000,
  "area": 0.0005
}

# Response
{
  "force": 5000,
  "area": 0.0005,
  "shear_stress": 10000000,
  "shear_stress_mpa": 10.0
}
```

**Formula**: `τ = V / A`

### Von Mises Stress

Calculate Von Mises equivalent stress for plane stress condition.

```bash
POST /api/v1/stress/von-mises
Content-Type: application/json

{
  "sigma_x": 100e6,
  "sigma_y": 50e6,
  "tau_xy": 25e6
}

# Response
{
  "sigma_x": 100000000,
  "sigma_y": 50000000,
  "tau_xy": 25000000,
  "von_mises_stress": 91856000,
  "von_mises_stress_mpa": 91.856
}
```

**Formula**: `σ_v = √(σ_x² - σ_x×σ_y + σ_y² + 3×τ_xy²)`

### Safety Factor

Calculate factor of safety with status classification.

```bash
POST /api/v1/stress/safety-factor
Content-Type: application/json

{
  "yield_strength": 250e6,
  "applied_stress": 100e6
}

# Response
{
  "yield_strength": 250000000,
  "applied_stress": 100000000,
  "safety_factor": 2.5,
  "status": "SAFE"
}
```

**Formula**: `SF = σ_yield / σ_applied`

**Status Classification**:
- SAFE: SF ≥ 2.0
- MARGINAL: 1.0 ≤ SF < 2.0
- UNSAFE: SF < 1.0

## Testing with curl

```bash
# Health check
curl http://localhost:8000/health

# Gear ratio calculation
curl -X POST http://localhost:8000/api/v1/powertrain/gear-ratio \
  -H "Content-Type: application/json" \
  -d '{"driver_teeth": 20, "driven_teeth": 60}'

# Beam deflection
curl -X POST http://localhost:8000/api/v1/beam/deflection \
  -H "Content-Type: application/json" \
  -d '{"load": 1000, "length": 2.0, "elastic_modulus": 200e9, "moment_of_inertia": 1e-6, "support_type": "simply_supported"}'

# Safety factor
curl -X POST http://localhost:8000/api/v1/stress/safety-factor \
  -H "Content-Type: application/json" \
  -d '{"yield_strength": 250e6, "applied_stress": 100e6}'
```

## Interactive Documentation

Once the server is running, visit:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

Both provide interactive API documentation where you can test endpoints directly from your browser.

## Development

### Running Tests

```bash
cd python-app
uv sync --extra dev
uv run pytest tests/ -v
```

### Running with Coverage

```bash
uv run pytest --cov=app --cov-report=html
```

### Project Structure

```
python-app/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app initialization
│   ├── config.py            # Settings and configuration
│   ├── utils.py             # Utility functions
│   ├── api/
│   │   └── routes/          # API endpoints
│   │       ├── health.py    # Health check
│   │       ├── powertrain.py # Powertrain calculations
│   │       ├── beam.py      # Beam mechanics
│   │       └── stress.py    # Stress analysis
│   ├── schemas/             # Pydantic models
│   │   ├── powertrain.py
│   │   ├── beam.py
│   │   └── stress.py
│   └── services/            # Business logic
│       ├── powertrain_service.py
│       ├── beam_service.py
│       └── stress_service.py
├── tests/                   # API tests
├── prompts/                 # Empty directory for Docker
├── Dockerfile               # Multi-stage Docker build
├── docker-compose.yml       # Development orchestration
└── pyproject.toml          # Dependencies and config
```

## Docker Configuration

### Dockerfile Features

- **Multi-stage build**: Reduces final image size
- **Non-root user**: Runs as user `appuser` for security
- **Health checks**: Built-in container health monitoring
- **uv for dependencies**: Fast, reliable dependency installation
- **Python 3.12 slim**: Small base image

### docker-compose Features

- **Hot reload**: Source code mounted for development
- **Environment variables**: Easy configuration
- **Health checks**: Container health monitoring
- **Port mapping**: Exposes port 8000

### Production Deployment

```bash
# Build production image
docker build -t mech-eng-api:latest .

# Run production container
docker run -d \
  --name mech-eng-api \
  -p 8000:8000 \
  --health-cmd "python -c 'import urllib.request; urllib.request.urlopen(\"http://localhost:8000/health\")'" \
  --health-interval 30s \
  --health-timeout 10s \
  --health-retries 3 \
  mech-eng-api:latest

# Check container health
docker ps
docker logs mech-eng-api
```

## Environment Variables

Create a `.env` file:

```bash
# Application Settings
APP_NAME=Mechanical Engineering API
API_VERSION=v1
DEBUG=false

# CORS Settings (comma-separated origins)
CORS_ORIGINS=*

# Uvicorn Settings
HOST=0.0.0.0
PORT=8000
WORKERS=1
```

## Architecture

### Layered Design

1. **Routes Layer** (`api/routes/`): API endpoints, request/response handling
2. **Service Layer** (`services/`): Business logic, calculations
3. **Schemas Layer** (`schemas/`): Pydantic models for type safety
4. **Utils Layer** (`utils.py`): Shared utility functions

### Key Technologies

- **FastAPI**: Modern Python web framework with automatic docs
- **Pydantic**: Data validation using Python type annotations
- **Uvicorn**: ASGI server for high performance
- **Docker**: Containerization for consistent deployment
- **uv**: Fast Python package installer and resolver

## API Design Principles

- **RESTful**: Standard HTTP methods and status codes
- **Versioned**: API prefix `/api/v1` for future compatibility
- **Type-Safe**: Pydantic models ensure data validation
- **Self-Documenting**: Automatic OpenAPI/Swagger generation
- **Error Handling**: Clear error messages with appropriate status codes
- **CORS Enabled**: Configurable cross-origin resource sharing

## Use Cases

- Backend for mechanical engineering calculation tools
- Educational platform for engineering students
- Microservice in larger engineering platform
- Reference implementation for FastAPI best practices
- Rapid prototyping of mechanical designs

## Engineering Domains Covered

### Powertrain Engineering
- Gear train analysis
- Torque and power transmission
- Efficiency calculations

### Structural Mechanics
- Beam deflection analysis
- Bending moment calculations
- Stress analysis

### Materials Engineering
- Stress-strain relationships
- Failure prediction (Von Mises)
- Safety factor assessment

## License

MIT
