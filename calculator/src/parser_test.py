from src.parser import rpn
from src.lexer import lex


def test_basic():
    assert rpn(lex("1 1 +")) == 1 + 1


def test_multi_level():
    assert rpn(lex("3 6 + 7 *")) == (3 + 6) * 7


def test_subtraction():
    assert rpn(lex("6 3 -")) == 6 - 3


def test_division():
    assert rpn(lex("9 3 /")) == 9 / 3


def test_negative_answer():
    assert rpn(lex("5 8 -")) == 5 - 8


def test_negative_number():
    assert rpn(lex("-5 8 +")) == -5 + 8


def test_float_answer():
    assert rpn(lex("5 8 + 7 /")) == (5 + 8) / 7


def test_fraction():
    assert rpn(lex("1 5 + 7 /")) == (1 + 5) / 7


def test_float_number():
    assert rpn(lex("7 3 - 7.0 /")) == (7 - 3) / 7.0


def test_negative_division():
    assert rpn(lex("-5 3 + 2 /")) == (-5 + 3) / 2


def test_negative_and_float_division():
    assert rpn(lex("-5 3.0 + 2 /")) == (-5 + 3.0) / 2


def test_non_math_operator():
    try:
        rpn(lex("3 4 op"))
    except ValueError:
        pass
    else:
        raise ValueError("Expected exception, but it didn't raise")


def test_no_operator():
    try:
        rpn(lex("3 5"))
    except ValueError:
        pass
    else:
        raise ValueError("Expected exception, bit it didnt raise")
