def lex(s):
    """
    A lexer is a function which takes a string and turns it into a list of
    tokens.  For the purpose of our calculator, we want to create a
    function called `lex` in `lexer.py` with takes an argument `line` and
    returns a list of tokens of the correct type like so:
    * Numbers are converted to the correct type (e.g. "1.2" is the float `1.2` whereas "1" is the int `1`)
    * Do not rely on spaces to separate tokens (e.g. "-1.2*2" is a valid
      input string and should return the list `[ -1.2, '*', 2 ]`
    * The following operations are supported:
      * "*" - Multiplication
      * "+" - Addition
      * "-" - Subtraction
    * The following grouping symbols are supported:
      * "("
      * ")"
    """
   return []
