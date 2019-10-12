# -*- coding: utf-8 -*-
import os
import sys
from paczekfiller import get_jinja_env, meta
from jinja2 import Template

DELIM = '_'
SPACE = ' '


class Variable:
    """Representation of the template variable
    that will handle the user input"""
    def __init__(self, variable_name):
        self.key = variable_name
        self.message = self.key.replace(DELIM, SPACE)
        self.value = None

    def prompt(self):
        """Ask user for value"""
        return self.message

    def read(self):
        """Read the value and return it"""
        value = self.prompt()
        self.value = value
        return value


class InteractiveVariable(Variable):
    def prompt(self):
        """Ask user for value"""
        return input(self.message + ": ")


def make_variable(name):
    if os.environ.get('PACZEK_TEST', False):
        return Variable(name)

    return InteractiveVariable(name)


def template_content(template_path):
    """Read the contents of the template file"""
    with open(template_path) as f:
        return f.read()


def extract_variables(content):
    """Extract variables to fill in"""
    env = get_jinja_env(content)

    return meta.find_undeclared_variables(env.parse(content))  # gives me a set


def context(template_content):
    """Fill out the context"""
    return {
        v.key: v.read()
        for v in
        [make_variable(name) for name in extract_variables(template_content)]
    }


def main_function(template_name):
    """Load the template, get values for variables
    and return it"""

    try:
        content = template_content(template_name)

        assert content

        template = Template(content)

        return template.render(context(content))
    except EOFError:
        sys.stderr.write("Error EOF")
    except OSError:
        sys.stderr.write("Error loading template file")
    except Exception as e:
        sys.stderr.write("Unexptected exception %s" % e)
