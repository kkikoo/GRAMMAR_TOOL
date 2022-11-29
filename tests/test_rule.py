# unit test of class rule
import unittest

from test_doubles.test_io import TestIO
from test_doubles.double_rule import DoubleRule
from test_doubles.double_read_file import test_double_of_read_file
from test_doubles.double_terminal_symbol import DoubleTerminal
from test_doubles.double_variable_symbol import DoubleVariable
from test_doubles.double_option import DoubleOption


class TestRule(unittest.TestCase):
    def test_rule_generate_sentence_with_test_txt(self):
        G = test_double_of_read_file(TestIO().TEST)
        o = DoubleOption(1, [DoubleTerminal("Bob"), DoubleTerminal(
            "is"), DoubleVariable("Adjective"), DoubleTerminal("today")])
        t = DoubleRule([o])
        self.assertEqual(t.generate_sentence(
            G.grammar_map), "Bob is happy today")


if __name__ == '__main__':
    unittest.main()

