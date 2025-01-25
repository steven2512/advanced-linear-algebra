from linear_equations.solver.solve import solve
from matrix_operations.matrix import Matrix, identity
from matrix_operations.multiplication import multiplication
from matrix_decompositions.lu import lu
from linear_equations.equation import Equation, build_equations
from linear_equations.solver.solve import solve
from linear_equations.polynomial import Polynomial
from linear_equations.solver.back_sub import back_sub
from linear_equations.solver.forward_sub import forward_sub
from linear_equations.term import Term
from linear_equations.variable import Variable
import pdb


def lu_solve(A: Matrix, b: Matrix):
    """Solving sytem of linear equations using LU decomposition
        Decompose Ax = b to LUx = b, first set y = Ux, solves Ly = b then finally solves Ux = y to get final vector x"""
    A.is_valid()
    b.is_valid()
    if not b.is_vector():
        raise ValueError(f"Output of linear transformation A is not a vector")
    
    l, u = lu(A)
    
    #Solving Ly = b, setting y = Ux
    #Building system of linear equations:
    system = build_equations(l, b)
    

    #Using Forward Substituion to solve system of linear equations that are lower triangular
    y = Matrix(content = forward_sub(system), rows = l.get_columns(), columns = b.get_columns())
    # pdb.set_trace()
    #Using Backward Substituion to solve system of linear equations that are Upper triangular
    system = build_equations(u, y)

    #Infinite solution where output vector is vector 0
    if check_inf(system):
        #Assign free variable
        lhs = Polynomial()
        rhs = Polynomial()
        lhs.add_term(Term(1, Variable(f'a{len(system)}')))
        rhs.add_term(Term(1))
        system[-1] = Equation(lhs, rhs)
    
    # pdb.set_trace()
    # pdb.set_trace()
    x = Matrix(back_sub(system), rows = A.get_columns(), columns = b.get_columns())
    return x

def check_inf(system: list[Equation]):
    inf = False
    for eq in system:
        if len(eq.get_lhs().get_terms()) == 1 and eq.get_lhs().get_terms()[0].get_coefficient() == 0 and len(eq.get_rhs().get_terms()) == 1 and eq.get_rhs().get_terms()[0].get_coefficient() == 0:
            inf = True
    return inf

# A = Matrix(content = [2,-1,3,0,1,4,0,0,5], rows = 3, columns = 3)
# b = Matrix(content = [5,6,15], rows = 3, columns = 1)
# print(lu_solve(A, b))
    

