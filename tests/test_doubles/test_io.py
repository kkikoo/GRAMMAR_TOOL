# test_io.py
# hardcode some test case and use them to do our unit-test
# The info of file from Grin.txt and Test.txt from our teacher

import io

GRIN = """grin.txt
ICS 33 Fall 2022
Project 4: Still Looking for Something

An example grammar for generating Grin syntax.  For example, when using the
variable GrinStatement as the start variable, it will generate a random,
but syntactically valid, Grin statement.


{
LetStatement
1 LET [Variable] [Value]
}


{
PrintStatement
1 PRINT [Value]
}


{
InNumStatement
1 INNUM [Variable]
}


{
InStrStatement
1 INSTR [Variable]
}


{
AddStatement
1 ADD [Variable] [Value]
}


{
SubStatement
1 SUB [Variable] [Value]
}


{
MultStatement
1 MULT [Variable] [Value]
}


{
DivStatement
1 DIV [Variable] [Value]
}


{
GotoStatement
1 GOTO [Target] [Condition]
}


{
GosubStatement
1 GOSUB [Target] [Condition]
}


{
ReturnStatement
1 RETURN
}


{
EndStatement
1 END
}


{
Condition
4 
1 IF [Value] [Operator] [Value]
}


{
GrinStatement
1 [Label] [UnlabeledGrinStatement]
5 [UnlabeledGrinStatement]
}


{
UnlabeledGrinStatement
10 [LetStatement]
5 [PrintStatement]
2 [InNumStatement]
2 [InStrStatement]
2 [AddStatement]
2 [SubStatement]
2 [MultStatement]
2 [DivStatement]
5 [GotoStatement]
5 [GosubStatement]
5 [ReturnStatement]
1 [EndStatement]
}


{
Label
1 A:
1 B:
1 C:
1 D:
1 E:
1 F:
1 G:
1 H:
1 I:
1 J:
1 K:
1 L:
1 M:
1 N:
1 O:
1 P:
1 Q:
1 R:
1 S:
1 T:
1 U:
1 V:
1 W:
1 X:
1 Y:
1 Z:
}


{
Variable
1 A
1 B
1 C
1 D
1 E
1 F
1 G
1 H
1 I
1 J
1 K
1 L
1 M
1 N
1 O
1 P
1 Q
1 R
1 S
1 T
1 U
1 V
1 W
1 X
1 Y
1 Z
}


{
Value
1 [Variable]
1 [LiteralInteger]
1 [LiteralString]
}


{
LiteralInteger
1 0
1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10
}


{
LiteralString
1 "A"
1 "B"
1 "C"
1 "D"
1 "E"
1 "F"
1 "G"
1 "H"
1 "I"
1 "J"
1 "K"
1 "L"
1 "M"
1 "N"
1 "O"
1 "P"
1 "Q"
1 "R"
1 "S"
1 "T"
1 "U"
1 "V"
1 "W"
1 "X"
1 "Y"
1 "Z"
}


{
Target
5 [LiteralInteger]
1 [LiteralString]
1 [Variable]
}


{
Operator
1 =
1 <>
1 <
1 <=
1 >
1 >=
}
"""

TEST = """{
HowIsBoo
1 Boo is [Adjective] today
}

{
Adjective
3 happy
3 perfect
1 relaxing
1 fulfilled
2 excited
}
"""

class TestIO:
    def __init__(self) -> None:
        self.GRIN = io.StringIO(GRIN)
        self.TEST = io.StringIO(TEST)

