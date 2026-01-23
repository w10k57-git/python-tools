# engcalc - Engineering Calculations Library

A pure Python library for engineering calculations including unit conversions and formulas. Zero dependencies, clean API, fully typed.

## Features

- **Unit Conversions**
  - Temperature (Celsius, Fahrenheit, Kelvin)
  - Pressure (PSI, Bar, Pascal, kPa)
  - Length (meters, feet, inches)

- **Electrical Formulas**
  - Ohm's Law (V = IR)
  - Electrical Power (P = VI)
  - Resistance from resistivity

- **Thermodynamics Formulas**
  - Ideal Gas Law (PV = nRT)
  - Heat Capacity (Q = mcΔT)
  - Reynolds Number
  - Flow Rate

- **Physical Constants**
  - Gravitational acceleration, gas constant, speed of light, etc.

## Installation

### From local directory
```bash
uv pip install -e ./python-package
```

### From GitHub
```bash
uv pip install git+https://github.com/username/repo.git
```

### Traditional pip
```bash
pip install -e ./python-package
```

## Quick Start

### Temperature Conversions
```python
from engcalc.conversions import celsius_to_fahrenheit, fahrenheit_to_celsius

celsius_to_fahrenheit(100)  # 212.0
fahrenheit_to_celsius(32)   # 0.0
```

### Pressure Conversions
```python
from engcalc.conversions import psi_to_bar, bar_to_pascal

psi_to_bar(14.7)      # ~1.0135
bar_to_pascal(1.0)    # 100000.0
```

### Electrical Formulas
```python
from engcalc.formulas import ohms_law, electrical_power

# Calculate resistance: V = I × R
ohms_law(voltage=12, current=3)  # 4.0 ohms

# Calculate current
ohms_law(voltage=12, resistance=4)  # 3.0 amps

# Calculate power: P = V × I
electrical_power(voltage=12, current=2)  # 24.0 watts
```

### Thermodynamics Formulas
```python
from engcalc.formulas import ideal_gas_law, reynolds_number

# Ideal Gas Law: PV = nRT
temp = ideal_gas_law(
    pressure=101325,  # Pa
    volume=0.0224,    # m³
    moles=1,
    R=8.314
)  # ~273.15 K

# Reynolds Number: Re = (ρvD)/μ
re = reynolds_number(
    density=1000,     # kg/m³
    velocity=2,       # m/s
    diameter=0.1,     # m
    viscosity=0.001   # Pa·s
)  # 200000.0
```

### Physical Constants
```python
from engcalc.constants import (
    GRAVITY,
    GAS_CONSTANT,
    STANDARD_ATMOSPHERE,
    WATER_SPECIFIC_HEAT,
)

print(GRAVITY)              # 9.80665 m/s²
print(GAS_CONSTANT)         # 8.314 J/(mol·K)
print(STANDARD_ATMOSPHERE)  # 101325 Pa
```

## API Documentation

### Conversions Module

#### Temperature (`engcalc.conversions.temperature`)
- `celsius_to_fahrenheit(celsius: float) -> float`
- `fahrenheit_to_celsius(fahrenheit: float) -> float`
- `celsius_to_kelvin(celsius: float) -> float`
- `kelvin_to_celsius(kelvin: float) -> float`
- `fahrenheit_to_kelvin(fahrenheit: float) -> float`
- `kelvin_to_fahrenheit(kelvin: float) -> float`

#### Pressure (`engcalc.conversions.pressure`)
- `psi_to_bar(psi: float) -> float`
- `bar_to_psi(bar: float) -> float`
- `bar_to_pascal(bar: float) -> float`
- `pascal_to_bar(pascal: float) -> float`
- `pascal_to_kpa(pascal: float) -> float`
- `kpa_to_pascal(kpa: float) -> float`

#### Length (`engcalc.conversions.length`)
- `meters_to_feet(meters: float) -> float`
- `feet_to_meters(feet: float) -> float`
- `inches_to_meters(inches: float) -> float`
- `meters_to_inches(meters: float) -> float`
- `feet_to_inches(feet: float) -> float`
- `inches_to_feet(inches: float) -> float`

### Formulas Module

#### Electrical (`engcalc.formulas.electrical`)
- `ohms_law(voltage=None, current=None, resistance=None) -> float`
  - Provide any 2 parameters to calculate the third
- `electrical_power(voltage=None, current=None, power=None) -> float`
  - Provide any 2 parameters to calculate the third
- `resistance_from_resistivity(resistivity, length, area) -> float`

#### Thermodynamics (`engcalc.formulas.thermodynamics`)
- `ideal_gas_law(pressure=None, volume=None, moles=None, temperature=None, R=8.314) -> float`
  - Provide any 3 parameters to calculate the fourth
- `heat_capacity(mass, specific_heat, delta_temp) -> float`
- `reynolds_number(density, velocity, diameter, viscosity) -> float`
- `flow_rate(velocity, area) -> float`

## Design Principles

- **Zero Dependencies**: Pure calculation library with no external requirements
- **Src Layout**: Prevents import issues and follows modern Python packaging standards
- **Type Hints**: Fully typed with `py.typed` marker for type checkers
- **Educational**: Clear formulas in docstrings, realistic engineering examples
- **Installable from GitHub**: Can be installed directly from repository subdirectory

## Use Cases

This library is designed for:
- Engineering students learning Python
- Quick unit conversions in scripts
- Foundation for larger engineering applications
- Teaching modern Python packaging patterns