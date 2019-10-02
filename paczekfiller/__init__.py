"""paczekfiller - An opinionated, minimal cookiecutter template for Python packages"""

__version__ = '0.1.0'
__author__ = 'Szemek Kot <przemyslaw.kot@gmail.com>'
__all__ = ['REPOSITORY', 'loader', 'env', 'meta']

PACZEK_FILLINGS = 'PACZEK_FILLINGS'

import os
from jinja2 import Environment, meta, FileSystemLoader, select_autoescape


REPOSITORY = os.environ[PACZEK_FILLINGS]

loader = FileSystemLoader(REPOSITORY, followlinks=True)

env = Environment(
    loader=loader,
    autoescape=select_autoescape(['html', 'xml'])
)
