from lexer import lex

# Uncomment these asserts when `lex` is complete.  Also, don't forget to remove
# the pass function body.


def test_basecase():
    # assert lex('1 + 1') == [ 1, '+', 1 ]
    pass


def test_negative_weirdness():
    # assert lex('1 - -1') == [ 1, '-', -1 ]
    pass


def test_no_space():
    # assert lex('-1.2*2') == [ -1.2, '*', 2 ]
    pass


def test_parens():
    # assert lex('(2 + 3) - 3.2') == [ '(', 2, '+', 3, ')', '-', 3.2 ]
    pass
