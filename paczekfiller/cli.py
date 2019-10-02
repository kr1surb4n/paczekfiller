# -*- coding: utf-8 -*-

"""Console script for copypaster."""
import sys
import click

from paczekfiller.paczekfiller import main_function

@click.command()
@click.argument('template_name')
def main(template_name):
    """Console script for copypaster."""
    click.echo("Pączek is filled...")

    main_function(template_name)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
