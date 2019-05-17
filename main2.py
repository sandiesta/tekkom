import san_lexer
import san_parser
import san_interpreter

from sys import *

if __name__ == '__main__':
  lexer = san_lexer.BasicLexer()
  parser = san_parser.BasicParser()
  env = {}
  while True:
    try:
      text = input('san > ')
    except EOFError:
      break
    if text:
        tree = parser.parse(lexer.tokenize(text))
        san_interpreter.BasicExecute(tree, env)
