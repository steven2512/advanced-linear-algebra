from matrix_operations.matrix import Matrix, identity
from matrix_operations.determinant import determinant
from matrix_decompositions.lu import lu
from matrix_operations.tranpose import tranpose
from matrix_operations.scalar import scalar
from linear_equations.solver.lu_solve import lu_solve 
import pdb


def inverse(A: Matrix):
    A.is_valid()

    det = determinant(A)
    if det == 0:
        raise ValueError("Matrix with determinant = 0 does not have an inverse")
    row = A.get_rows()
    col = A.get_columns()
    cont = A.get_content()

    inverse = None

    #2x2 case
    if row == 2 and col == 2:
        inv_cont = [cont[3], -cont[1], -cont[2], cont[0]]
        inverse = Matrix(content = inv_cont,
                         rows = 2,
                         columns = 2)


    #3x3 case
    if row == 3 and col == 3:
        cof_cont = [
                    (cont[4]*cont[8]-cont[5]*cont[7]),
                    -(cont[3]*cont[8]-cont[5]*cont[6]),
                    (cont[3]*cont[7]-cont[4]*cont[6]),
                    -(cont[1]*cont[8]-cont[2]*cont[7]),
                    (cont[0]*cont[8]-cont[2]*cont[6]),
                    -(cont[0]*cont[7]-cont[1]*cont[6]),
                    (cont[1]*cont[5]-cont[2]*cont[4]),
                    -(cont[0]*cont[5]-cont[2]*cont[3]),
                    (cont[0]*cont[4]-cont[1]*cont[3])
                    ]
        cof_matrix = Matrix(content = cof_cont,
                            rows = 3,
                            columns = 3)
        inverse = scalar(tranpose(cof_matrix), 1/det)

    #nxn case
    l,u = lu(A)
    I = identity(A.get_columns())
    final = []
    for i in range(A.get_columns()):
        column_inverse = lu_solve(A, Matrix(I.get_column_content(i), I.get_rows(), 1)).get_content()

        final.extend(column_inverse)

    inverse = tranpose(Matrix(
        content= final, 
        rows = A.get_rows(), 
        columns = A.get_columns()
        ))

    return inverse

#Test case 4x4
A = Matrix(content = [
    4, 1, 1, 1,
    2, 5, 1, 1,
    1, 1, 6, 1,
    1, 1, 1, 7
], rows = 4, columns = 4)


print(inverse(A))

# print(inverse(Matrix([2,7,8,0,7,1,0,0,9], rows = 3, columns = 3)))


    