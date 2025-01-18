from linear_equations.equation import Equation
from linear_equations.term import Term
from linear_equations.polynomial import Polynomial

def solve(equation: Equation, variable: str):
    lhs = equation.get_lhs()
    rhs = equation.get_rhs()
    term_lhs = lhs.get_terms()
    term_rhs = lhs.get_terms()

    

    new_lhs = 0
    new_rhs = Polynomial()

    if variable not in term_lhs and variable not in term_rhs:
        raise ValueError(f"Variable {variable} does not exist in the equation")

    main_term = 0

    for term in term_lhs:
        if term.get_variable() == variable:
            main_term = term
        else:
            new_rhs.add_term(term, )

