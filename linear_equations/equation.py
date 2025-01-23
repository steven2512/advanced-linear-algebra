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
    
    def substitute(self, variable: str, value):
        self.check_variable(variable)
        lhs_terms = self.lhs.get_terms().copy()
        rhs_terms = self.rhs.get_terms().copy()
        for i in range(len(lhs_terms)):
            if lhs_terms[i].get_variable().get_symbol() == variable:
                lhs_terms[i] = Term(lhs_terms[i].get_coefficient()*value)
        # pdb.set_trace()
        for j in range(len(rhs_terms)):
            if rhs_terms[j].get_variable().get_symbol() == variable:
                rhs_terms[j] = Term(rhs_terms[j].get_coefficient()*value)
        return Equation(Polynomial(lhs_terms), Polynomial(rhs_terms))

    def check_variable(self, variable: Variable):
        lhs = self.lhs.get_terms()
        rhs = self.rhs.get_terms()
        found = False
        for term in lhs:
            if variable == term.get_variable().get_symbol():
                found = True
                break
        if not found:
            for term in rhs:
                if variable == term.get_variable().get_symbol():
                    found = True
                    break
        return found
            

    def __str__(self):
        return f'{self.lhs}={self.rhs}'
    
def build_equations(A: Matrix, b: Matrix) -> list[Equation]:
    variables = [Variable(f'a{i+1}') for i in range(A.get_columns())]
    equations = [0 for i in range(A.get_rows())]
    # pdb.set_trace()
    for i in range(A.get_rows()):
        lhs = Polynomial()
        rhs = Polynomial()
        for j in range(A.get_columns()):
            cof = A.get_content()[i*A.get_columns() + j]
            if cof !=0:
                term = Term(cof, variables[j])
                lhs.add_term(term)
        rhs.add_term(Term(b.get_content()[i]))
        equations[i] = Equation(lhs = lhs, rhs = rhs)
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
# print(*build_equations(Matrix([0,4,7,1,9,1,1,-1,1], 3, 3), Matrix([2,2,2], 3, 1)))
        
