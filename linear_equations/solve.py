from linear_equations.equation import Equation
from linear_equations.term import Term
from linear_equations.polynomial import Polynomial
from linear_equations.variable import Variable
from linear_equations.fraction import Fraction
import numpy as np
import pdb

def solve(equation: Equation, variable: str):
    lhs: Polynomial = equation.get_lhs()
    rhs: Polynomial = equation.get_rhs()

    found = check_variable(lhs.get_terms(), rhs.get_terms(), variable)
    if not found:
        raise ValueError(f"Variable {variable} does not exist in the equation")
    
    #Initialize new lhs and rhs
    new_lhs: Polynomial = Polynomial()
    new_rhs: Polynomial = Polynomial()
    
    #Put all terms that contain target variable to LHS
    #Put all other terms to RHS
    
    for term in lhs.get_terms():
        if term.get_variable().get_symbol() == variable:
            new_lhs.add_term(term)
              
        else:
            term.flip_coefficient()
            new_rhs.add_term(term)
        
    for term in rhs.get_terms():
        if term.get_variable().get_symbol() == variable:
            term.flip_coefficient()
            new_lhs.add_term(term)
        else:
            new_rhs.add_term(term)

    
    #Simplify LHS and RHS
    new_lhs.simplify()
    new_rhs.simplify()

    #Divide by coefficient of main term (that consists the target variable)
    new_rhs.divide_polynomial(new_lhs.get_terms()[0].get_coefficient())
    
    #
    print(f"{variable} =  {new_rhs}")
    return new_rhs

def check_variable(lhs: list[Term], rhs: list[Term], variable: Variable):
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

    
# #Test 1
# var1 = Variable('x')
# var2 = Variable('x')
# term1 = Term(5)
# term2 = Term(3, var1)
# term3 = Term(-2, var2)
# term4 = Term(20)
# pol1 = Polynomial([term1, term2])
# pol2 = Polynomial([term3, term4])
# eq = Equation(pol1, pol2)
# print(eq)
# solve(eq, 'x')

#Test 2
# var1 = Variable('x')
# var2 = Variable('x')
# term1 = Term(8)
# term2 = Term(-5, var1)
# term3 = Term(2, var2)
# term4 = Term(1/3)
# pol1 = Polynomial([term1, term2])
# pol2 = Polynomial([term3, term4])
# eq = Equation(pol1, pol2)
# print(eq)
# solve(eq, 'x')

#Test 3
var1 = Variable('x')
var2 = Variable('x')
var3 = Variable('y')
var4 = Variable('y')
term1 = Term(4, var1)
term2 = Term(-3, var3)
term3 = Term(7)
term4 = Term(2, var2)
term5 = Term(2.5, var4)
term6 = Term(-9)
pol1 = Polynomial([term1, term2, term3])
pol2 = Polynomial([term4, term5, term6])
eq = Equation(pol1, pol2)
print(eq)
solve(eq, 'x')



