"""Tests for `serpentine_isg` package."""

from click.testing import CliRunner
from serpentine_isg import cli, serpentine_isg


def test_command_line_interface() -> None:
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert "serpentine_isg.cli.main" in result.output
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert "--help  Show this message and exit." in help_result.output


def test_serpentine_isg() -> None:
    """Test serpentine_isg."""
    assert serpentine_isg(0, 0, 0, 0, 0)
