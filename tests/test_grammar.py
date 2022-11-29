# test_main.py
# unittest for the project4.py

import random
import unittest
import io
import contextlib
from project4 import *


class TestMain(unittest.TestCase):
    def test_the_file_from_teacher(self):
        path = Path("../test_data/test.txt")
        number_of_random_sentences = 10
        name_of_start_variable = "HowIsBoo"

        class_grammar = read_file(path)

        random.seed(99)

        with contextlib.redirect_stdout(io.StringIO()) as output:
            class_grammar.generate_sentence(
                start_variable=name_of_start_variable,
                number_of_sentences=number_of_random_sentences
            )
            self.assertEqual(
                output.getvalue(),
                """Boo is relaxing today
Boo is excited today
Boo is perfect today
Boo is happy today
Boo is perfect today
Boo is excited today
Boo is excited today
Boo is perfect today
Boo is excited today
Boo is perfect today
"""
            )

    def test_the_file_from_grin(self):
        path = Path("../test_data/grin.txt")
        number_of_random_sentences = 10
        name_of_start_variable = "UnlabeledGrinStatement"

        class_grammar = read_file(path)

        random.seed(99)

        with contextlib.redirect_stdout(io.StringIO()) as output:
            class_grammar.generate_sentence(
                start_variable=name_of_start_variable,
                number_of_sentences=number_of_random_sentences
            )
            self.assertEqual(
                output.getvalue(),
                """DIV G "F"
PRINT Y
LET X 8
GOSUB 7 
DIV Z 6
PRINT 10
PRINT W
GOSUB 5 
LET R N
PRINT "C"
"""
            )


if __name__ == "__main__":
    unittest.main()
