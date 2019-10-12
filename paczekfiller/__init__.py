# -*- coding: utf-8 -*-
import os
from jinja2 import Environment, meta, FileSystemLoader, select_autoescape
"""paczekfiller - An opinionated, minimal cookiecutter template for Python packages"""  # noqa

__version__ = '0.1.0'
__author__ = 'Szemek Kot <przemyslaw.kot@gmail.com>'
__all__ = ['REPOSITORY', 'loader', 'env', 'meta', 'erase_repository_path']

def get_jinja_env():
    
    loader = FileSystemLoader(REPOSITORY, followlinks=True)

    env = Environment(loader=loader, autoescape=select_autoescape(['html', 'xml']))
    return env, 
