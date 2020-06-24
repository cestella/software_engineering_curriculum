BINARY_OPERATORS = ["+", "-", "*", "/"]


def binary_operator(lhs, rhs, op):
    """
    Evaluates and acts on different binary operators

    Parameters
    ----------
    lhs : integer or float
        The first number to be operated on, will be on the left hand side of the op
    
    rhs : integer or float
        The second number to be operated on, will be on the right hand side of the op
    
    op : string
        The operator that is going to be applied to the numbers

    Returns
    -------
    integer : The final answer after after the nums are operated on
    """

    if op == "+":
        return lhs + rhs

    elif op == "-":
        return lhs - rhs

    elif op == "*":
        return lhs * rhs

    elif op == "/":
        return lhs / rhs
    else:
        raise ValueError(
            "The operator you used: {} is not supported, please try another one!".format(
                op
            )
        )


def push(e, stack):
    """
    Pushes the element (e) to the given stack, which mutates the stack

    Parameters
    ----------
    e : element
        The element to be pushed on top of the stack

    stack : list
        The stack that e is going to be pushed onto

    """
    return stack.append(e)


def pop(stack):
    """
    Retrieves the last element from the given stack and deletes it, which mutates it

    Parameters
    ----------
    stack : list
        The stack (in list form) to be operated on
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

    return type(token) == float or type(token) == int


def rpn(tokens):
    """
    Parses RPN and returns an answer

    Parameters
    ----------
    tokens : list
        list of tokens

    Returns
    -------
    answer : the answer to the equation 
    """
    # Stack used to evaluate the token list (tokens)
    rpn_stack = []

    # Iterating through each index in tokens
    for i in range(0, len(tokens)):

        current_token = tokens[i]

        if is_numeric_token(current_token):
            # Adding the current token (which is a number) to the rpn stack to be operated on

            push(current_token, rpn_stack)

        elif current_token in BINARY_OPERATORS:
            # First number to be operated on is being taken from the stack
            rhs = pop(rpn_stack)
            # Second number to be operated on is being token from the stack
            lhs = pop(rpn_stack)
            # The awnser of the equation using the binary_operator() function
            answer = binary_operator(lhs, rhs, current_token)
            # Adding the answer to the stack
            push(answer, rpn_stack)

        else:
            raise ValueError(
                "The token: {} is not a supported token. Please remove it.".format(
                    current_token
                )
            )

    # If the rpn_stack has only one element (that element would be the answer)
    if len(rpn_stack) == 1:
        # Ending the loop and returning the stack with the answer
        return rpn_stack[0]
    else:
        raise ValueError(
            "Your equation is non-mathmatical, here are the tokens: {}".format(tokens)
        )
