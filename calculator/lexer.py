def lex(line):
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
      * "/" - Division
    * The following grouping symbols are supported:
      * "("
      * ")"
    """
    char_before = None
    partial_num = None
    tokens = []
    
    for c in line:
        if c.is_digit() or c == ".":
            if partial_num == None:
                partial_num = c
            else:
                partial_num += c

   
print(lex("56 + 5"))

def lex_2(line):
    
    char_before = None
    char_after = None
    partial_num = None
    tokens = []

    for c in line:
        if c.isdigit() or partial_num == ".":
                # if it is not the first char
                if partial_num == None:
                    partial_num = str(c)
                # adding this char to partial num
                char_before = c 
                # updating char_before
                print('In the digit part: {}'.format(partial_num))
        elif c in ["+", "-", "*", "/"] or c == " ":
            # if it is an operator or a space (spaces are ignored)
            print('In the op part: {}'.format(partial_num))
            print(partial_num)
            if type(partial_num) == "NoneType":
                tokens.append(partial_num)
            # restarting partial_num so that it appends to the token list
            print(partial_num)
            if c == " ":
                tokens.append(str(partial_num))
                partial_num = None
            elif c in ["+", "*", "/", "-"]:
                if c in ["+", "*", "/"]:
                    tokens.append(c)
                elif c == "-":
                    if char_before == None:
                        partial_num += str(c)
                    elif char_before == " " or char_before.isdigit():
                        tokens.append(partial_num)
    return tokens


