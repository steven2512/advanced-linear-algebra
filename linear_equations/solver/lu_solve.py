from linear_equations.solver.solve import solve
from matrix_operations.matrix import Matrix, identity
from matrix_operations.multiplication import multiplication
from matrix_decompositions.lu import lu
from linear_equations.equation import Equation, build_equations
from linear_equations.solver.solve import solve
from linear_equations.polynomial import Polynomial
from linear_equations.solver.back_sub import back_sub
import pdb

def lu_solve(A: Matrix, b: Matrix):
    A.is_valid()
    b.is_valid()
    if not b.is_vector():
        raise ValueError(f"Output of linear transformation A is not a vector")
    
    l, u = lu(A)

    #Solving Ly = b, setting y = Ux
    #Building system of linear equations:
    system = build_equations(A, b)
    #Special case - back sub
    y = back_sub(system)

    system = build_equations(u, y)
    x = forward_sub(system)
        
    return x

A = Matrix(content = [2,-1,3,0,1,4,0,0,5], rows = 3, columns = 3)
b = Matrix(content = [5,6,15], rows = 3, columns = 1)
print(*lu_solve(A, b))
    

