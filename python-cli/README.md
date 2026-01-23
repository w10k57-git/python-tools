# engcalc-cli - Engineering Calculations CLI

A command-line tool for quick engineering calculations and unit conversions. Built with Click for an intuitive interface with colorful, formatted output.

## Features

- **Unit Conversions**: Temperature, pressure, and length conversions
- **Engineering Formulas**: Ohm's Law, electrical power, Reynolds number, Ideal Gas Law
- **Colorful Output**: Rich terminal formatting with color-coded results
- **Intuitive CLI**: Command groups, short flags, helpful error messages

## Installation

### Install as a tool (recommended)
```bash
cd python-cli
uv tool install .
```

This installs `engcalc` in an isolated environment and makes it globally available.

### Install in current project
```bash
uv add engcalc-cli --editable python-cli
```

### Traditional pip
```bash
pip install ./python-cli
```

## Quick Start

### Get Help
```bash
engcalc --help
engcalc convert --help
engcalc calc --help
```

### Temperature Conversions
```bash
# Celsius to Fahrenheit
engcalc convert temperature 100 --from celsius --to fahrenheit
# Output: 100 celsius = 212.00 fahrenheit

# Fahrenheit to Celsius
engcalc convert temperature 32 --from fahrenheit --to celsius
# Output: 32 fahrenheit = 0.00 celsius

# Celsius to Kelvin
engcalc convert temperature 25 --from celsius --to kelvin
# Output: 25 celsius = 298.15 kelvin
```

### Pressure Conversions
```bash
# PSI to Bar
engcalc convert pressure 14.7 --from psi --to bar
# Output: 14.7 psi = 1.0135 bar

# Bar to Pascal
engcalc convert pressure 1 --from bar --to pascal
# Output: 1 bar = 100000.0000 pascal

# Pascal to kPa
engcalc convert pressure 100000 --from pascal --to kpa
# Output: 100000 pascal = 100.0000 kpa
```

### Length Conversions
```bash
# Meters to Feet
engcalc convert length 1 --from meters --to feet
# Output: 1 meters = 3.2808 feet

# Feet to Inches
engcalc convert length 5 --from feet --to inches
# Output: 5 feet = 60.0000 inches

# Inches to Meters
engcalc convert length 39.37 --from inches --to meters
# Output: 39.37 inches = 1.0000 meters
```

## Formula Calculations

### Ohm's Law (V = I × R)
Provide any two parameters to calculate the third.

```bash
# Calculate resistance
engcalc calc ohms-law --voltage 12 --current 3
# Output: Resistance: 4 Ω

# Calculate current (using short flags)
engcalc calc ohms-law -v 12 -r 4
# Output: Current: 3 A

# Calculate voltage
engcalc calc ohms-law -i 3 -r 4
# Output: Voltage: 12 V
```

### Electrical Power (P = V × I)
```bash
# Calculate power
engcalc calc power --voltage 12 --current 2
# Output: Power: 24 W

# Calculate voltage
engcalc calc power -p 24 -i 2
# Output: Voltage: 12 V

# Calculate current
engcalc calc power -p 24 -v 12
# Output: Current: 2 A
```

### Reynolds Number (Re = ρvD/μ)
```bash
engcalc calc reynolds \
  --density 1000 \
  --velocity 2 \
  --diameter 0.1 \
  --viscosity 0.001

# Output:
# Reynolds Number: Re = (ρvD)/μ
#
# Density (ρ): 1000 kg/m³
# Velocity (v): 2 m/s
# Diameter (D): 0.1 m
# Viscosity (μ): 0.001 Pa·s
#
# Reynolds Number: 200000.00
# Flow regime: Turbulent

# Using short flags
engcalc calc reynolds -d 1000 -v 2 -D 0.1 -m 0.001
```

### Ideal Gas Law (PV = nRT)
Provide any three parameters to calculate the fourth.

```bash
# Calculate temperature
engcalc calc ideal-gas \
  --pressure 101325 \
  --volume 0.0224 \
  --moles 1

# Output: Temperature: 273.15 K (0.00 °C)

# Calculate volume
engcalc calc ideal-gas -p 101325 -n 1 -t 273.15
# Output: Volume: 0.022400 m³

# Using custom gas constant
engcalc calc ideal-gas -p 101325 -v 0.0224 -n 1 --gas-constant 8.314
```

## Command Reference

### Conversion Commands

```bash
engcalc convert temperature <value> --from <unit> --to <unit>
  Units: celsius, fahrenheit, kelvin

engcalc convert pressure <value> --from <unit> --to <unit>
  Units: psi, bar, pascal, kpa

engcalc convert length <value> --from <unit> --to <unit>
  Units: meters, feet, inches
```

### Formula Commands

```bash
engcalc calc ohms-law [--voltage V] [--current I] [--resistance R]
  Short flags: -v, -i, -r
  Provide any 2 of 3 parameters

engcalc calc power [--voltage V] [--current I] [--power P]
  Short flags: -v, -i, -p
  Provide any 2 of 3 parameters

engcalc calc reynolds --density D --velocity V --diameter D --viscosity M
  Short flags: -d, -v, -D, -m
  All parameters required

engcalc calc ideal-gas [options]
  Options: --pressure, --volume, --moles, --temperature, --gas-constant
  Short flags: -p, -v, -n, -t, -R
  Provide any 3 of 4 main parameters (P, V, n, T)
```

## Design Features

- **Click Framework**: Industry-standard CLI framework with great UX
- **Command Groups**: Organized into `convert` and `calc` subcommands
- **Rich Output**: Colored, formatted terminal output for better readability
- **Entry Points**: Installed as `engcalc` command via `[project.scripts]`
- **Independent Logic**: Self-contained calculations (doesn't depend on python-package)
- **Error Handling**: Clear error messages for invalid input

## Use Cases

- Quick unit conversions in terminal workflows
- Engineering calculations without opening Python REPL
- Teaching tool for CLI application development
- Integration into shell scripts and automation
