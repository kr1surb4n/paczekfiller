# -*- coding: utf-8 -*-
import io
import os
import re

from setuptools import find_packages
from setuptools import setup


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding='utf-8') as fd:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), fd.read())


setup(
    name="paczekfiller",
    version="0.1.0",
    url="https://github.com/borntyping/cookiecutter-pypackage-minimal",
    license='MIT',

    author="Szemek Kot",
    author_email="przemyslaw.kot@gmail.com",

    description="Paczek filler - a template file filler, that  outputs rendered template to STDOUT",
    long_description=read("README.rst"),

    packages=find_packages(exclude=('tests', 'docs',)),

    install_requires=[],
    extras_require={
        'fzf':  ["fzf"],
    },
    scripts=['bin/paczek'],
    entry_points={'console_scripts': [
        'paczekfiller = paczekfiller.cli:main',
    ]},
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
