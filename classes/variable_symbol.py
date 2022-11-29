# Variable_symbol.py
# We defined a class called Variable

# a Variable can represent any string or sentences
# * here we rewrite the __hash__() method for this class

# We also define a function: generate_sentence(grammar_map) function
# * which accepts the grammar_map of file,
# * and then get the rule of this Variable
# * finally we do the generate_sentence(grammar_map) method of this rule


class Variable:
    def __init__(self, name_of_var) -> None:
        self.var_name = name_of_var

    def __eq__(self, __o) -> bool:
        """check if self == __o
        Args:
            __o (str or Variable): the one who need to compare with self
        Returns:
            bool: True if self == __o else False
        """
        if type(__o) == str:
            return self.var_name == __o
        elif isinstance(__o, Variable):
            return self.var_name == __o.var_name
        else:
            return False

    def __hash__(self) -> int:
        """make the class hashable
        Returns:
            int: the hash value of the var_name in class
        """
        return hash(self.var_name)

    def generate_sentence(self, grammar_map) -> str:
        """generate sentence from this Terminal
        Args:
            grammar_map (dict, optional): the grammar_map of file, Defaults to None.
        Returns:
            str: the result of generate_sentence(grammar_map) method of the rule map to this Variable
        """
        rule_of_var = grammar_map[self.var_name]
        _ = rule_of_var.generate_sentence(grammar_map)
        return _