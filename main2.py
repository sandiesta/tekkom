import lexer
import parser
import interpreter

from sys import *

if __name__ == '__main__':
  lexer = lexer.BasicLexer()
  parser = parser.BasicParser()
  env = {}
  while True:
    try:
      text = input('san > ')
        except EOFError:
    break
      if text:
        tree = parser.parse(lexer.tokenize(text))
         interpreter.BasicExecute(tree, env)
