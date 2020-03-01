# -*- coding: utf-8 -*-
import os
import sys
from paczekfiller import get_jinja_env, meta
from jinja2 import Template

DELIM = '_'
SPACE = ' '


def main_function(template_file):
    """Load the template, get values for variables
    and return it"""

    try:
        content = load(template_file
        assert content, "Couldn't load template"

        template = Template(content)

        return template.render(context(content))
    except EOFError:
        sys.stderr.write("Error EOF")
    except OSError:
        sys.stderr.write("Error loading template file")
    except Exception as e:
        sys.stderr.write("Unexptected exception %s" % e)


def load(template):
    """Read the contents of the template file"""
    with open(template) as f:
        return f.read()


def make_variable(name):
    if os.environ.get('PACZEK_TEST', False):
        return Variable(name)

    return InteractiveVariable(name)


def extract_variables(content: str) -> set:
    """Extract variables to fill in"""
    env = get_jinja_env(content)

    return meta.find_undeclared_variables(env.parse(content))


def context(template):
    """Create template context from
    variables used in the template.

    Fill them out interactively using
    `InteractiveVariable`s
    """

    return {
        v.key: v.read()
        for v in
        [make_variable(name) for name in extract_variables(template)]
    }


class Variable:
    """Representation of the template variable
    that will handle the user input"""
    def __init__(self, variable_name):
        self.key = variable_name
        self.message = self.key.replace(DELIM, SPACE)
        self.value = None

    def prompt(self):
        """Ask user for value"""
        return self.message.strip()

    def read(self):
        """Read the value and return it"""
        value_from_cli = self.prompt()

        self.value = value_from_cli
        return value_from_cli


class InteractiveVariable(Variable):
    def prompt(self):
        """Ask user for value"""
        return input(self.message + ": ").strip()
