ops = ["+", "-", "*", "/"]
ops_without_subtraction = ["+", "*", "/"]


def is_numeric_char(char):
    """
    is_numeric_char checks if a char is a number or a decimal point.
    Input: char 
    Output: True or False
    """
    if char.isdigit() or char == ".":
        return True
    else:
        return False


def convert_string(s):
    """Convert_string function converts a string to a float or a int, depending on whether it has a decimal point or not
       Input: s (Type: String)
       Output: float or int conversion of  "s"
"""
    if "." in s:
        return float(s)
    else:
        return int(s)


def is_op(char):
    """is_op fuction figures out whether the input is an operator
       Input: char (Type: String)
       Output: True/False (Type: Boolean)
    """
    if char in ops:
        return True
    else:
        return False


def is_op_not_subtract(char):
    """is_op_not_subtract is the same as is_op() but it excludes subtraction ("-")
       Input: char (Type: String)
       Output: True/False
    """
    if char in ops_without_subtraction:
        return True
    else:
        return False


def is_parenthesis(char):
    """is_parenthesis() checks if a char is a parenthesis
       Input: char (Type: String)
       Output: True/False
"""
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

    # Defining char_before and char_after
    char_before = None
    char_after = None
    # Partial_num is the var that stores my nums until I have to append it to my tokens list
    partial_num = None
    # List that stores the tokens
    tokens = []
    # Stripping the input line of spaces
    stripped_line = line

    # Iterating through each index in my stripped_line
    for i in range(0, len(stripped_line)):
        # Defining "c" as the char at the index "i" in stripped_line
        c = stripped_line[i]
        # Defining char_before but if i is the first index then the index will be invalid
        if i != 0:
            # Char_before is the current char's index (i), but subtracting 1 because it is 1 before
            char_before = stripped_line[i - 1]
        else:
            # if i is the first index then char_before is None
            char_before = None

        # Catching the same error as the first if statement but if i is the last index
        if i != len(stripped_line) - 1:
            # Char_after is the current char's index (i), but adding 1 because it is 1 after
            char_after = stripped_line[i + 1]
        else:
            # If i is the last index then char_after is None
            char_after = None
        # If c (current char), is a digit or a decimal point. If c is a int or a float:
        if is_numeric_char(c):
            # If c is the first iteration:
            if partial_num == None:
                # Partial_num is equal to c instead of partial_num is the original value but c added on.
                partial_num = str(c)
            else:
                partial_num += str(c)
            # If the char_after is a operator or a parenthesis:
            if (
                is_op(char_after)
                or is_parenthesis(char_after)
                or char_after == " "
                or i == len(stripped_line) - 1
            ):
                # If this condition is true then we know that the number or decimal is done.
                tokens.append(convert_string(partial_num))
                # Then we have to reset partial_num.
                partial_num = None
                # We do the same as the above if statement, if it is the end of the line.

        elif c == "-":
            # If it is the first char in the line:
            if i == 0:
                # If it is the first char then we know it is part of a number because a subtraction sign is a binary operator and it takes 2 params.
                partial_num = str(c)
            # If the char_before is a digit or a parenthisis
            elif (
                char_before.isdigit()
                or is_parenthesis(char_before)
                or char_after == " "
            ):
                # If the char_before is a digit or a parenthisis then we know that it is a subtraction operator because if it is a digit then it would be, "5-5" and that is a subtraction, also, "5-(5+5)" then it is a subtraction.
                tokens.append(c)
            elif is_op(char_before) or char_before == " ":
                # If the char_before is an operator then we know it is part of a number
                partial_num = c

        elif is_op_not_subtract(c):
            # Add the operator to the tokens list
            tokens.append(c)

        elif is_parenthesis(c):
            # Add parenthisis to the tokens list
            tokens.append(c)

    return tokens
