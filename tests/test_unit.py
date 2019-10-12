import os
import sys
import pytest
import unittest
import tempfile
from unittest.mock import MagicMock, patch

VARIABLE_NAME="This_is_a_test_variable"
CONTENTS="""{{This_is_a_test_variable}}, yo!"""
TEXT='This is a test variable, yo!'

class PaczekTestCaseMixin(unittest.TestCase):
    messages = [
            ('Some_nice_message', 'Some nice message',),
            ('Some', 'Some',),
            ('', '',),
    ]

    folder = '/tmp'
    template_file = 'tttt.txt.tpl'

    @classmethod
    def setUpClass(self):
        self.folder = tempfile.mkdtemp()
        with open(os.path.join(self.folder, self.template_file), 'w') as f:
            f.write(CONTENTS)

        os.environ.get = MagicMock(return_value=self.folder)

    def setUp(self):
        from paczekfiller.paczekfiller import Variable
        self.Variable = Variable

class TestVariable(PaczekTestCaseMixin):

    def test_message(self):
        """Test for message formatting"""
        for key, message in self.messages:
            with self.subTest():
                 assert self.Variable(key).message == message

    def test_read(self):
        """Test read function"""
        # mock prompt
        self.Variable.prompt = lambda s: s.message

        for key, message in self.messages:
            with self.subTest():
                assert self.Variable(key).read() == message


class TestProcessingFunctions(PaczekTestCaseMixin):

    @classmethod
    def tearDownClass(self):
        try:
            import glob
            for file in glob.glob(os.path.join(self.folder, '**')):
                try:
                    os.remove(file)
                except Exception:
                    pass
            os.rmdir(self.folder)
        except OSError:
            pass


    def test_template_functions(self):
        from jinja2 import Template, TemplateNotFound
        from paczekfiller.paczekfiller import template_object, template_content

        template = template_object(self.template_file)
        assert isinstance(template, Template)

        with self.assertRaises(TemplateNotFound):
            template_object('i_don_exist.txt.tpl')


        assert CONTENTS == template_content(template)

    def test_extract_variables(self):
        from paczekfiller.paczekfiller import template_object, extract_variables

        template = template_object(self.template_file)

        variables = extract_variables(template)

        assert VARIABLE_NAME in variables


    def test_main_function(self):
        self.Variable.read = lambda s: s.message

        from io import StringIO
        with patch('sys.stdout', new_callable=StringIO) as mstdout:

            from paczekfiller.paczekfiller import main_function

            main_function(self.template_file)

            assert mstdout.getvalue() == TEXT
