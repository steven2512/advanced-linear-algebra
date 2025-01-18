from linear_equations.operator import Operator
from linear_equations.term import Term
from linear_equations.variable import Variable
from linear_equations.polynomial import Polynomial

class Equation:

    def __init__(self, lhs: Polynomial, rhs: Polynomial):
        self.lhs = lhs
        self.rhs = rhs

    def get_lhs(self):
        return self.lhs
    
    def get_rhs(self):
        return self.rhs

    def __str__(self):
        return f'{self.lhs}={self.rhs}'

# #Test
# var1 = Variable('x')
# var2 = Variable('y')
# term1 = Term(2, var1)
# term2 = Term(4, var2)
# term3 = Term(7)
# term4 = Term(15)
# pol1 = Polynomial([term1, term2, term3], [Operator('+'), Operator("-")])
# pol2 = Polynomial([term4], [])
# eq = Equation(pol1, pol2)
# print(eq)
        
