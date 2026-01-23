"""Engineering formula calculation commands."""

import click


@click.group()
def calc():
    """Calculate engineering formulas."""
    pass


@calc.command()
@click.option("--voltage", "-v", type=float, help="Voltage in Volts")
@click.option("--current", "-i", type=float, help="Current in Amperes")
@click.option("--resistance", "-r", type=float, help="Resistance in Ohms")
def ohms_law(voltage: float, current: float, resistance: float):
    """Calculate using Ohm's Law: V = I × R

    Provide any two of the three parameters to calculate the third.

    Examples:
        engcalc calc ohms-law --voltage 12 --current 3
        engcalc calc ohms-law -v 12 -r 4
        engcalc calc ohms-law -i 3 -r 4
    """
    provided = sum(x is not None for x in [voltage, current, resistance])

    if provided != 2:
        click.secho(
            "Error: Must provide exactly two of three parameters", fg="red", err=True
        )
        raise click.Abort()

    click.secho("Ohm's Law: V = I × R", fg="cyan")
    click.echo()

    if voltage is None:
        result = current * resistance
        click.echo(f"Given: I = {current} A, R = {resistance} Ω")
        click.secho(f"Voltage: {result} V", fg="green", bold=True)
    elif current is None:
        result = voltage / resistance
        click.echo(f"Given: V = {voltage} V, R = {resistance} Ω")
        click.secho(f"Current: {result} A", fg="green", bold=True)
    else:  # resistance is None
        result = voltage / current
        click.echo(f"Given: V = {voltage} V, I = {current} A")
        click.secho(f"Resistance: {result} Ω", fg="green", bold=True)


@calc.command()
@click.option("--voltage", "-v", type=float, help="Voltage in Volts")
@click.option("--current", "-i", type=float, help="Current in Amperes")
@click.option("--power", "-p", type=float, help="Power in Watts")
def power(voltage: float, current: float, power: float):
    """Calculate electrical power: P = V × I

    Provide any two of the three parameters to calculate the third.

    Examples:
        engcalc calc power --voltage 12 --current 2
        engcalc calc power -p 24 -i 2
        engcalc calc power -p 24 -v 12
    """
    provided = sum(x is not None for x in [voltage, current, power])

    if provided != 2:
        click.secho(
            "Error: Must provide exactly two of three parameters", fg="red", err=True
        )
        raise click.Abort()

    click.secho("Electrical Power: P = V × I", fg="cyan")
    click.echo()

    if power is None:
        result = voltage * current
        click.echo(f"Given: V = {voltage} V, I = {current} A")
        click.secho(f"Power: {result} W", fg="green", bold=True)
    elif voltage is None:
        result = power / current
        click.echo(f"Given: P = {power} W, I = {current} A")
        click.secho(f"Voltage: {result} V", fg="green", bold=True)
    else:  # current is None
        result = power / voltage
        click.echo(f"Given: P = {power} W, V = {voltage} V")
        click.secho(f"Current: {result} A", fg="green", bold=True)


@calc.command()
@click.option(
    "--density", "-d", type=float, required=True, help="Fluid density in kg/m³"
)
@click.option(
    "--velocity", "-v", type=float, required=True, help="Flow velocity in m/s"
)
@click.option(
    "--diameter",
    "-D",
    type=float,
    required=True,
    help="Characteristic length in meters",
)
@click.option(
    "--viscosity", "-m", type=float, required=True, help="Dynamic viscosity in Pa·s"
)
def reynolds(density: float, velocity: float, diameter: float, viscosity: float):
    """Calculate Reynolds number: Re = (ρvD)/μ

    Example:
        engcalc calc reynolds -d 1000 -v 2 -D 0.1 -m 0.001
    """
    result = (density * velocity * diameter) / viscosity

    click.secho("Reynolds Number: Re = (ρvD)/μ", fg="cyan")
    click.echo()
    click.echo(f"Density (ρ): {density} kg/m³")
    click.echo(f"Velocity (v): {velocity} m/s")
    click.echo(f"Diameter (D): {diameter} m")
    click.echo(f"Viscosity (μ): {viscosity} Pa·s")
    click.echo()
    click.secho(f"Reynolds Number: {result:.2f}", fg="green", bold=True)

    # Provide flow regime interpretation
    if result < 2300:
        click.secho("Flow regime: Laminar", fg="yellow")
    elif result < 4000:
        click.secho("Flow regime: Transitional", fg="yellow")
    else:
        click.secho("Flow regime: Turbulent", fg="yellow")


@calc.command()
@click.option("--pressure", "-p", type=float, help="Pressure in Pascals")
@click.option("--volume", "-v", type=float, help="Volume in cubic meters")
@click.option("--moles", "-n", type=float, help="Number of moles")
@click.option("--temperature", "-t", type=float, help="Temperature in Kelvin")
@click.option(
    "--gas-constant",
    "-R",
    type=float,
    default=8.314,
    help="Gas constant (default: 8.314 J/(mol·K))",
)
def ideal_gas(
    pressure: float,
    volume: float,
    moles: float,
    temperature: float,
    gas_constant: float,
):
    """Calculate using Ideal Gas Law: PV = nRT

    Provide any three of the four main parameters to calculate the fourth.

    Examples:
        engcalc calc ideal-gas -p 101325 -v 0.0224 -n 1
        engcalc calc ideal-gas -v 0.0224 -n 1 -t 273.15
    """
    provided = sum(x is not None for x in [pressure, volume, moles, temperature])

    if provided != 3:
        click.secho(
            "Error: Must provide exactly three of four parameters (P, V, n, T)",
            fg="red",
            err=True,
        )
        raise click.Abort()

    click.secho("Ideal Gas Law: PV = nRT", fg="cyan")
    click.echo(f"Gas constant R = {gas_constant} J/(mol·K)")
    click.echo()

    if pressure is None:
        result = (moles * gas_constant * temperature) / volume
        click.echo(f"Given: V = {volume} m³, n = {moles} mol, T = {temperature} K")
        click.secho(f"Pressure: {result:.2f} Pa", fg="green", bold=True)
    elif volume is None:
        result = (moles * gas_constant * temperature) / pressure
        click.echo(f"Given: P = {pressure} Pa, n = {moles} mol, T = {temperature} K")
        click.secho(f"Volume: {result:.6f} m³", fg="green", bold=True)
    elif moles is None:
        result = (pressure * volume) / (gas_constant * temperature)
        click.echo(f"Given: P = {pressure} Pa, V = {volume} m³, T = {temperature} K")
        click.secho(f"Moles: {result:.4f} mol", fg="green", bold=True)
    else:  # temperature is None
        result = (pressure * volume) / (moles * gas_constant)
        click.echo(f"Given: P = {pressure} Pa, V = {volume} m³, n = {moles} mol")
        click.secho(
            f"Temperature: {result:.2f} K ({result - 273.15:.2f} °C)",
            fg="green",
            bold=True,
        )
