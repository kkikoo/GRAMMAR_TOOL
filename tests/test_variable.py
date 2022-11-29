import random
import unittest
from pathlib import Path

from classes.variable_symbol import Variable
from classes.read_file import read_file


class TestTerminal(unittest.TestCase):
    def test_hash(self):
        t = Variable("Bob")
        self.assertEqual(hash(t), hash("Bob"))

    def test_equal(self):
        var1 = "Bob"
        self.assertEqual(Variable("Bob"), var1)
        self.assertEqual(Variable("Bob"), Variable("Bob"))

    def test_generate_sentence_with_test_txt(self):
        path = Path("../test_data/test.txt")
        G = read_file(path)
        t = Variable("HowIsBoo")
        random.seed(99)
        self.assertEqual(t.generate_sentence(G.grammar_map), "Boo is relaxing today")

    def test_generate_sentence_with_grin_txt(self):
        path = Path("../test_data/grin.txt")
        G = read_file(path)
        t = Variable("UnlabeledGrinStatement")
        random.seed(99)
        self.assertEqual(t.generate_sentence(G.grammar_map), 'DIV G "F"')


if __name__ == '__main__':
    unittest.main()
