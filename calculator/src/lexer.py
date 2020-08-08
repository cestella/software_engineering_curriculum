OPS = ["+", "-", "*", "/"]
OPS_WITHOUT_SUBTRACTION = ["+", "*", "/"]


def is_numeric_char(char):
    """
        Determines if a character is a numeric character (i.e. a character which may appear in a number).

        Parameters
        ----------
        char : char
            The character to be evaluated

        Returns
        -------
        bool: Whether or not this character is a numeric character.
    """
    return char.isdigit() or char == "."


def convert_string(s):
    """
        Converts a string to the appropriate type, either a float type or a int type

        Parameters
        ----------
        s : string
            The string that should be converted
        
        Returns
        -------
        float or int : The numerical representation of "s"
    """
    if "." in s:
        return float(s)
    else:
        return int(s)


def is_op(char):
    """  
        Checks if a char is an operator

        Parameters
        ----------
        char : char
            The character that is going to be checked

        Returns
        -------
        bool : Whether or not char is an operator
    """

    return char in OPS


def is_op_not_subtract(char):
    """
        Checks whether a char is an operator that is not subtraction

        Parameters
        ----------
        char : char
            The charactere that is going to be checked

        Returns
        -------
        bool: Whether the character is an operator
    """
    return char in OPS_WITHOUT_SUBTRACTION


def is_parenthesis(char):
    """
        Checks whether a char is a parenthesis 

        Parameters
        ----------
        char : char
        The charactere that is going to be checked

        Returns
        -------
        bool: Whether the character is a parenthesis
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

    Parameters
    ----------
    line : string
        The line to be lexed

    Returns
    -------
    list: list of tokens
    """

    # Defining char_before and char_after
    char_before = None
    char_after = None
    # Partial_num is the var that stores my nums until I have to append it to my tokens list
    partial_num = None
    # List that stores the tokens
    tokens = []
    # Stripping the input line of spaces
    stripped_line = line.strip()

    # Iterating through each index in my stripped_line
    for i in range(0, len(stripped_line)):
        # Defining "c" as the char at the index "i" in stripped_line
        c = stripped_line[i]
        # Defining is_first_iteration:
        is_first_iteration = i == 0
        # Defining char_before but if i is the first index then the index will be invalid
        if not is_first_iteration:
            char_before = stripped_line[i - 1]
        else:
            char_before = None

        # Catching the index error if i is the last iteration:
        if i != len(stripped_line) - 1:
            char_after = stripped_line[i + 1]
        else:
            # If i is the last index then char_after is None
            char_after = None

        if is_numeric_char(c):
            # If c is the first iteration:
            if partial_num == None:
                partial_num = str(c)
            else:
                partial_num += str(c)

            if (
                is_op(char_after)  # If we see an op afterwards
                or is_parenthesis(char_after)  # or if we see a parenthesis after
                or char_after == " "  # or if we see a space afterwards
                or i == len(stripped_line) - 1  # or if it is the last char
            ):
                # If this condition is true then we know that the number or decimal is done.
                tokens.append(convert_string(partial_num))
                partial_num = None

        elif c == "-":
            # Negative signs are a problem, because they can be part of a
            # number, OR they can be a subtraction sign. I am going to use
            # the following series of checks to differentiate them:
            # 1. If it is the first character then it is a negative sign.
            # 2. If the char before is a digit or a parenthesis then there must be no spaces, and if it is after, then it must be operating on that num.
            # 3. If the char_before is an operator or a space then it must be part of the number
            # 4. If the char before is a "(" then it is a negative sign

            if is_first_iteration:
                # If it is the first char then we know it is part of a number because a subtraction sign is a binary operator and it takes 2 params.
                partial_num = str(c)

            elif i == len(stripped_line) - 1:
                tokens.append(c)

            elif char_before == "(":
                partial_num = str(c)

            elif is_first_iteration == False:
                # If the char_before is a digit or a parenthisis or the char_after is a space
                if (
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
