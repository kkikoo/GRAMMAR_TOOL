# test_grammar.py
# unittest for the grammar.py

import unittest
import io
import contextlib

from test_doubles.test_io import TestIO
from test_doubles.double_read_file import test_double_of_read_file


class TestGrammar(unittest.TestCase):
    def test_the_file_from_teacher(self):
        number_of_random_sentences = 3
        name_of_start_variable = "HowIsBoo"

        class_grammar = test_double_of_read_file(TestIO().TEST)

        with contextlib.redirect_stdout(io.StringIO()) as output:
            class_grammar.generate_sentence(
                start_variable = name_of_start_variable,
                number_of_sentences = number_of_random_sentences
            )
            self.assertEqual(
                output.getvalue(),
                """Boo is happy today
Boo is happy today
Boo is happy today
"""
            )

    def test_the_file_from_grin(self):
        number_of_random_sentences = 3
        name_of_start_variable = "UnlabeledGrinStatement"

        class_grammar = test_double_of_read_file(TestIO().GRIN)

        with contextlib.redirect_stdout(io.StringIO()) as output:
            class_grammar.generate_sentence(
                start_variable = name_of_start_variable,
                number_of_sentences = number_of_random_sentences
            )
            self.assertEqual(
                output.getvalue(),
                """LET A A
LET A A
LET A A
"""
            )


if __name__ == "__main__":
    unittest.main()