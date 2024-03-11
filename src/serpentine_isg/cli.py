"""Console script for serpentine_isg."""

import sys
import click


@click.command()
def main(args=None):
    """Console script for serpentine_isg."""
    click.echo("Replace this message by putting your code into "
               "serpentine_isg.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
