# read_file.py

# we defined a function called read_file()
# * it read file and process it to a class Grammar
# * it return a class Grammar, combine all info of the file

from pathlib import Path
from classes.option import Option
from classes.grammar import Grammar
from classes.terminal_symbol import Terminal
from classes.variable_symbol import Variable


def read_file(filepath: Path) -> Grammar:
    """read file and process it to a class Grammar
    Args:
        filepath (Path): the file path
    Returns:
        a class Grammar, combine all info of the file
    """
    def process_option_line(option: list) -> Option:
        """process an option line
        Args:
            option (list): a string consists of [variable] and [terminal]
        Returns:
            Option: a class consists of a list  of Variable and Terminal
        """
        trans_option = []
        op_weight = int(option[0])
        for i in range(1, len(option)):
            if option[i][0] == '[':
                trans_option.append(
                    Variable(option[i][1:-1])
                )
            else:
                trans_option.append(
                    Terminal(option[i])
                )
        return Option(
            op_weight,
            trans_option[:]
        )

    """main of this function"""
    data = []
    index = 0
    index_of_left, index_of_right = [], []
    with open(filepath, "r") as fp:
        for line in fp.readlines():
            line = line.strip()
            if len(line) == 0:
                continue
            data.append(line)
            if line == "{":
                index_of_left.append(index)
            if line == "}":
                index_of_right.append(index)
            index += 1

    G = Grammar({})

