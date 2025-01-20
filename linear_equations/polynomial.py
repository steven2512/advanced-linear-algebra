from linear_equations.term import Term
from linear_equations.variable import Variable
from linear_equations.operator import Operator
from sorting_algorithms.merge_sort import merge_sort
import pdb

class Polynomial:

    def __init__(self, terms: list[Term] = []):
        self.terms = terms

    def get_terms(self):
        return self.terms

    def add_term(self, term: Term):
        self.terms.append(term)

    def simplify(self):
        new_terms = []
        self.sort()

        temp = []
        for i in range(len(self.terms)):
            var = self.terms[i].get_variable()
            if temp:
                if var.get_exponent() != temp[-1].get_variable().get_exponent():
                    new_terms.append(self.sum_terms(temp))
                    temp.clear()
            temp.append(self.terms[i])

        
        if temp:
            new_terms.append(self.sum_terms(temp))
        self.terms = new_terms

    def sum_terms(self, terms):
        sum = 0
        for term in terms:
            sum+=term.get_coefficient()

        return Term(coefficient=sum, 
                    variable = terms[-1].get_variable())

    def sort(self):
        "Sort polynomials from largest exponent to smallest exponent"
        #Use merge sorts run in O(NlogN)
        self.terms = merge_sort(array = self.terms, func = lambda a: -a.get_variable().get_exponent())

    def __str__(self):
        final = ''
        for term in self.terms:
            if term.get_coefficient() > 0 and final:
                final+='+'+str(term)
            else:
                final+=str(term)
        return final


#Test
var1 = Variable('x', 3)
var2 = Variable('x', 3)
var3 = Variable('x', 4)
term1 = Term(-2, var1)
term2 = Term(4, var2)
term3 = Term(5, var3)
pol = Polynomial([term1, term2, term3])
pol.simplify()
print(pol)


        