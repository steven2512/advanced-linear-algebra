from linear_equations.term import Term
from linear_equations.variable import Variable
from linear_equations.operator import Operator
import pdb

class Polynomial:

    def __init__(self, terms: list[Term] = []):
        self.terms = terms

    def get_terms(self):
        return self.terms

    def add_term(self, term: Term):
            self.terms.append(term)

    def simplify(self):
        new_poly = Polynomial()
        for term in self.terms:

    def sort(self):
        
    
    def __str__(self):
        final = ''
        for term in self.terms:
            if term.get_coefficent() > 0:
                final+='+'+str(term)
            else:
                final+=str(term)
        return final


# #Test
# var1 = Variable('x')
# var2 = Variable('y')
# term1 = Term(-2, var1)
# term2 = Term(4, var2)
# term3 = Term(-7)
# pol = Polynomial([term1, term2, term3])
# print(pol)


        