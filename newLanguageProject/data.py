class Data:
    def __init__(self):
        self.variables = {}
        self.MEM_MAX_VARS = 2

    def read(self, id):
        return self.variables[id]

    def read_all(self):
        return self.variables

    def write(self, variable, expression):
        variable_name = variable.value
        self.variables[variable_name] = expression

        if variable_name[0].isupper():
            print(f"Variable name cannot start with an uppercase letter")
            del self.variables[variable_name]

        if len(self.variables.keys()) > self.MEM_MAX_VARS:
            print(f"Mem error: has more than {self.MEM_MAX_VARS} variables")
            del self.variables[variable_name]


