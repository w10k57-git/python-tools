"""Tests for CLI conversion commands."""

from click.testing import CliRunner
from engcalc_cli.main import cli


class TestTemperatureConversion:
    """Test temperature conversion CLI commands."""

    def setup_method(self):
        self.runner = CliRunner()

    def test_celsius_to_fahrenheit(self):
        result = self.runner.invoke(
            cli,
            [
                "convert",
                "temperature",
                "100",
                "--from",
                "celsius",
                "--to",
                "fahrenheit",
            ],
        )
        assert result.exit_code == 0
        assert "212.00" in result.output

    def test_fahrenheit_to_celsius(self):
        result = self.runner.invoke(
            cli,
            ["convert", "temperature", "32", "--from", "fahrenheit", "--to", "celsius"],
        )
        assert result.exit_code == 0
        assert "0.00" in result.output

    def test_celsius_to_kelvin(self):
        result = self.runner.invoke(
            cli, ["convert", "temperature", "0", "--from", "celsius", "--to", "kelvin"]
        )
        assert result.exit_code == 0
        assert "273.15" in result.output


class TestPressureConversion:
    """Test pressure conversion CLI commands."""

    def setup_method(self):
        self.runner = CliRunner()

    def test_bar_to_pascal(self):
        result = self.runner.invoke(
            cli, ["convert", "pressure", "1", "--from", "bar", "--to", "pascal"]
        )
        assert result.exit_code == 0
        assert "100000" in result.output

    def test_psi_to_bar(self):
        result = self.runner.invoke(
            cli, ["convert", "pressure", "14.7", "--from", "psi", "--to", "bar"]
        )
        assert result.exit_code == 0
        assert "1.0" in result.output


class TestLengthConversion:
    """Test length conversion CLI commands."""

    def setup_method(self):
        self.runner = CliRunner()

    def test_feet_to_inches(self):
        result = self.runner.invoke(
            cli, ["convert", "length", "1", "--from", "feet", "--to", "inches"]
        )
        assert result.exit_code == 0
        assert "12" in result.output

    def test_meters_to_feet(self):
        result = self.runner.invoke(
            cli, ["convert", "length", "1", "--from", "meters", "--to", "feet"]
        )
        assert result.exit_code == 0
        assert "3.28" in result.output
