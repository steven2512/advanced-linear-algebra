from matrix_operations.matrix import Matrix, identity
from matrix_operations.determinant import determinant
from matrix_decompositions.lu import lu
from matrix_operations.tranpose import tranpose
from matrix_operations.multiplication import multiplication
from matrix_operations.scalar import scalar
from linear_equations.solver.lu_solve import lu_solve 
from matrix_operations.subtraction import subtraction
import math
import pdb

def eigenvalue(A: Matrix):
    eigenvalues = []
    #2X2 case
    content = A.get_content()
    m = (content[0] + content[3])/2
    p = determinant(A)
    eigenvalues.append(m+math.sqrt(pow(m,2)-p))
    eigenvalues.append(m-math.sqrt(pow(m,2)-p))

    return eigenvalues


def eigenvector(A: Matrix, eigenvalue : float):
    n = A.get_columns()
    new_matrix = subtraction(
        A, 
        scalar(eigenvalue,
        identity(n)))
    
    eigenvector = lu_solve(new_matrix, Matrix(content = [0]*n, rows = n, column = 1))

    return eigenvector


#Test cases
A = Matrix(content = [4,2,1,3], rows =2, columns = 2)
print(eigenvalue(A))
