
#Function to convert a string to an int or a float depending on which one is appropriate
def convert(s):
    #If there is a decimal point it is a float so we
    if "." in s:
        return float(s)
    else:
        return int(s)

#If the char is an operator
def is_op(char):
    if char in ["+", "-", "*", "/"]:
        return True
    else:
        return False

#If the char is an operator but not subtraction
def is_op_not_subtract(char):
    if char in ["+", "*", "/"]:
        return True
    else:
        return False
#If the char is a parenthisis
def is_parenthisis(char):
    if char in ["(", ")"]:
        return True
    else:
        return False

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
    
    #Defining char_before and char_after
    char_before = None
    char_after = None
    #Partial_num is the var that stores my nums until I have to append it to my tokens list
    partial_num = None
    #List that stores the tokens
    tokens = []
    #Stripping the input line of spaces
    stripped_line = line.replace(" ", "")
    
    #Iterating through each index in my stripped_line
    for i in range(0, len(stripped_line)):
        #Defining "c" as the char at the index "i" in stripped_line
        c = stripped_line[i]
        #Defining char_before but if i is the first index then the index will be invalid
        if i != 0:
            #Char_before is the current char's index (i), but subtracting 1 because it is 1 before
            char_before = stripped_line[i - 1]
        else:
            #if i is the first index then char_before is None
            char_before = None
    
        #Catching the same error as the first if statement but if i is the last index
        if i != len(stripped_line) - 1:
            #Char_after is the current char's index (i), but adding 1 because it is 1 after
            char_after = stripped_line[i+1]
        else:
            #If i is the last index then char_after is None
            char_after = None
        #If c (current char), is a digit or a decimal point. If c is a int or a float: 
        if c.isdigit() or c == ".":
            #If c is the first iteration:
            if partial_num == None:
                #Partial_num is equal to c instead of partial_num is the original value but c added on.
                partial_num = str(c)
                # adding this char to partial num
            else:
                partial_num += str(c)
            #If the char_after is a operator or a parenthesis:
            if is_op(char_after) == True or is_parenthisis(char_after) == True:
                #If this condition is true then we know that the number or decimal is done.
                tokens.append(convert(partial_num))
                #Then we have to reset partial_num.
                partial_num = None
            #We do the same as the above if statement, if it is the end of the line.
            elif i == len(stripped_line) - 1:
                tokens.append(convert(partial_num))
                partial_num = None

        #If c is a negative sign or a subtraction operator:
        elif c == "-":
            #If it is the first char in the line:
            if stripped_line[0] == c:
                #If it is the first char then we know it is part of a number because a subtraction sign is a binary operator and it takes 2 params.
                partial_num = str(c)
            #If the char_before is a digit or a parenthisis
            elif char_before.isdigit() or is_parenthisis(char_before) == True:
                #If the char_before is a digit or a parenthisis then we know that it is a subtraction operator because if it is a digit then it would be, "5-5" and that is a subtraction, also, "5-(5+5)" then it is a subtraction. 
                tokens.append(c)
            #If the char_before is a operator:
            elif is_op(char_before) == True:
                #If the char_before is an operator then we know it is part of a number
                partial_num = c
        # if c is an operator:
        elif is_op_not_subtract(c) == True:
            #Add the operator to the tokens list
            tokens.append(c)
        # if c is a parenthisis:
        elif is_parenthisis(c) == True:
            #Add parenthisis to the tokens list
            tokens.append(c)

    return tokens


print(lex("1 - -1"))
print(lex("5.6 + 1"))
print(lex("-1.2*(2-1)"))
print(lex("(2 + 3) - 3.2"))
