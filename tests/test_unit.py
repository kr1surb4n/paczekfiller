import pytest
from paczekfiller.paczekfiller import Variable

class TestVariable:

    def setUp(self):
        self.messages = [
            ('Some_nice_message', 'Some nice message',),
            ('Some', 'Some',),
            ('', '',),
        ]


    def test_message(self):
        """Test for message formatting"""
        for key, message in self.messages:
            with self.subTest():
                assert Variable(key).message == message

    def test_read(self):
        raise NotImplemented("No trza skończyć"):
