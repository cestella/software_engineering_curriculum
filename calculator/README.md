# A Simple Calculator

Creating a simple calculator is somehow both surprisingly difficult and
surprisingly easy once we introduce some algorithms. This document will
break down the set of features which we will build (you will write the
code and I will review).

### Code Style
* Variable names which are named in a readable manner (e.g. prefer `first_token` to `x`)
* Any external dependencies are noted in the `requirements.txt` which can be generated via running `pip freeze > requirements.txt` from your virtual environment.
* The codebase should be in Python 3
* Code should be autoformatted using `black`.  This should be as simple as running `black .` from this directory.

## [X] Practice Pull Request
1. Create a new python3 virtual environment in your `~/venvs` directory for this project called `~/venvs/calculator` by running `python3 -m venv ~/venvs/calculator`.
2. Activate the virtualenv from this directory by running `source ~/venvs/calculator/bin/activate`
3. Install the required libraries in the virtualenv by running `pip install -r requirements.txt`
4. Edit this file (`README.md`) and put an `x` on line 14 inside the box (e.g. replace `[ ]` with `[x]`)
5. Using the `git` and pull request primers from the main page (see [here](https://github.com/cestella/software_engineering_curriculum#pull-request-primer) create a pull request for this change.  

Please remember to request a review from me by assigning me to your PR
(from the Pull Request webpage).

## [X] Create a lexer

A lexer is a function which takes a string and turns it into a list of
tokens.  For the purpose of our calculator, we want to create a
function called `lex` in `lexer.py` with takes an argument `line` and
returns a list of tokens of the correct type like so:
* Numbers are converted to the correct type (e.g. "1.2" is the float `1.2` whereas "1" is the int `1`)
  * Characters which can comprise a number are digits [`0`-`9`], `-` and `.`
* Do not rely on spaces to separate tokens (e.g. "-1.2*2" is a valid
  input string and should return the list `[ -1.2, '*', 2 ]`
* Negative numbers and subtraction will be hard to distinguish. Think hard about how to distinguish between a `-` sign that is part of a negative number and one which is part of subtraction. (hint: peek ahead one character)
* The following operations are supported:
  * "*" - Multiplication
  * "+" - Addition
  * "-" - Subtraction
  * "/" - Division
* The following grouping symbols are supported:
  * "("
  * ")"

To fully illustrate this, I would expect the following to be true:
```
lex('1 + 1') == [ 1, '+', 1 ]
lex('1 - -1') == [ 1, '-', -1 ]
lex('-1.2*2') == [ -1.2, '*', 2 ]
lex('(2 + 3) - 3.2') == [ '(', 2, '+', 3, ')', '-', 3.2 ]
```

These test cases have been encoded in a unit test located in
`lexer_test.py`. When you are complete with your implementation:
1. uncomment the assert statements in this test
2. run it via `nosetests ./lexer_test.py`.  If there are errors, it will indicate the test case which fails.
3. Add any new assertions that you think might be reasonable.

## [X] Create a RPN Parser
Now that you have a lexer which will convert strings into tokens, we have to DO something with those tokens.  
Since we're creating a calculator here, we should actually write a parser.  Before we do that, let's talk a bit
about the different types of mathematical notation.

### Mathematical Notation
A notation system is a way of expressing a mathematical expression.  The normal one that you've learned in school is called
"infix" because the operators fall between the operands (e.g. `1 + 1`).  While this is very convenient for us to understand,
it's not as convenient for a computer to parse.  This is because as you read the tokens `[ 1, '+', 1]` from left-to-right,
when you get to the operator `+` you don't have all of the information that you need to calculate.  Furthermore, because the
order of operations are ambiguous, we had to construct things like parenthesis to disambiguate!  All of this is non-trivial
for a parser.  There HAS to be a better, more clear way!

### Reverse Polish Notation
It turns out, if we reconsider the mathematical notation, we can construct an arrangement which still represents the same
set of mathematical expressions, but is easier to parse: [Reverse Polish Notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation).

Reverse Polish Notation, otherwise known as "postfix notation" or RPN (for short), is a way of writing mathematical expressions in which the
operands follow the operator. For instance, whereas `1 + 1` is infix, the equivalent in RPN would be `1 1 +`.
As you can see, when we get to the `+` operator in the RPN tokens (`[ 1, 1, '+' ]` in this case), we would have everything
that we need to know to perform the calculation.  Even better, there is no need for parenthesis in this system as the order of operations is entirely unambiguous and encoded in the notation itself.  
For instance, if we were to consider the RPN expression `4 5 * 3 -` it is clear that this is `(4 * 5) - 3`

There's a trick to parsing RPN, but I'm not going to tell you much about it.  Instead, I'm going to leave you with this very big hint: Sometimes programming languages who use RPN-style notation are called stack-languages.  
1. How might you use a stack to parse a RPN expression?
2. Write on your whiteboard a few expressions and their answers.  How are YOU solving them in your head?  How could you use the stack data structure to teach a computer how to recreate your internal processes?

## Your Task
Your task for this PR is to create a Reverse Polish Notation Parser:
1. Create a new file called `parser.py` next to `lexer.py` and create a function called `rpn` which will take in a list of
tokens and return the computed answer.  For instance, `assert rpn( lex('1 1 +') ) == 2` should be true.
2. Create a new file called `parser_test.py` where you will add a set of representative test cases (the example I made in 1 should be one of them).

## [X] Create a Infix to RPN Converter
While accurate, what we have now isn't the most convenient calculator to use. Specifically, we don't generally THINK in reverse
polish notation when we're writing down mathematical expressions.  Instead, we typically use infix notation (e.g. `1 + 1`) rather than RPN, but we
have spent all this time building a RPN parser to go with our lexer.  We could build another parser which will return the result and take in a list of
tokens in infix order, but that's not as straightforward as one might think.  

Instead, we can build on a classical algorithm in computer science
to perform the transformation of a list of tokens from Infix notation to RPN and then parse with our RPN parser.
This algorithm is called the [Shunting Yard](https://en.wikipedia.org/wiki/Shunting-yard_algorithm) Algorithm and the pseudocode for it is as follows:
```
/* This implementation does not implement composite functions,functions with variable number of arguments, and unary operators. */

while there are tokens to be read:
    read a token.
    if the token is a number, then:
        push it to the output queue.
    else if the token is a function then:
        push it onto the operator stack 
    else if the token is an operator then:
        while ((there is a operator at the top of the operator stack)
              and ((the operator at the top of the operator stack has greater precedence)
               or (the operator at the top of the operator stack has equal precedence and the token is left associative))
              and (the operator at the top of the operator stack is not a left parenthesis)):
            pop operators from the operator stack onto the output queue.
        push it onto the operator stack.
    else if the token is a left parenthesis (i.e. "("), then:
        push it onto the operator stack.
    else if the token is a right parenthesis (i.e. ")"), then:
        while the operator at the top of the operator stack is not a left parenthesis:
            pop the operator from the operator stack onto the output queue.
        /* If the stack runs out without finding a left parenthesis, then there are mismatched parentheses. */
        if there is a left parenthesis at the top of the operator stack, then:
            pop the operator from the operator stack and discard it
/* After while loop, if operator stack not null, pop everything to output queue */
if there are no more tokens to read then:
    while there are still operator tokens on the stack:
        /* If the operator token on the top of the stack is a parenthesis, then there are mismatched parentheses. */
        pop the operator from the operator stack onto the output queue.
exit.
```

## Your Task


* Create a new function in `parser.py` called `infix(tokens)` that uses the shunting yard algorithm to do the following:
  * Input: a list of tokens from our lexer in infix ordering
  * Returns: list of tokens in RPN ordering
  * NOTE: try to stay as close to the above pseudocode as possible; I will be looking to see if you have cribbed from existing open source python implementations.  If you do, there will be hell to pay.  This exercise is intended to demonstrate mastery of taking a nontrivial algorithm given in pseudocode and translating it to a functional representation in python.
* Create a new test called `infix_parser_test.py` with a set of tests that ensure that the following style of computation works: `assert rpn(infix(lex('1 + 1'))) == 1 + 1`

## [ ] Create a Calculator CLI REPL
I will make a command line interface where the user can install the calculator package using pip, and then just type in 'calc' into the command line, then it will show a repl in the command line.
