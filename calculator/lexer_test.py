from lexer import lex

# Uncomment these asserts when `lex` is complete.  Also, don't forget to remove
# the pass function body.


def test_basecase():
    assert lex("1 + 1") == [1, "+", 1]


def test_negative_weirdness():
    assert lex("1 - -1") == [1, "-", -1]


def test_no_space():
    assert lex("-1.2*2") == [-1.2, "*", 2]


def test_multiple_spaces():
    assert lex("1  + 1") == [1, "+", 1]


def test_parens():
    assert lex("(2 + 3) - 3.2") == ["(", 2, "+", 3, ")", "-", 3.2]


def test_RPN():
    assert lex("1 1 +") == [1, 1, "+"]

def test_RPN_with_spaces():
    assert lex("1  1 +") == [1, 1, "+"]
