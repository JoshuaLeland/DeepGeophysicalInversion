import unittest
from mockito import when, mock, unstub

class TestStringMethods(unittest.TestCase):

    def test_inversion_trainer(self):
        self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()