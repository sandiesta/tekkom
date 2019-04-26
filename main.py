import lexer

def main():

    content = ""
    with open('test.san', 'r') as file:
        content = file.read()

    lex = lexer.lexer(content)
    tokens = lex.tokenize()
main()