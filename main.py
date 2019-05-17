import san_lexer
import san_parser
import san_interpreter

from sys import *

#DENGAN MASUKAN BAHASAKU.san
lexer = san_lexer.BasicLexer()
parser = san_parser.BasicParser()
env = {}

file = open(argv[1])
text = file.readlines()
for line in text:
    tree = parser.parse(lexer.tokenize(line))
    san_interpreter.BasicExecute(tree, env)
