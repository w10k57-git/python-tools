"""Tests for CLI formula calculation commands."""

from click.testing import CliRunner
from engcalc_cli.main import cli


class TestOhmsLaw:
    """Test Ohm's Law CLI commands."""

    def setup_method(self):
        self.runner = CliRunner()

    def test_calculate_resistance(self):
        result = self.runner.invoke(
            cli, ["calc", "ohms-law", "--voltage", "12", "--current", "3"]
        )
        assert result.exit_code == 0
        assert "4" in result.output

    def test_calculate_current(self):
        result = self.runner.invoke(cli, ["calc", "ohms-law", "-v", "12", "-r", "4"])
        assert result.exit_code == 0
        assert "3" in result.output

    def test_missing_parameters(self):
        result = self.runner.invoke(cli, ["calc", "ohms-law", "--voltage", "12"])
        assert result.exit_code != 0


class TestPower:
    """Test electrical power CLI commands."""

    def setup_method(self):
        self.runner = CliRunner()

    def test_calculate_power(self):
        result = self.runner.invoke(
            cli, ["calc", "power", "--voltage", "12", "--current", "2"]
        )
        assert result.exit_code == 0
        assert "24" in result.output


class TestReynolds:
    """Test Reynolds number CLI command."""

    def setup_method(self):
        self.runner = CliRunner()

    def test_calculate_reynolds(self):
        result = self.runner.invoke(
            cli,
            ["calc", "reynolds", "-d", "1000", "-v", "2", "-D", "0.1", "-m", "0.001"],
        )
        assert result.exit_code == 0
        assert "200000" in result.output
        assert "Turbulent" in result.output


class TestIdealGas:
    """Test Ideal Gas Law CLI command."""

    def setup_method(self):
        self.runner = CliRunner()

    def test_calculate_temperature(self):
        result = self.runner.invoke(
            cli, ["calc", "ideal-gas", "-p", "101325", "-v", "0.0224", "-n", "1"]
        )
        assert result.exit_code == 0
        assert "272" in result.output or "273" in result.output
