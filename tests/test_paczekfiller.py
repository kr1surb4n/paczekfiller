import os
import sys
import pytest
import unittest
import tempfile

VARIABLE_NAME = "This_is_a_test_variable"
CONTENTS = """{{This_is_a_test_variable}}, yo!"""
TEXT = 'This is a test variable, yo!'


class TestVariable(unittest.TestCase):
    """Test Variable object.

    User input is not tested."""
    messages = [
       (
            'Some_nice_message',
            'Some nice message',
        ),
        (
            'Some',
            'Some',
        ),
        (
            '',
            '',
        ),
    ]

    def test_message(self):
        """Test for message formatting"""
        from paczekfiller.paczekfiller import make_variable
        for key, message in self.messages:
            with self.subTest():
                assert make_variable(key).message == message

    def test_read(self):
        """Test read function"""
        # mock prompt
        from paczekfiller.paczekfiller import make_variable
        os.environ['PACZEK_TEST'] = 'True'

        for key, message in self.messages:
            with self.subTest():
                assert make_variable(key).read() == message


class TestProcessingFunctions(unittest.TestCase):
    # test template filename
    template_file = 'tttt.txt.tpl'

    # output file path for cli test
    output_path = '/tmp/test_output'

    def setUp(self):
        self.folder = tempfile.mkdtemp()
        with open(os.path.join(self.folder, self.template_file), 'w') as f:
            f.write(CONTENTS)

    def tearDown(self):
        try:
            import glob
            for file in glob.glob(os.path.join(self.folder, '**')):
                try:
                    os.remove(file)
                except Exception:
                    pass
            os.rmdir(self.folder)
            os.remove(self.output_path)
        except OSError:
            pass

    def test_template_functions(self):
        from paczekfiller.paczekfiller import (
            template_content,
            extract_variables,
        )

        filepath = os.path.join(self.folder, self.template_file)

        contents = template_content(filepath)

        assert CONTENTS == contents, "Content loading"

        variables = extract_variables(contents)

        assert VARIABLE_NAME in variables, "Loading of variables"

    def test_main_function(self):
        """Test main_function"""
        from paczekfiller.paczekfiller import Variable, main_function
        Variable.read = lambda s: s.message

        path = os.path.join(self.folder, self.template_file)
        output = main_function(path)

        assert output == TEXT, "Main function test"

    def test_cli(self):
        """Test command line interface"""

        import subprocess
        from paczekfiller.paczekfiller import template_content

        # The base dir for Django's tests is one level up.
        tests_dir = os.path.dirname(os.path.dirname(__file__))
        path = os.path.join(self.folder, self.template_file)
        test_environ = os.environ.copy()
        test_environ['PACZEK_TEST'] = 'True'

        script = 'paczekfiller.cli'
        args = [
            path,
            self.output_path,
        ]

        # execute command
        p = subprocess.run(
            [sys.executable, '-m', script] + args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=tests_dir,
            env=test_environ,
            universal_newlines=True,
        )

        # p.stderr, p.stdout
        assert p.stderr == ''
        assert TEXT == template_content(self.output_path)
