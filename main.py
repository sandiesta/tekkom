import lexer
import parser
import interpreter

from sys import *

lexer = lexer.BasicLexer()
parser = parser.BasicParser()
env = {}

file = open(argv[1])
text = file.readlines()
for line in text:
    tree = parser.parse(lexer.tokenize(line))
    interpreter.BasicExecute(tree, env)
