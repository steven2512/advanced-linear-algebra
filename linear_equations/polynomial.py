from linear_equations.term import Term
from linear_equations.variable import Variable
from linear_equations.operator import Operator

class Polynomial:

    def __init__(self, terms: list[Term], operators = list[Operator]):
        if len(operators) != len(terms) - 1:
            raise ValueError("The number of Terms does not match the number of Operators")
        self.terms = terms
        self.operators = operators

    def __str__(self):
        final = ''
        for i in range(self.terms):
            final+=self.terms[i]
            if i<len(self.terms)-1:
                final+=self.operators[i]


        