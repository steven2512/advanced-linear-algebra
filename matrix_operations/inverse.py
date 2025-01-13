from matrix_operations.matrix import Matrix
from matrix_operations.determinant import determinant
from matrix_decompositions.lu import lu


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


    return inverse        

    