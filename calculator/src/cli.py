#!/usr/local/bin/env/ python3
from src.lexer import lex
from src.parser import rpn, infix
import argparse


parser = argparse.ArgumentParser(description="A Command Line Calculator")
parser.add_argument("--quiet", action="store_true")
args = parser.parse_args()


def main():
    if args.quiet == False:
        quit = False
        while quit == False:
            user_input = input(">>>")
            user_input = user_input.strip()
            if user_input == "quit":
                quit = True
            elif len(user_input.strip()) == 0:
                continue
            else:
                answer = lex(user_input)
                answer = infix(answer)
                answer = rpn(answer)
                print(answer)

    else:
        user_input = input()
        print(rpn(infix(lex(user_input))))


if __name__ == "__main__":
    main()
