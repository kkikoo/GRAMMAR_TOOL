# double_rule.py

# We defined a class called DoubleRule, a test doubles of class Rule
# Notice that we change the result of random generate,
# just return the one from our given index

# a Rule consists a list of Option

# We also define a function: generate_sentence(grammar_map) function
# * which accepts the grammar_map of file,
# * then random select one option in the Rule,
# * and then generates a sentence according to the Rule

from test_doubles.double_option import DoubleOption


class DoubleRule:
    def __init__(self, option_list_of_rule: list[DoubleOption]) -> None:
        self.rule_option_list = option_list_of_rule[:]

        self.probability_list = []
        for idx, opt in enumerate(self.rule_option_list):
            self.probability_list.extend(
                [idx]*opt.option_weight
            )
        self.length = len(self.probability_list)

    def generate_sentence(self, grammar_map=None):
        """generate sentence from this Rule, first random select one option in the Rule,
            * then do the  generate_sentence(...) method of this Option.
        Args:
            grammar_map (dict, optional): the grammar_map of file, Defaults to None.
        Returns:
            str: one sentence from the Option which is random select from the Rule
        """

        select_option = self.rule_option_list[0]
        ans = []
        for each_var in select_option.option_varlist:
            ans.append(
                each_var.generate_sentence(grammar_map)
            )
        return ' '.join(ans)
