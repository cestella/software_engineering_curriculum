BINARY_OPERATORS = ["+", "-", "*", "/"]


def binary_operator(num_1, num_2, op):
    """
    Evaluates and acts on different binary operators

    Parameters
    ----------
    num_1 : integer
        The first number to be operated on
    
    num_2 : integer
        The second number to be operated on
    
    op : char
        The operator that is going to be applied to the numbers

    Returns
    -------
    integer : The final answer after after the nums are operated on
    """

    if op == "+":
        return num_1 + num_2

    elif op == "-":
        return num_2 - num_1

    elif op == "*":
        return num_1 * num_2

    elif op == "/":
        return num_2 / num_1


def push(e, stack):
    """
    Pushes the element (e) to the given stack

    Parameters
    ----------
    e : element
        The element to be pushed on top of the stack

    stack : list
        The stack that e is going to be pushed onto

    Returns
    -------
    list : The stack that is now updated to have e pushed ontop of it
    """
    return stack.append(e)


def pop(stack):
    """
    Retrieves the last element from the given stack and deletes it

    Parameters
    ----------
    stack : list
        The stack (in list form) to be operated on

    Returns
    -------
    stack : The popped stack
    """
    return stack.pop()


def is_numeric_token(token):
    """
    Says whether or not the token input is a number

    Parameter
    ---------
    token : token
        The token to be evalueated

    Returns
    -------
    bool: Whether or not this token is a numeric character
    """

    if type(token) == float or type(token) == int:
        return True

    else:
        return False


def rpn(tokens):
    """
    Parses RPN and returns an answer

    Parameters
    ----------
    tokens : list
        list of tokens

    Returns
    -------
    rpn_stack : list containing 1 element (the answer)
    """
    # Stack used to evaluate the token list (tokens)
    rpn_stack = []

    # Iterating through each index in tokens
    for i in range(0, len(tokens)):

        current_char = tokens[i]

        if is_numeric_token(current_char):
            # Adding the current character (which is a number) to the rpn stack to be operated on

            push(current_char, rpn_stack)

        elif current_char in BINARY_OPERATORS:
            # First number to be operated on is being taken from the stack
            first_num = pop(rpn_stack)
            # Second number to be operated on is being token from the stack
            second_num = pop(rpn_stack)
            # The awnser of the equation using the binary_operator() function
            answer = binary_operator(first_num, second_num, current_char)
            # Adding the answer to the stack
            push(answer, rpn_stack)

    # If the rpn_stack has only one element (that element would be the answer)
    if len(rpn_stack) == 1:
        # Ending the loop and returning the stack with the answer
        return rpn_stack
