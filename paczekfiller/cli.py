# -*- coding: utf-8 -*-
"""Command line function."""
import sys
import click

from paczekfiller.paczekfiller import main_function


def write(filename, contents):
    with open(filename, 'w') as file:
        file.write(contents)


@click.command()
@click.argument('template_name')
@click.argument('output_filename')
def main(output_filename, template_name):
    """Console script for Pączek filler."""

    contents = main_function(template_name)

    write(output_filename, contents)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
