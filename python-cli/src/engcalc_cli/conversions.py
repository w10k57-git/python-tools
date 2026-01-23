"""Unit conversion commands."""

import click


@click.group()
def convert():
    """Convert between different units."""
    pass


@convert.command()
@click.argument("value", type=float)
@click.option(
    "--from",
    "from_unit",
    required=True,
    type=click.Choice(["celsius", "fahrenheit", "kelvin"], case_sensitive=False),
)
@click.option(
    "--to",
    "to_unit",
    required=True,
    type=click.Choice(["celsius", "fahrenheit", "kelvin"], case_sensitive=False),
)
def temperature(value: float, from_unit: str, to_unit: str):
    """Convert temperature between Celsius, Fahrenheit, and Kelvin.

    Examples:
        engcalc convert temperature 100 --from celsius --to fahrenheit
        engcalc convert temperature 32 --from fahrenheit --to celsius
        engcalc convert temperature 273.15 --from kelvin --to celsius
    """
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit == to_unit:
        click.echo(f"{value} {from_unit}")
        return

    # Convert to celsius first
    if from_unit == "celsius":
        celsius = value
    elif from_unit == "fahrenheit":
        celsius = (value - 32) * 5 / 9
    else:  # kelvin
        celsius = value - 273.15

    # Convert from celsius to target
    if to_unit == "celsius":
        result = celsius
    elif to_unit == "fahrenheit":
        result = (celsius * 9 / 5) + 32
    else:  # kelvin
        result = celsius + 273.15

    click.secho(f"{value} {from_unit} = ", fg="cyan", nl=False)
    click.secho(f"{result:.2f} {to_unit}", fg="green", bold=True)


@convert.command()
@click.argument("value", type=float)
@click.option(
    "--from",
    "from_unit",
    required=True,
    type=click.Choice(["psi", "bar", "pascal", "kpa"], case_sensitive=False),
)
@click.option(
    "--to",
    "to_unit",
    required=True,
    type=click.Choice(["psi", "bar", "pascal", "kpa"], case_sensitive=False),
)
def pressure(value: float, from_unit: str, to_unit: str):
    """Convert pressure between PSI, Bar, Pascal, and kPa.

    Examples:
        engcalc convert pressure 14.7 --from psi --to bar
        engcalc convert pressure 1 --from bar --to pascal
        engcalc convert pressure 100000 --from pascal --to kpa
    """
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit == to_unit:
        click.echo(f"{value} {from_unit}")
        return

    # Convert to pascal first
    if from_unit == "pascal":
        pascal = value
    elif from_unit == "bar":
        pascal = value * 100000
    elif from_unit == "psi":
        pascal = value * 0.0689476 * 100000
    else:  # kpa
        pascal = value * 1000

    # Convert from pascal to target
    if to_unit == "pascal":
        result = pascal
    elif to_unit == "bar":
        result = pascal / 100000
    elif to_unit == "psi":
        result = pascal / 100000 / 0.0689476
    else:  # kpa
        result = pascal / 1000

    click.secho(f"{value} {from_unit} = ", fg="cyan", nl=False)
    click.secho(f"{result:.4f} {to_unit}", fg="green", bold=True)


@convert.command()
@click.argument("value", type=float)
@click.option(
    "--from",
    "from_unit",
    required=True,
    type=click.Choice(["meters", "feet", "inches"], case_sensitive=False),
)
@click.option(
    "--to",
    "to_unit",
    required=True,
    type=click.Choice(["meters", "feet", "inches"], case_sensitive=False),
)
def length(value: float, from_unit: str, to_unit: str):
    """Convert length between meters, feet, and inches.

    Examples:
        engcalc convert length 1 --from meters --to feet
        engcalc convert length 12 --from inches --to feet
        engcalc convert length 3.28 --from feet --to meters
    """
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit == to_unit:
        click.echo(f"{value} {from_unit}")
        return

    # Convert to meters first
    if from_unit == "meters":
        meters = value
    elif from_unit == "feet":
        meters = value / 3.28084
    else:  # inches
        meters = value * 0.0254

    # Convert from meters to target
    if to_unit == "meters":
        result = meters
    elif to_unit == "feet":
        result = meters * 3.28084
    else:  # inches
        result = meters / 0.0254

    click.secho(f"{value} {from_unit} = ", fg="cyan", nl=False)
    click.secho(f"{result:.4f} {to_unit}", fg="green", bold=True)
