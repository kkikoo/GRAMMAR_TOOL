import unittest
from classes.terminal_symbol import Terminal


class TestTerminal(unittest.TestCase):
    def test_hash(self):
        t = Terminal("Bob")
        self.assertEqual(hash(t), hash("Bob"))

    def test_equal(self):
        var1 = "Bob"
        self.assertEqual(Terminal("Bob"), var1)
        self.assertEqual(Terminal("Bob"), Terminal("Bob"))

    def test_generate_sentence(self):
        t = Terminal("Bob")
        self.assertEqual(t.generate_sentence(), "Bob")


if __name__ == '__main__':
    unittest.main()
