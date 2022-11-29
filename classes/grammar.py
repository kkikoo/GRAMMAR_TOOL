# grammar.py
# We defined a class called Grammar

# The Grammar class records all variable names and rules in the file
# * and combine them as a dictionary, grammar_map
# * the key of the map is Class Variable
# * the value of the map is Class Rule

# We also define a function: generate_sentence(start_variable, number_of_sentences) function
# * which accepts the name of start_variable,
# * the number of sentences expected to be output,
# * and then generates a series of sentences according to the rules


class Grammar:
    def __init__(self, map_of_grammar: dict) -> None:
        self.grammar_map = map_of_grammar

    def generate_sentence(self, start_variable: str, number_of_sentences: int):
        """generate sentence from grammar, with given start_variable and number_of_sentences
        Args:
            start_variable (str): the name of start_variable, such as "HowIsBoo"
            number_of_sentences (int): number_of_sentences, such as 10
        """
        try:
            rules = self.grammar_map[start_variable]
            for i in range(number_of_sentences):
                print(
                    rules.generate_sentence(self.grammar_map)
                )
        except:
            raise ValueError(
                "Do not have a variable named {}".format(start_variable))
