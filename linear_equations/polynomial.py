from linear_equations.term import Term
from linear_equations.variable import Variable
from linear_equations.operator import Operator
import pdb

class Polynomial:

    def __init__(self, terms: list[Term], operators = list[Operator]):
        if len(operators) != len(terms) - 1:
            raise ValueError("The number of Terms does not have the required number of Operators (operators != terms - 1)")
        self.terms = terms
        self.operators = operators

    def __str__(self):
        final = ''
        for i in range(len(self.terms)):
            final+=str(self.terms[i])
            
            if i<len(self.terms)-1:
                final+=str(self.operators[i])
        return final


# #Test
# var1 = Variable('x')
# var2 = Variable('y')
# term1 = Term(2, var1)
# term2 = Term(4, var2)
# term3 = Term(7)
# pol = Polynomial([term1, term2, term3], [Operator('+'), Operator("-")])
# print(pol)


        