import lexer

BINARY_OPERATORS = ["+", "-", "*", "/"]

OPS_RANKING = {"(":1, ")":1, "/":2, "*":3, "+":4, "-":5}

OPS_ASSOSIATIVITY = {"+":"l", "-":"l", "*":"l", "/":"l"} 

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
    stack.append(e)


def pop(list, type):
    """
    Retrieves the last element from the given stack or queue and deletes it, which mutates it

    Parameters
    ----------
    list : list
        The list to be operated on

    type : string
        Whether or not it is a queue or a stack

    """
    if type == "s":
        return list.pop()

    elif type == "q":
        return list.pop(0)

def peek(list, type):
    """
    Returns the top value of the given stack

    Parameter
    ---------
    stack : list
        The stack to operated on

    Returns
    -------
    token : The top token of the stack
    """
    
    try:
        if type == "s":
            return list[-1]

        elif type == "q":
            return list[0]

    except:
        return None

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
            rhs = pop(rpn_stack, "s")
            # The number to the left of the operator is being taken from the stack
            lhs = pop(rpn_stack, "s")
            # The answer of the expression using the binary_operator() function
            # print("lhs: {} and rhs: {}".format(lhs, rhs))

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
    output = []
    operators = []
    iteration_num = 1 
    for token in token_list:
        
        if str(token).isdigit() or "-" in str(token) and str(token) != "-" or "." in str(token):
            push(token, output)
            iteration_num += 1

        elif is_function(token):
            push(token, operators)

        elif token in lexer.OPS:
            while ((peek(operators, "s") != None)
                   and ((OPS_RANKING[peek(operators, "s")] > OPS_RANKING[token])
                   or (OPS_RANKING[peek(operators, "s")] == OPS_RANKING[token] and OPS_ASSOSIATIVITY[token] == "l"))
                   and(peek(operators, "s") != "(")):
                push(peek(operators, "s"), output)
                iteration_num += 1
                    
        
            push(token, operators)
        
        if token == "(":
            push(token, operators)
            iteration_num += 1
    
        elif token == ")":
            while peek(operators, "s") != "(":
                push(pop(operators, "s"), output)
                iteration_num += 1 

            if peek(operators, "s") == "(":
                pop(operators, "s")
                iteration_num += 1

    if iteration_num == len(token_list):
        while len(operators) != 0:
            push(pop(operators, "s"), output)

    return output

print(rpn(infix(lexer.lex("-5 + 8"))))
print(1 + 1)
