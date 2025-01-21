from linear_equations.variable import Variable
import pdb

class Term:
    "Represents a mathematical term (inclusive or exclusive of variables)"
    def __init__(self, coefficient: int, variable: Variable = Variable('....', 0)):
        self.coefficient = coefficient
        self.variable = variable
    def get_variable(self):
        return self.variable
    def add_term(self, term):
        var: Variable = term.get_variable()

        if var != self.variable or var.get_exponent() != self.variable.get_exponent():
            raise ValueError("The term being added does not have matching variable or does not have matching exponent")
        
        self.coefficient+=term.get_coefficient()
    def get_coefficient(self):
        return self.coefficient
    def divide_coefficient(self, divisor: int):
        self.coefficient /= divisor
    def multiply_coefficient(self, multiplicant: int):
        self.coefficient *= multiplicant
    def flip_coefficient(self):
        self.coefficient = -self.coefficient
    def __str__(self):
        return f"{str(self.coefficient)}{self.variable if self.variable is not None else ''}"
