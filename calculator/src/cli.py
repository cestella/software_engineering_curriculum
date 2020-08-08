#!/usr/local/bin/python3
from src.lexer import lex
from src.parser import rpn, infix

def main():
    quit = False
    while quit == False:
        user_input = input(">>>")
        user_input = user_input.strip()
        
        if user_input == "quit":
            quit = True
        elif len(strip(user_input)) == 0:
            continue
        else:
            answer = lex(user_input)
            answer = infix(answer)
            answer = rpn(answer)
            print(answer)

if __name__ == "__main__":
    main()
