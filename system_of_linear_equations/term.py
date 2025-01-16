from system_of_linear_equations.variable import Variable

class Term:
    "Represents a mathematical term (inclusive or exclusive of variables)"
    def __init__(self, coefficient: int, variables: list[Variable]):
        self.coefficient = coefficient
        self.variables = variables
    def get_variable(self, variable: str):
        if len(self.variables) == 1:
            return self.variables[0]
        else:
            for var in self.variables:
                if var.get_symbol() == variable:
                    return var
    
