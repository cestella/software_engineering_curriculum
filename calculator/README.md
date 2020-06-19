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

## [ ] Create a RPN Parser
TODO

## [ ] Create a Infix to RPN Converter
TODO

## [ ] Create a Calculator CLI REPL
TODO
