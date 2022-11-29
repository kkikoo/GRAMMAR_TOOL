import unittest

from test_doubles.double_terminal_symbol import DoubleTerminal


class TestTerminal(unittest.TestCase):
    def test_hash(self):
        t = DoubleTerminal("Bob")
        self.assertEqual(hash(t), hash("Bob"))

    def test_equal(self):
        var1 = "Bob"
        self.assertEqual(DoubleTerminal("Bob"), var1)
        self.assertEqual(DoubleTerminal("Bob"), DoubleTerminal("Bob"))

    def test_generate_sentence(self):
        t = DoubleTerminal("Bob")
        self.assertEqual(t.generate_sentence(), "Bob")


if __name__ == '__main__':
    unittest.main()

