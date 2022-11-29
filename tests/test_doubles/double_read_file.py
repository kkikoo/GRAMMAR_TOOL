# double_read_file.py
# test doubles of function read_file(...)
# Notice that, to help we do unittest, we change the args of this function
# * from Path to StingIo

from test_doubles.double_rule import DoubleRule
from test_doubles.double_option import DoubleOption
from test_doubles.double_grammar import DoubleGrammar
from test_doubles.double_terminal_symbol import DoubleTerminal
from test_doubles.double_variable_symbol import DoubleVariable


def test_double_of_read_file(file_stream) -> DoubleGrammar:
    """read file and process it to a class Grammar
    Args:
        file_stream: stringIo object
    Returns:
        a class Grammar, combine all info of the file
    """
    def process_option_line(option: list) -> DoubleOption:
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
                    DoubleVariable(option[i][1:-1])
                )
            else:
                trans_option.append(
                    DoubleTerminal(option[i])
                )
        return DoubleOption(
            op_weight,
            trans_option[:]
        )

    """main of this function"""
    data = []
    index = 0
    index_of_left, index_of_right = [], []
    fp = file_stream
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


    G = DoubleGrammar({})

    for (L, R) in zip(index_of_left, index_of_right):
        var_name = data[L+1:R][0]

        option_list = [e.split(' ') for e in data[L+1:R][1:]]
        option_list = [process_option_line(e) for e in option_list]

        r = DoubleRule(option_list)
        v = DoubleVariable(var_name)
        G.grammar_map[v] = r

    return G