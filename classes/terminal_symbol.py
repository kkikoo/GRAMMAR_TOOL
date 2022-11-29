# Terminal_symbol.py
# We defined a class called Terminal

# a Terminal is just a string, here we rewrite the __hash__() method for this class

# We also define a function: generate_sentence(grammar_map) function
# * which accepts the grammar_map of file,
# * and then return the var_name in this class


class Terminal:
    def __init__(self, name_of_var: str) -> None:
        self.var_name = name_of_var

    def __eq__(self, __o) -> bool:
        """check if self == __o
        Args:
            __o (str or Terminal): the one who need to compare with self
        Returns:
            bool: True if self == __o else False
        """
        if type(__o) == str:
            return self.var_name == __o
        elif isinstance(__o, Terminal):
            return self.var_name == __o.var_name
        else:
            return False

    def __hash__(self) -> int:
        """make the class hashable
        Returns:
            int: the hash value of the string in class
        """
        return hash(self.var_name)

    def generate_sentence(self, grammar_map = None) -> str:
        """generate sentence from this Terminal
        Args:
            grammar_map (dict, optional): the grammar_map of file, Defaults to None.
        Returns:
            str: the var_name in this class
        """
        return self.var_name

