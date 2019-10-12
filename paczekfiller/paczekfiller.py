# -*- coding: utf-8 -*-
import sys
from paczekfiller import env, meta, erase_repository_path
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
        return input(self.message)

    def read(self):
        """Read the value and return it"""
        value = self.prompt()
        self.value = value
        return value


def template_object(template_name):
    """Return template object"""
    return env.get_template(template_name)


def template_content(template):
    """Read the contents of the template file"""
    with open(template.filename) as f:
        return f.read()


def extract_variables(template):
    """Extract variables to fill in"""
    contents = template_content(template)

    return meta.find_undeclared_variables(
        env.parse(contents))  # gives me a set


def context(template):
    """Fill out the context"""
    return {
        v.key: v.read()
        for v in (Variable(name) for name in extract_variables(template))
    }


def main_function(template_name):
    """Load the template, get values for variables
    and return it to stdout"""
    template_name = erase_repository_path(template_name)
    try:
        template = template_object(template_name)

        sys.stdout.write(template.render(context(template)))
    except TemplateNotFound:
        sys.stderr.write("No such template: %s" % template_name)

    except OSError:
        sys.stderr.write("Error loading template file")
    except Exception as e:
        sys.stderr.write("Unexptected exception %s" % e)


