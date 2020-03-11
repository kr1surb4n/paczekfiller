import unittest

from unittest.mock import patch, MagicMock
from tests.conftest import template_variables

from hypothesis import given, example

from paczekfiller.paczekfiller import Variable


class TestVariable(unittest.TestCase):
    """Test Variable object."""

    @given(template_variables())
    def test_message(self, variables):
        """Test for message formatting

        GIVEN variable name is 'text_text'
        WHEN Variable object is initiated with such string
        THEN Variable.message will contain string 'text text'
        """
        assert Variable(variables[0]).message == variables[1]

    @given(variables=template_variables())
    def test_read(self, variables):
        """Test read function
        """

        mock = MagicMock(return_value=variables[1].strip())
        with patch('builtins.input', mock):
            assert Variable(variables[0]).read() == variables[1].strip()


class TestProcessingFunctions(unittest.TestCase):
    template = "{{Example_Value}} is {{Another_Value}}"
    template_output = "Example Value is Another Value"

    def test_extract_variables(self):
        from paczekfiller.paczekfiller import extract_variables

        value_bag = extract_variables(self.template)

        assert len(value_bag) == 2
        assert 'Example_Value' in value_bag

    def test_context(self):
        from paczekfiller.paczekfiller import Variable, context

        Variable.read = lambda s: s.message

        ctx = context(self.template)

        assert len(ctx) == 2
        assert ctx['Example_Value'] == 'Example Value'

    def test_main_function(self):
        """Test main_function"""
        from paczekfiller.paczekfiller import Variable, main_function

        Variable.read = lambda s: s.message

        mock = MagicMock(return_value=self.template)
        with patch('paczekfiller.paczekfiller.load', mock):

            output = main_function('not_important_in_this_test')
            assert output == self.template_output