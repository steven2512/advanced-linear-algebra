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

        current = None
        sum = 0
        for i in range(len(self.terms)):
            var = self.terms[i].get_variable()
            if current is not None:
                if var.get_exponent() != current.get_variable().get_exponent() or var.get_symbol() != current.get_variable().get_symbol():
                    if sum !=0:
                        new_terms.append(Term(sum, current.get_variable()))
                    current = self.terms[i]
                    sum = 0
                    sum+= current.get_coefficient()
                else:
                    sum+=self.terms[i].get_coefficient()

            else:
                current = self.terms[i]
                sum+=current.get_coefficient()
        
        if sum != 0:
            new_terms.append(Term(sum, current.get_variable()))

        self.terms = new_terms


    def sort(self):
        "Sort polynomials from largest exponent to smallest exponent"
        #Use merge sorts run in O(NlogN)
        self.terms = merge_sort(array = self.terms, func = lambda a: (-a.get_variable().get_exponent(), a.get_variable().get_symbol()))

    def __str__(self):
        final = ''
        for term in self.terms:
            if term.get_coefficient() > 0 and final:
                final+='+'+str(term)
            else:
                final+=str(term)
        return final


#Test
var1 = Variable('t', 5)
var2 = Variable('t', 5)
var3 = Variable('c', 3)
var4 = Variable('v', 3)
var5 = Variable('k', 4)
var6 = Variable('q', 9)
var7 = Variable('k', 11)
var8 = Variable('k', 11)
var9 = Variable('l', 9)
var10 = Variable('f', 2)
term1 = Term(-2, var1)
term2 = Term(4, var2)
term3 = Term(5, var3)
term4 = Term(-2, var4)
term5 = Term(4, var5)
term6 = Term(5, var6)
term7 = Term(-2, var7)
term8 = Term(4, var8)
term9 = Term(5, var9)
pol = Polynomial([term1, term2, term3, term4, term5, term6, term7, term8, term9])
pol.simplify()
print(pol)


        