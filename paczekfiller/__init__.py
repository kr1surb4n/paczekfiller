# -*- coding: utf-8 -*-
from jinja2 import Environment, meta, select_autoescape
"""Pączek filler - simple script for filling out single template files."""  # noqa

__version__ = '0.1.0'
__author__ = 'Kris Urbanski <kris@whereibend.space>'
__all__ = [
    'get_jinja_env',
    'meta',
]


def get_jinja_env(template_content):
    """Load environment object
    you don't need any loader for parse function
    loader = DictLoader({'template': template_content})
    """

    return Environment(autoescape=select_autoescape(['html', 'xml']))
