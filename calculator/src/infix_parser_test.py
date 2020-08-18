from src.parser import rpn
from src.lexer import lex
from src.parser import infix


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


def test_num():
    assert rpn(infix(lex("1"))) == 1


def test_decimal():
    assert rpn(infix(lex("5.0"))) == 5.0


def test_negative():
    assert rpn(infix(lex("-5"))) == -5


def test_negative_decimal():
    assert rpn(infix(lex("-5.0")))


def test_multiple_levels():
    assert rpn(infix(lex("(4 + 2) / 3 * 5"))) == (4 + 2) / 3 * 5


def test_complex_mult():
    assert rpn(infix(lex("5 * ( 1 + 2) * 1"))) == (5 * (1 + 2) * 1)


def test_complex_division():
    assert rpn(infix(lex("5 * ( 1 + 2) / 1"))) == (5 * (1 + 2) / 1)


def test_left_to_right():
    assert rpn(infix(lex("10 * 4 / 8"))) == (10 * 4 / 8)
