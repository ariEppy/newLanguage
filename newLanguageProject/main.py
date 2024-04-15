from lexer import Lexer
from parse import Parser
from interpreter import Interpreter
from data import Data

base = Data()


def checkInerpeter(expression):
    print("the syntax:" + expression + " the output: ", end="")
    tokenizer = Lexer(expression)
    tokens = tokenizer.tokenize()

    parser = Parser(tokens)
    tree = parser.parse()

    interpreter = Interpreter(tree, base)
    result = interpreter.interpret()
    if result is not None:
        print(result)


text = "50 * 2"
checkInerpeter(text)
text = "(7 + 3) * 4"
checkInerpeter(text)
text = "new a = 5"
checkInerpeter(text)
text = "new a=a+5"
checkInerpeter(text)
text = "if 5>6 do 3*3 other do 2*2"
checkInerpeter(text)
text = "new B=1"
checkInerpeter(text)
text = "new b=1"
checkInerpeter(text)
text = "while b<6 do new b = b + 1"
checkInerpeter(text)
text = " 7 / 0"
checkInerpeter(text)
text = "new c=1"
checkInerpeter(text)
# here we can to show in a dynamic way
"""
while True:
    text = input("newLanguage: ")

    tokenizer = Lexer(text)
    tokens = tokenizer.tokenize()

    parser = Parser(tokens)
    tree = parser.parse()

    interpreter = Interpreter(tree, base)
    result = interpreter.interpret()
    if result is not None:
        print(result)

"""

