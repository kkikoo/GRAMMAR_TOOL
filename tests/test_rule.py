import random
import unittest

from pathlib import Path

from classes.read_file import read_file
from classes.rule import Rule
from classes.terminal_symbol import Terminal
from classes.variable_symbol import Variable
from classes.option import Option


class TestRule(unittest.TestCase):
    def test_rule_generate_sentence_with_test_txt(self):
        path = Path("../test_data/test.txt")
        G = read_file(path)
        o = Option(1, [Terminal("Bob"), Terminal("is"), Variable("Adjective"), Terminal("today")])
        t = Rule([o])
        random.seed(99)
        self.assertEqual(t.generate_sentence(G.grammar_map), "Bob is relaxing today")


if __name__ == '__main__':
    unittest.main()
