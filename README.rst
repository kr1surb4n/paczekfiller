Pączek filler
============

.. image:: https://img.shields.io/pypi/v/paczekfiller.svg
    :target: https://pypi.python.org/pypi/paczekfiller
    :alt: Latest PyPI version

Script for filling out single Jinja2 templates. This tool tries to
fill in a space next to `cookiecutter`, giving the user ability to
reuse functionality across different projects in template files.

Please remember, redundancy can be removed and files can me merged
using git. 

Usage
-----

There are two commands:
- `paczek`
- `paczekfiller <template_filepath> <target_filepath>`

### paczekfiller

`paczekfiller` fills out a jinja2 template file and saves it under given target filepath.

`<template_filepath>` is an absolute path.


### paczek

`paczek` is a script that uses `fzf` to fill out a template in your template's folder and save it in current folder.

If a template file ends with `.tpl`, then it is passed to `paczekfiller`, with the output filename without the `.tpl` extension.

If template file is without `.tpl`, then it's copied to your current folder.

`PACZEK_FILINGS` environment variable stores path to that folder

### templates

Variables are extracted from templates. Variables names are
used in user prompt. The "_" are changed into spaces (" ").

So, for a variable `{{Some_variable}}`, script will prompt user with
this: `Some variable: `

Installation
------------

`pip install paczekfiller`

Requirements
^^^^^^^^^^^^

`fzf`

Licence
-------
MIT type.


Authors
-------

`paczekfiller` was written by `Oren (Przemyslaw Kot) <przemyslaw.kot@gmail.com>`_.
