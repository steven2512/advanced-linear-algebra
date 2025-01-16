from system_of_linear_equations.variable import Variable

class Term:
    "Represents a mathematical term (inclusive or exclusive of variables)"
    def __init__(self, coefficient: int, variable: str = None):
        self.coefficient = coefficient
        self.variable = variable
    def get_variable(self):
        if self.variable is None:
            raise ValueError(f"This term has no variable")
    def get_coefficent(self):
        return self.coefficient

    
