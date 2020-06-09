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
    stripped_line = line.replace(" ", "")
    print(stripped_line + " : " + line)
    
    for i in range(0, len(stripped_line)):
        c = stripped_line[i]
        if i != 0:
            char_before = stripped_line[i-1]
        else:
            char_before = None
        if i == len(stripped_line) - 1:
            char_after = None
        else:
            char_after = stripped_line[i+1]
        
        if c.isdigit() or c == ".":
            if partial_num == None:
                partial_num = str(c)
                    # adding this char to partial num
            else:
                partial_num += str(c)
                
            if char_after in ["+", "-", "*", "/"]:
                tokens.append(convert(partial_num))
                partial_num = None
            
            elif i == len(stripped_line) - 1:
                tokens.append(convert(partial_num))
                partial_num = None
                
                #print("In the digit part: {}".format(partial_num))
          
                    
        elif c == "-":
            if stripped_line[0] == c:
                partial_num = str(c)
            elif char_before.isdigit():
                tokens.append(c)
            elif char_before in ["+", "*", "-", "/"]:
                partial_num = c 
        elif c in ["+","*", "/"]:
            # if it is an operator or a space (spaces are ignored)
            #print("In the op part: {}".format(partial_num))
            tokens.append(c)

    return tokens

print(lex("1 - -1"))
print(lex("5.6 + 1"))
print(lex("-1.2*2"))
