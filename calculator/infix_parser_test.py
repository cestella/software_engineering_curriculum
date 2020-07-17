from parser import rpn
from lexer import lex
from parser import infix


def test_basic():
    assert rpn(infix(lex("1 + 1"))) == (1 + 1)


def test_multi_level():
    assert rpn(infix(lex("(3 + 6) * 7"))) == (3 + 6) * 7


def test_subtraction():
    assert rpn(infix(lex("6 - 3"))) == 6 - 3


def test_division():
    assert rpn(infix(lex("9 / 3"))) == 9 / 3


def test_negative_answer():
    assert rpn(infix(lex("5 - 8"))) == 5 - 8


def test_negative_number():
    assert rpn(infix(lex("-5 + 8"))) == -5 + 8


def test_float_answer():
    assert rpn(infix(lex("(5 + 8) / 7"))) == (5 + 8) / 7


def test_fraction():
    assert rpn(infix(lex("(1 + 5) / 7"))) == (1 + 5) / 7


def test_float_number():
    assert rpn(infix(lex("(7 - 3) / 7.0"))) == (7 - 3) / 7.0


def test_negative_division():
    assert rpn(infix(lex("(-5 + 3) / 2"))) == (-5 + 3) / 2


def test_negative_and_float_division():
    assert rpn(infix(lex("(-5 + 3.0) / 2"))) == (-5 + 3.0) / 2


def test_non_math_operator():
    try:
        rpn(infix(lex("3 4 op")))
    except ValueError:
        pass
    else:
        raise ValueError("Expected exception, but it didn't raise")


def test_no_operator():
    try:
        rpn(infix(lex("3 5")))
    except ValueError:
        pass
    else:
        raise ValueError("Expected exception, bit it didnt raise")