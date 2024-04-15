from tokens import Integer, Float, Operation, Declaration, Variable, Comparison, Reserved




class Lexer:
    # while <expr> do <statement>
    digits = "0123456789"
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    operations = "+-/*()="
    stopwords = [" "]
    declarations = ["new"]
    comparisons = [">", "<", ">=", "<=", "?="]
    specialCharacters = "><=?"
    reserved = ["if", "other", "do", "while"]

    def __init__(self, text):
        self.text = text
        self.idx = 0
        self.tokens = []
        self.char = self.text[self.idx]
        self.token = None

# it returns a list of tokens generated from the input text.
    def tokenize(self):
        while self.idx < len(self.text):
            if self.char in Lexer.digits:
                self.token = self.extract_number()

            elif self.char in Lexer.operations:
                self.token = Operation(self.char)
                self.move()

            elif self.char in Lexer.stopwords:
                self.move()
                continue

            elif self.char in Lexer.letters:

                word = self.extract_word()

                if word in Lexer.declarations:
                    self.token = Declaration(word)
                elif word in Lexer.reserved:
                    self.token = Reserved(word)
                else:
                    self.token = Variable(word)

            elif self.char in Lexer.specialCharacters:
                comparisonOperator = ""
                while self.char in Lexer.specialCharacters and self.idx < len(self.text):
                    comparisonOperator += self.char
                    self.move()

                self.token = Comparison(comparisonOperator)

            self.tokens.append(self.token)

        return self.tokens

# give the number token from the input text.
    def extract_number(self):
        number = ""
        isFloat = False
        while (self.char in Lexer.digits or self.char == ".") and (self.idx < len(self.text)):
            if self.char == ".":
                isFloat = True
            number += self.char
            self.move()

        return Integer(number) if not isFloat else Float(number)

# give the word token from the input text.
    def extract_word(self):
        word = ""
        while self.char in Lexer.letters and self.idx < len(self.text):
            word += self.char
            self.move()

        return word

# moves the lexer to the next character in the input text
    def move(self):
        self.idx += 1
        if self.idx < len(self.text):
            self.char = self.text[self.idx]
