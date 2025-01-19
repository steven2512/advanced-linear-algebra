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
        self.sort(self.terms)
        
        for term in self.terms:

    def sort(self, terms: list[Term]):
        #Use merge sorts run in O(NlogN)
        if len(self.terms) >1:
            mid = len(self.terms)//2
            left_array = self.sort(terms[:mid+1])
            right_array = self.sort(terms[mid+1:])
        else:
            return terms
        
        sorted_list = self.merge(left_array, right_array)
        return sorted_list

    def merge(self, left_array: list, right_array: list):
        merged_list = []
        i, j = 0,0
        while i < len(left_array) or j<len(right_array):
            if i < len(left_array) and j<len(right_array):
                if left_array[i]<right_array[j]:
                    merged_list.append(left_array[i])
                    i+=1
                elif left_array[j]<right_array[i]:
                    merged_list.append(right_array[j])
                    j+=1
                else:
                    merged_list.append(left_array[i])
                    merged_list.append(right_array[j])
                    i+=1
                    j+=1
            elif i == len(left_array):
                merged_list.append(right_array[j])
                j+=1
            else:
                merged_list.append(left_array[i])
                i+=1
        return merged_list


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


        