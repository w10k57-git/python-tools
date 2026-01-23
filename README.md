# Python Teaching Repository: Three Packaging Patterns

A comprehensive teaching repository demonstrating three distinct Python project patterns, all focused on engineering calculations. Each project showcases modern Python packaging with `uv` and `pyproject.toml`.

## Overview

This repository contains three independent Python projects that demonstrate different packaging and deployment patterns:

1. **python-package** - Reusable library with src layout
2. **python-cli** - Command-line tool with entry points
3. **python-app** - FastAPI REST API with Docker deployment

All three projects implement the same domain (engineering calculations) but serve different purposes and use cases.

## Requirements

- **Python**: 3.11 or higher
- **uv**: Fast Python package installer ([installation guide](https://docs.astral.sh/uv/))
- **Docker**: For python-app deployment (optional)

## Projects

### 1. python-package: Reusable Library

**Location**: `python-package/`

A zero-dependency calculation library with clean API and src layout.

**Key Features**:
- Src layout for import safety
- Pure Python calculations (no dependencies)
- Type hints with `py.typed` marker
- Installable from GitHub

**Installation**:
```bash
cd python-package
uv sync --extra dev
uv run pytest tests/
```

**Usage**:
```python
from engcalc.conversions import celsius_to_fahrenheit
from engcalc.formulas import ohms_law

celsius_to_fahrenheit(100)  # 212.0
ohms_law(voltage=12, current=3)  # 4.0 (resistance)
```

**Learn About**:
- Src layout benefits
- Public API design with `__init__.py`
- Zero-dependency library patterns
- PEP 561 type hints

[Full Documentation →](python-package/README.md)

---

### 2. python-cli: Command-Line Tool

**Location**: `python-cli/`

An intuitive CLI tool built with Click and Rich for colored terminal output.

**Key Features**:
- Click framework for elegant CLI
- Command groups and subcommands
- Entry points for global installation
- Colorful, formatted output

**Installation**:
```bash
cd python-cli
uv tool install .
```

**Usage**:
```bash
# Convert temperature
engcalc convert temperature 100 --from celsius --to fahrenheit

# Calculate Ohm's Law
engcalc calc ohms-law --voltage 12 --current 3

# Calculate Reynolds number
engcalc calc reynolds -d 1000 -v 2 -D 0.1 -m 0.001
```

**Learn About**:
- Click command groups and decorators
- Entry points configuration
- `uv tool install` for isolated CLI tools
- Rich terminal formatting

[Full Documentation →](python-cli/README.md)

---

### 3. python-app: REST API with Docker

**Location**: `python-app/`

Production-ready FastAPI application with automatic documentation and Docker deployment.

**Key Features**:
- FastAPI with automatic OpenAPI docs
- Pydantic models for type safety
- Multi-stage Docker build
- CORS, health checks, structured routes

**Installation**:
```bash
cd python-app
uv sync --extra dev
uv run uvicorn engcalc_api.main:app --reload
```

**Docker**:
```bash
docker-compose up --build
```

**API Endpoints**:
- `GET /health` - Health check
- `POST /api/v1/conversions/temperature` - Convert temperature
- `POST /api/v1/formulas/electrical/ohms-law` - Ohm's Law calculation
- `GET /docs` - Interactive Swagger documentation

**Learn About**:
- FastAPI application structure
- Pydantic request/response models
- Multi-stage Docker builds with uv
- REST API design patterns

[Full Documentation →](python-app/README.md)

---

## Quick Start

### Test All Projects

```bash
# Library
cd python-package
uv sync --extra dev
uv run pytest tests/

# CLI Tool
cd ../python-cli
uv sync --extra dev
uv run pytest tests/
uv run engcalc --help

# REST API
cd ../python-app
uv sync --extra dev
uv run pytest tests/
uv run uvicorn engcalc_api.main:app --reload
```

## Domain: Engineering Calculations

All three projects implement the same functionality domain:

### Unit Conversions
- **Temperature**: Celsius ↔ Fahrenheit ↔ Kelvin
- **Pressure**: PSI ↔ Bar ↔ Pascal ↔ kPa
- **Length**: Meters ↔ Feet ↔ Inches

### Engineering Formulas
- **Ohm's Law**: V = I × R
- **Electrical Power**: P = V × I
- **Ideal Gas Law**: PV = nRT
- **Reynolds Number**: Re = (ρvD)/μ

### Physical Constants
- Gravitational acceleration (g)
- Universal gas constant (R)
- Standard atmospheric pressure
- Material resistivities

## Learning Objectives

### Python Packaging
- Modern `pyproject.toml` configuration
- Src vs flat layouts
- Entry points and scripts
- Dependencies management with uv

### Project Patterns
- **Library**: Reusable, importable code
- **CLI**: Interactive terminal applications
- **API**: Web services and REST endpoints

### Tools & Frameworks
- **uv**: Fast dependency resolution and project management
- **Click**: CLI framework with decorators
- **FastAPI**: Modern web framework with auto docs
- **Pydantic**: Data validation with type hints
- **Docker**: Containerization and deployment

### Best Practices
- Type hints and type safety
- Automated testing with pytest
- API documentation
- Error handling
- Security (non-root Docker user)
- CORS configuration

## Architecture Comparison

| Feature | python-package | python-cli | python-app |
|---------|---------------|------------|------------|
| **Type** | Library | CLI Tool | Web API |
| **Interface** | Import | Commands | HTTP |
| **Installation** | `uv pip install` | `uv tool install` | Docker |
| **Dependencies** | None | Click, Rich | FastAPI, Uvicorn |
| **Entry Point** | Import | Script | Server |
| **Output** | Return values | Terminal | JSON |
| **Docs** | Docstrings | --help | OpenAPI |

## Teaching Flow

### Beginner Path
1. Start with **python-package** to understand:
   - Basic Python packaging
   - Src layout
   - Imports and modules
   - Testing with pytest

2. Move to **python-cli** to learn:
   - Entry points
   - CLI frameworks
   - User interaction
   - Tool installation

3. Finish with **python-app** to explore:
   - Web frameworks
   - API design
   - Docker deployment
   - Production patterns

### Advanced Topics
- Compare the same calculation logic across three interfaces
- Study how each project handles errors differently
- Analyze dependency choices and trade-offs
- Explore testing strategies for each pattern

## Development Workflow

### Adding a New Feature

To add a new engineering calculation to all three projects:

1. **python-package**: Add function to appropriate module
2. **python-cli**: Add command to conversions.py or formulas.py
3. **python-app**: Add route, request/response models, and service

### Example: Adding Heat Capacity

**Library**:
```python
# python-package/src/engcalc/formulas/thermodynamics.py
def heat_capacity(mass: float, specific_heat: float, delta_temp: float) -> float:
    return mass * specific_heat * delta_temp
```

**CLI**:
```python
# python-cli/src/engcalc_cli/formulas.py
@calc.command()
@click.option("--mass", required=True)
@click.option("--specific-heat", required=True)
@click.option("--delta-temp", required=True)
def heat_capacity(mass, specific_heat, delta_temp):
    result = mass * specific_heat * delta_temp
    click.echo(f"Heat energy: {result} J")
```

**API**:
```python
# python-app/src/engcalc_api/routes/formulas.py
@router.post("/thermodynamics/heat-capacity")
async def heat_capacity(request: HeatCapacityRequest):
    result = request.mass * request.specific_heat * request.delta_temp
    return HeatCapacityResponse(heat_energy=result)
```

## Common Tasks

### Running Tests
```bash
# All projects
cd python-package && uv run pytest
cd python-cli && uv run pytest
cd python-app && uv run pytest
```

### Type Checking
```bash
# Install mypy
uv pip install mypy

# Check each project
cd python-package && uv run mypy src/
cd python-cli && uv run mypy src/
cd python-app && uv run mypy src/
```

### Code Coverage
```bash
cd python-package && uv run pytest --cov=engcalc --cov-report=html
cd python-cli && uv run pytest --cov=engcalc_cli --cov-report=html
cd python-app && uv run pytest --cov=engcalc_api --cov-report=html
```

## Project Structure

```
python-tools/
├── README.md                   # This file
├── .gitignore                  # Python-specific ignores
│
├── python-package/             # Library project
│   ├── src/engcalc/           # Src layout
│   ├── tests/                 # Pytest tests
│   ├── pyproject.toml         # Hatchling backend
│   └── README.md              # Library docs
│
├── python-cli/                # CLI project
│   ├── src/engcalc_cli/      # CLI code
│   ├── tests/                # CLI tests
│   ├── pyproject.toml        # Entry points
│   └── README.md             # CLI docs
│
└── python-app/               # API project
    ├── src/engcalc_api/     # FastAPI app
    │   ├── routes/          # API endpoints
    │   ├── models/          # Pydantic schemas
    │   └── services/        # Business logic
    ├── tests/               # API tests
    ├── Dockerfile           # Multi-stage build
    ├── docker-compose.yml   # Development setup
    ├── pyproject.toml       # FastAPI deps
    └── README.md            # API docs
```

## Why Three Projects?

Each project teaches distinct concepts:

- **python-package**: Foundation of Python packaging, imports, and library design
- **python-cli**: User interfaces, entry points, and tool distribution
- **python-app**: Web services, APIs, Docker, and production deployment

By implementing the same domain across three patterns, students can:
- Compare interfaces and use cases
- Understand packaging trade-offs
- Learn when to use each pattern
- Practice consistent implementation across contexts

## Resources

### Documentation
- [uv Documentation](https://docs.astral.sh/uv/)
- [Python Packaging Guide](https://packaging.python.org/)
- [Click Documentation](https://click.palletsprojects.com/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)

### Related Concepts
- PEP 517/518: Modern Python packaging
- PEP 561: Type hints in libraries
- ASGI: Async web server gateway
- OpenAPI/Swagger: API documentation
- Docker best practices