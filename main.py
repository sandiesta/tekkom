from sly import lexer
from sly import parser

def main():

    content = ""
    with open('test.san', 'r') as file:
        content = file.read()

    lex = lexer.lexer(content)
    tokens = lex.tokenize()
main()
