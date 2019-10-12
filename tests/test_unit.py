import os
import sys
import pytest
import unittest
import tempfile
from unittest.mock import MagicMock, patch

VARIABLE_NAME="This_is_a_test_variable"
CONTENTS="""{{This_is_a_test_variable}}, yo!"""
TEXT='This is a test variable, yo!'


class TestVariable(unittest.TestCase):
    messages = [
            ('Some_nice_message', 'Some nice message',),
            ('Some', 'Some',),
            ('', '',),
    ]

    def setUp(self):
        os.environ['PACZEK_FILLINGS'] = '/tmp'
        from paczekfiller.paczekfiller import Variable
        self.Variable = Variable


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


class TestProcessingFunctions(unittest.TestCase):
    template_file = 'tttt.txt.tpl'

    def setUp(self):
        self.folder = tempfile.mkdtemp()
        with open(os.path.join(self.folder, self.template_file), 'w') as f:
            f.write(CONTENTS)

        os.environ.get = MagicMock(return_value=self.folder)
        os.environ['PACZEK_FILLINGS'] = self.folder
        from paczekfiller.paczekfiller import Variable
        self.Variable = Variable

    """
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
    """

    def test_template_functions(self):
        from paczekfiller.paczekfiller import template_content

        filepath = os.path.join(self.folder, self.template_file)

        assert CONTENTS == template_content(filepath)

    def test_extract_variables(self):
        from paczekfiller.paczekfiller import template_object, extract_variables

        template = template_object(self.template_file)

        variables = extract_variables(template)

        assert VARIABLE_NAME in variables


    def test_main_function(self):
        self.Variable.read = lambda s: s.message

        #from io import StringIO
        #with patch('sys.stdout', new_callable=StringIO) as mstdout:

        from paczekfiller.paczekfiller import main_function

        path = os.path.join(self.folder, self.template_file)
        output = main_function(path)

        assert output == TEXT
