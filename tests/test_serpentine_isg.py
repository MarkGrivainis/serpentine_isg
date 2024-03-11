"""Tests for `serpentine_isg` package."""

from click.testing import CliRunner
from serpentine_isg import __version__, cli
from serpentine_isg.serpentine_isg import Data, column_sort, row_sort


def test_command_line_interface() -> None:
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ["--version"])
    assert result.exit_code == 0
    assert f"version {__version__}" in result.output
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert "--help         Show this message and exit." in help_result.output


class TestSerpentineIsg:
    """Test serpentine_isg."""

    header = ("source start", "source end", "target start", "target end", "value")

    def test_row_orientation(self: "TestSerpentineIsg") -> None:
        """Test row orientation."""
        values = [(0, 0, x, y, 0) for x in range(1, 4) for y in range(1, 4)]
        data = Data(self.header, values, row_sort)
        new_values = data.sort()
        transformed_coords = [(x[2], x[3]) for x in new_values]
        expected_coords = [
            (1, 1),
            (1, 2),
            (1, 3),
            (2, 3),
            (2, 2),
            (2, 1),
            (3, 1),
            (3, 2),
            (3, 3),
        ]
        assert expected_coords == transformed_coords

    def test_column_orientation(self: "TestSerpentineIsg") -> None:
        """Test column orientation."""
        values = [(0, 0, x, y, 0) for x in range(1, 4) for y in range(1, 4)]
        data = Data(self.header, values, column_sort)
        new_values = data.sort()
        transformed_coords = [(x[2], x[3]) for x in new_values]
        expected_coords = [
            (1, 1),
            (2, 1),
            (3, 1),
            (3, 2),
            (2, 2),
            (1, 2),
            (1, 3),
            (2, 3),
            (3, 3),
        ]
        assert expected_coords == transformed_coords
