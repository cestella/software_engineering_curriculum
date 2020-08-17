import numbers
from src import lexer

BINARY_OPERATORS = ["+", "-", "*", "/"]

OPS_RANKING = {"(": 1, ")": 1, "/": 2, "*": 2, "+": 3, "-": 3}

OPS_ASSOSIATIVITY = {"+": "l", "-": "l", "*": "l", "/": "l"}


def is_function(string):
    return False


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
    integer or float : The final answer after after the nums are operated on
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
            "The operator you used: {} is not supported. Valid Operators: {}".format(
                op, ",".join(BINARY_OPERATORS)
            )
        )


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

    return isinstance(token, numbers.Number)


def push(value, stack):
    """
    Pushes the element (value) to the given stack, which mutates the stack
    Parameters
    ----------
    value : element
        The element to be pushed on top of the stack
    stack : list
        The stack that e is going to be pushed onto
    """
    stack.append(value)


def pop(stack):
    """
    Retrieves the last element from the given stack and deletes it, which mutates iti
    Parameters
    ----------
    stack : list
        The stack (in list form) to be operated on
    Returns
    -------
    value : char
        The value at the end of the given stack
    """
    return stack.pop()


def peek(stack):
    """
    Returns the top value of the given stack
    Parameter
    ---------
    stack : list
        The stack (in list form) to operated on
    Returns
    -------
    token : The top token of the stack
    """
    try:
        return stack[-1]
    except:
        return None


def enqueue(value, queue):
    """
    Pushes the element (value) to the given queue, which mutates the queue
    Parameters
    ----------
    queue : list
        The queue in list form
    value : element
        The item to enqueue to the given queue
    """
    queue.append(value)


def rpn(tokens):
    """
    Parses RPN and returns an answer

    Parameters
    ----------
    tokens : list
        list of tokens in RPN

    Returns
    -------
    answer : the answer to the expression
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
            # The number to the right of the operator is being taken from the stack
            rhs = pop(rpn_stack)
            # The number to the left of the operator is being taken from the stack
            lhs = pop(rpn_stack)
            # The answer of the expression using the binary_operator() function

            answer = binary_operator(lhs, rhs, current_token)
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
            "Your equation is non-mathmatical, here are the tokens: {}".format(
                ",".join(str(t) for t in tokens)
            )
        )


def infix(token_list):

    """
    Parses Infix notation and returns the equivilant RPN form (Pseudocode used from: https://en.wikipedia.org/wiki/Shunting-yard_algorithm)

    Parameters
    ==========
    token_list : list
        The list of infix tokens

    Returns 
    --------
    output : list
        This is the output queue where the final answer is arranged
    
    """

    # Output Queue
    output = []

    # Operators Stack
    operators = []

    processed_tokens = 0

    # Iterating through each token in the token_list
    for token in token_list:
        if is_numeric_token(token):

            enqueue(token, output)
            processed_tokens += 1

        elif is_function(token):
            push(token, operators)
            processed_tokens += 1

        elif token in lexer.OPS:
            # If there are tokens to be read then
            # 1. If the operators stack is not empty (for the first operator, we want to skip this loop and go push the token to the opeators stack)
            # 2. And the operator on teh operator stack has greater precedence (for order of operations)
            # 3. Or they have equal precedense and the token is left associative because if the tokens are 1+1+1, then we need to know which way to group them
            # 4. If the operator on the operator stack is not a "("
            while (
                (len(operators) != 0)
                and (
                    (OPS_RANKING[peek(operators)] < OPS_RANKING[token])
                    or (
                        OPS_RANKING[peek(operators)] == OPS_RANKING[token]
                        and OPS_ASSOSIATIVITY[token] == "l"
                    )
                )
                and (peek(operators) != "(")
            ):
                # Pushing the token on top of the operators stack onto the output queue
                enqueue(pop(operators), output)
                processed_tokens += 1

            push(token, operators)

        # This is basically useless, that is why we skip it in the operator while loop, but we still need to recognize it as an operator processed
        if token == "(":
            push(token, operators)
            processed_tokens += 1

        elif token == ")":
            # If the operator on the top of the operator stack is not a "(", then it is an operator, and since this is the end of the group then we have to update the output with the operator
            # If the top of the operator stack is not a "(" (Left Parenthesis)
            if peek(operators) != "(" and len(operators) != 0:
                enqueue(pop(operators), output)
                processed_tokens += 1

            # Ignoring this char again, but we still need to count it as a operator operated on
            # If the top of the operator stack is a "(" (Left Parenthesis)
            if peek(operators) == "(" and len(operators) != 0:
                pop(operators)
                processed_tokens += 1

    if len(token_list) - 1 == processed_tokens:
        while len(operators) != 0:
            if peek(operators) != "(":
                enqueue(pop(operators), output)

    return output
