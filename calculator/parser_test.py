from parser import rpn
from lexer import lex


def test_basic():
    assert rpn(lex("1 1 +")) == [2]


def test_multi_level():
    assert rpn(lex("3 6 + 7 *")) == [63]


def test_subtraction():
    assert rpn(lex("6 3 -")) == [3]


def test_division():
    assert rpn(lex("9 3 /")) == [3]


def test_negative_answer():
    assert rpn(lex("5 8 -")) == [-3]


def test_negative_equation():
    assert rpn(lex("-5 8 +")) == [3]
