from linear_equations.equation import Equation
from linear_equations.term import Term
from linear_equations.polynomial import Polynomial

def solve(equation: Equation, variable: str):
    lhs: Polynomial = equation.get_lhs()
    rhs: Polynomial = equation.get_rhs()


    if variable not in lhs.get_terms() and variable not in rhs.get_terms():
        raise ValueError(f"Variable {variable} does not exist in the equation")
    
    #Initialize new lhs and rhs
    new_lhs: Polynomial = Polynomial()
    new_rhs: Polynomial = Polynomial()
    
    #Put all terms that contain target variable to LHS
    #Put all other terms to RHS
    for term in lhs.get_terms():
        if term.get_variable() == variable:
            new_lhs.add_term(term)
        else:
            term.flip_coefficient()
            new_rhs.add_term(term)
    
    for term in rhs.get_terms():
        if term.get_variable() == variable:
            term.flip_coefficient()
            new_lhs.add_term(term)
        else:
            new_rhs.add_term(term)
    
    #Simplify LHS
    



    return new_rhs

    
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

