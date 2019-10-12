# -*- coding: utf-8 -*-
import sys
from paczekfiller import get_jinja_env, meta, erase_repository_path
from jinja2 import TemplateNotFound

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
        return input(self.message + ": ")

    def read(self):
        """Read the value and return it"""
        value = self.prompt()
        self.value = value
        return value


def template_content(template_path):
    """Read the contents of the template file"""
    with open(template_path) as f:
        return f.read()


def extract_variables(content):
    """Extract variables to fill in"""
    env = get_jinja_env()

    return meta.find_undeclared_variables(
        env.parse(contents))  # gives me a set


def context(template):
    """Fill out the context"""
    return {
        v.key: v.read()
        for v in [Variable(name) for name in extract_variables(template)]
    }


def main_function(template_name):
    """Load the template, get values for variables
    and return it"""

    try:
        content = template_content(template_name)

        template = Template(content)

        return template.render(context(template))
    except TemplateNotFound:
        sys.stderr.write("No such template: %s" % template_name)

    except OSError:
        sys.stderr.write("Error loading template file")
    except Exception as e:
        sys.stderr.write("Unexptected exception %s" % e)


