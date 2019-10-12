# -*- coding: utf-8 -*-
"""Console script for copypaster."""
import sys
import click

from paczekfiller.paczekfiller import main_function


@click.command()
@click.argument('output_filename')
@click.argument('template_name')
def main(template_name, output_filename):
    """Console script for copypaster."""

    output = main_function(template_name)

    output_filename

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
