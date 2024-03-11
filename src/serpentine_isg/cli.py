"""Console script for serpentine_isg."""

import sys
from pathlib import Path

import click

from serpentine_isg import __version__
from serpentine_isg.serpentine_isg import process_file


@click.command()
@click.version_option(__version__, "--version", "-V")
@click.argument("input_file", type=click.Path(exists=True))
@click.option("--row", "orientation", flag_value="row", default=True)
@click.option("--col", "orientation", flag_value="column")
def main(input_file: str, orientation: str) -> None:
    """Console script for serpentine_isg."""
    process_file(Path(input_file), orientation)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
