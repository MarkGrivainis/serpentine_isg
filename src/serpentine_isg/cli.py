"""Console script for serpentine_isg."""

import sys
from pathlib import Path

import click

from serpentine_isg.serpentine_isg import process_file


@click.command()
@click.argument("input_file", type=click.Path(exists=True))
@click.option("--row", "orientation", flag_value="row", default=True)
@click.option("--column", "orientation", flag_value="column")
def main(input_file: str, orientation: str) -> None:
    """Console script for serpentine_isg."""
    process_file(Path(input_file), orientation)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
