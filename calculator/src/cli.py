from src.lexer import lexer
from src.parser import parser

def main():
    quit = False
    while quit == False:
        user_input = input(">>>")
        user_input = user_input.strip()
        
        if user_input == "quit":
            quit = True
        else:
            answer = lexer.lex(user_input)
            answer = parser.infix(answer)
            answer = parser.rpn(answer)
            print(answer)

if __name__ == "__main__":
    main()
