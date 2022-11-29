# project4.py
#
# ICS 33 Fall 2022
# Project 4: Still Looking for Something


from classes.read_file import read_file
from pathlib import Path


def _read_input_file_path() -> Path:
    """Reads the input file path from the standard input"""
    return Path(input())


def main() -> None:
    """begin generate n sentences"""

    # CHECK1: check the input file path
    print("Please input your file path: ", end='')
    input_file_path = _read_input_file_path()
    try:
        G = read_file(input_file_path)
    except FileNotFoundError:
        print("File do not exist!")
        return

    # CHECK2: check the number of random_sentences
    try:
        number_of_random_sentences = int(
            input("Please input your expected number of random sentences: "))
        if number_of_random_sentences <= 0:
            raise ValueError
    except:
        print("Expect a positive integer!")
        return

    # CHECK3: begin generate from the Grammar
    name_of_start_variable = input(
        "Please input the name of your expected begin variable: ")
    try:
        # print("\nHere are series sentences generated from the Grammar in the file => ")
        G.generate_sentence(
            start_variable=name_of_start_variable,
            number_of_sentences=number_of_random_sentences
        )
    except:
        print("Invalid start variable name!")
        return


if __name__ == '__main__':
    main()
