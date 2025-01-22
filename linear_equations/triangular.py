from linear_equations.solve import solve
from matrix_operations.matrix import Matrix
from matrix_operations.multiplication import multiplication
from matrix_decompositions.lu import lu

def lu_solve(A: Matrix, b: Matrix):
    A.is_valid()
    b.is_valid()
    if not b.is_vector():
        raise ValueError(f"Output of linear transformation A is not a vector")
    
    l, u = lu(A)

    #Solving Ly = b, setting y = Ux
    multiplication(l, Matrix())
