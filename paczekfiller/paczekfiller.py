import os
import sy
from paczekfiller import env, meta

DELIM = '_'

class Variable:
    """Representation of the template variable
    that will handle the user input"""

    def __init__(self, variable_name):
        self.key = variable_name
        self.message = self.key.split(DELIM)

        self.prompt()

    def prompt():
        """Ask user for value"""
        return input(self.message)

    def read():
        """Read the value and return it"""
        value = self.prompt()

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

    return meta.find_undeclared_variables(env.parse(contents)) # gives me a set

def context():
    """Fill out the context"""
    return { v.key: v.read() for v in (Variable(name) for name in extract_variables())}

def main_function(template_name):
    """Load the template, get values for variables
    and return it to stdout"""
    template = template_object(template_name)

    sys.stdout.write(template.render(context()))
