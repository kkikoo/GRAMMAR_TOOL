# GRAMMAR_TOOL
实现一个Grammar解析器，根据Grammar规则生成语句

思路分析：

定义Grammar: 一系列的替换规则，将含有Variable的句子转化为Terminal

Sentence Generator 算法:
1. 从只有一个Variable的Sentence开始
2. 选一个Variable，在对应的替换规则中pick一个 3. Repeat，直到没有Variable剩下

• A grammar contains a collection of rules.

• Each rule is made up of a variable and one or more options.

• Each option has a weight and a sequence of symbols, each of which is a terminal or a variable.


• A class representing a terminal symbol.

• A class representing a variable symbol.

• A class representing an option.

• A class representing a rule.

• A class representing a grammar.
