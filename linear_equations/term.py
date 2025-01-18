from linear_equations.variable import Variable
import pdb

class Term:
    "Represents a mathematical term (inclusive or exclusive of variables)"
    def __init__(self, coefficient: int, variable: Variable = None):
        self.coefficient = coefficient
        self.variable = variable
    def get_variable(self):
        if self.variable is None:
            raise ValueError(f"This term has no variable")
        return self.variable
    def get_coefficent(self):
        return self.coefficient
    def divide_coefficient(self, coefficient: int):
        self.coefficient = self.coefficient / coefficient
    def multiply_coefficient(self, coefficient: int):
        self.coefficient = self.coefficient * coefficient
    def __str__(self):
        return f"{str(self.coefficient)}{self.variable if self.variable is not None else ''}"
