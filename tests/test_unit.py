import pytest
import unittest
from _pytest.monkeypatch import MonkeyPatch


class TestVariable(unittest.TestCase):
    messages = [
            ('Some_nice_message', 'Some nice message',),
            ('Some', 'Some',),
            ('', '',),
    ]

    def setUp(self):

        self.monkeypatch = MonkeyPatch

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
