"""Main CLI entry point for engcalc."""

import click

from engcalc_cli.conversions import convert
from engcalc_cli.formulas import calc


@click.group()
@click.version_option(version="0.1.0", prog_name="engcalc")
def cli():
    """Engineering calculations command-line tool.

    Convert units and calculate engineering formulas.
    """
    pass


# Register command groups
cli.add_command(convert)
cli.add_command(calc)


if __name__ == "__main__":
    cli()
