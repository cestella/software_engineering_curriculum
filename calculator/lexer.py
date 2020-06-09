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

def convert(s):
    if '.' in s:
        return float(s)
    else:
        return int(s)

def lex(line):

    char_before = None
    char_after = None
    partial_num = None
    tokens = []
    
    for c in line:
        if c.isdigit() or c == ".":
            if c != line[-1]:
                # if it is not the first char
                if partial_num == None:
                    partial_num = str(c)
                    # adding this char to partial num
                    char_before = c
                else:
                    partial_num += str(c)
                 # updating char_before
                print("In the digit part: {}".format(partial_num))
            else:
                # if it is not the first char
                if partial_num == None:
                    partial_num = str(c)
                    # adding this char to partial num
                    char_before = c
                else:
                    partial_num += str(c)
                    # updating char_before
                print("In the digit part: {}".format(partial_num))
                tokens.append(convert(partial_num))
            
                    
        elif c == "-":
            if line[0] == c:
                partial_num = str(c)
            elif char_before.isdigit():
                tokens.append(c)
        elif c in ["+","*", "/"]:
            # if it is an operator or a space (spaces are ignored)
            print("In the op part: {}".format(partial_num))
            #tokens.append(convert(partial_num))
            #partial_num = None
            if type(partial_num) == "NoneType":
                tokens.append(partial_num)
            tokens.append(c)
            char_before = c

    return tokens

print(lex("-1.2*2"))
