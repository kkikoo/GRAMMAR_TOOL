import unittest

from test_doubles.double_variable_symbol import DoubleVariable
from test_doubles.double_read_file import test_double_of_read_file
from test_doubles.test_io import TestIO


class TestVariable(unittest.TestCase):
    def test_hash(self):
        t = DoubleVariable("Bob")
        self.assertEqual(hash(t), hash("Bob"))

    def test_equal(self):
        var1 = "Bob"
        self.assertEqual(DoubleVariable("Bob"), var1)
        self.assertEqual(DoubleVariable("Bob"), DoubleVariable("Bob"))

    def test_generate_sentence_with_test_txt(self):
        G = test_double_of_read_file(TestIO().TEST)
        t = DoubleVariable("HowIsBoo")
        self.assertEqual(t.generate_sentence(G.grammar_map), "Boo is happy today")

    def test_generate_sentence_with_grin_txt(self):
        G = test_double_of_read_file(TestIO().GRIN)

        t = DoubleVariable("UnlabeledGrinStatement")
        self.assertEqual(t.generate_sentence(G.grammar_map), 'LET A A')


if __name__ == '__main__':
    unittest.main()

