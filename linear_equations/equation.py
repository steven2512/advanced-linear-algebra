from linear_equations.operator import Operator
from linear_equations.term import Term
from linear_equations.variable import Variable
from linear_equations.polynomial import Polynomial
from matrix_operations.matrix import Matrix
import pdb

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
    
def build_equations(A: Matrix, B: Matrix):
    variables = [Variable('a'*(i+1)) for i in range(A.get_columns())]
    equations = [0 for i in range(A.get_rows())]
    # pdb.set_trace()
    for i in range(A.get_rows()):
        poly = Polynomial()
        for j in range(A.get_columns()):
            term = Term(A.get_content()[i*A.get_columns() + j], variables[j])
            poly.add_term(term)
        equations[i] = Equation(lhs = poly, rhs = B.get_content()[i])
    return equations

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
print(*build_equations(Matrix([2,4,7,1,9,1,1,-1,1], 3, 3), Matrix([2,2,2], 3, 1)))
        
