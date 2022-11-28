# option.py
# We defined a class called Option

# an Option consists of Variable and Terminal, so it can be expressed as a list of Variable or Terminal
# It has a value means its weight, called option_weight

# We also define a function: generate_sentence(grammar_map) function
# * which accepts the grammar_map of file,
# * and then generates a series of sentences according to the Option

class Option:
    def __init__(self, weight_of_option: int, varlist_of_option: list) -> None:
        self.option_weight = weight_of_option
        self.option_varlist = varlist_of_option[:]

    def generate_sentence(self, grammar_map=None) -> str:
        """generate sentence from this Option
        Notice that element in option is class Variable or class Terminal
        Args:
            grammar_map (dict, optional): the grammar_map of file, Defaults to None.
        Returns:
            str: one sentence from this Option
        """
        return ' '.join([var.generate_sentence(grammar_map) for var in self.option_varlist])

    def _print(self):
        """_print function, help we to see what the Option is"""
        print("-------begin----------")
        print("weight = ", self.option_weight)
        for i in self.option_varlist:
            print("name = ", i.var_name)
        print("-------end----------")

