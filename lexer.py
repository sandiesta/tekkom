import re

class lexer(object):

    def __init__(self, source_code):
        self.source_code = source_code
    
    def tokenize(self):
        
        tokens = []

        source_code = self.source_code.split()

        source_index = 0

        while source_index < len(source_code):
            word = source_code[source_index]

            if word == "v":
                tokens.append(["VAR_DECLARATION", word])

            elif re.match('[a-z]', word) or re.match('[A-Z]', word):
                if word[len(word) - 1] == ";":
                    tokens.append(['IDENTIFIER', word[0:len(word) - 1]])
                else:
                    tokens.append(['IDENTIFIER', word])

            elif re.match('[0-9]', word):
                if word[len(word) -1] == ";":
                    tokens.append(['INTEGER', word[0:len(word) -1]])
                else:
                    tokens.append(['INTEGER', word])

            elif word in "=/*=+":
                tokens.append(['OPERATOR', word])

            if word[len(word) -1] ==";":
                tokens.append(['STATEMENT_END', ':'])

            source_index += 1

        print(tokens)

        return tokens