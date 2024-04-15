class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.idx = 0
        self.token = self.tokens[self.idx]

# Parses a factor expression
    def factor(self):
        if self.token.type == "INT" or self.token.type == "FLT":
            return self.token
        elif self.token.value == "(":
            self.move()
            expression = self.comp_expression()
            return expression

        elif self.token.type.startswith("VAR"):
            return self.token
        elif self.token.value == "+" or self.token.value == "-":
            operator = self.token
            self.move()
            operand = self.comp_expression()
            return [operator, operand]

# Parses a term expression
    def term(self):
        left_node = self.factor()
        self.move()

        while self.token.value == "*" or self.token.value == "/":
            operator = self.token
            self.move()
            right_node = self.factor()
            self.move()

            left_node = [left_node, operator, right_node]

        return left_node

# Parses an if statement.
    def if_statement(self):
        self.move()
        condition = self.comp_expression()

        if self.token.value == "do":
            self.move()
            action = self.statement()

            return condition, action

# Parses a series of if statements.
    def if_statements(self):
        conditions = []
        actions = []
        if_statement = self.if_statement()

        conditions.append(if_statement[0])
        actions.append(if_statement[1])

        if self.token.value == "other":
            self.move()
            self.move()
            else_action = self.statement()

            return [conditions, actions, else_action]

        return [conditions, actions]

# Parses a while statement
    def while_statement(self):
        self.move()
        condition = self.comp_expression()

        if self.token.value == "do":
            self.move()
            action = self.statement()
            return [condition, action]

# Parses a comparison expression.
    def comp_expression(self):
        left_node = self.expression()
        while self.token.type == "COMP":
            operator = self.token
            self.move()
            right_node = self.expression()
            left_node = [left_node, operator, right_node]

        return left_node

# Parses a expression.
    def expression(self):
        left_node = self.term()
        while self.token.value == "+" or self.token.value == "-":
            operator = self.token
            self.move()
            right_node = self.term()
            left_node = [left_node, operator, right_node]

        return left_node

#  Parses a variable
    def variable(self):
        if self.token.type.startswith("VAR"):
            return self.token

# Parses a statement
    def statement(self):
        if self.token.type == "DECL":
            # Variable assignment
            self.move()
            left_node = self.variable()
            self.move()
            if self.token.value == "=":
                operation = self.token
                self.move()
                right_node = self.comp_expression()

                return [left_node, operation, right_node]

        elif self.token.type == "INT" or self.token.type == "FLT" or self.token.type == "OP":
            # Arithmetic expression
            return self.comp_expression()

        elif self.token.value == "if":
            return [self.token, self.if_statements()]
        elif self.token.value == "while":
            return [self.token, self.while_statement()]

# Parses the tokens into a tree
    def parse(self):
        return self.statement()

#  Moves to the next token
    def move(self):
        self.idx += 1
        if self.idx < len(self.tokens):
            self.token = self.tokens[self.idx]
