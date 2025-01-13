from matrix_operations.matrix import Matrix
from matrix_decompositions.lu import lu

def determinant(A: Matrix):
    """Determinant of a matrix A/ Scaling factor of linear transformation A"""
    A.is_valid()

    #Square check
    if not A.is_square():
        raise ValueError("Non-square Matrix does not have a determinant")
    
    content = A.get_content()

    det = 0

    #2x2 case
    if A.get_rows() == 2 and A.get_columns() == 2:
        det = (content[0] * content[3]) - (content[1] * content[2])

    #3x3 case
    if A.get_rows() == 3 and A.get_columns() == 3:
        det = content[0] * (content[4] * content[8] - content[5] * content[7]) \
        - content[1] * (content[3] * content[8] - content[5] * content[6]) \
        + content[2] * (content[3] * content[7] - content[4] * content[6])
    
    #nxn case
    #We decompose any matrix A into a lower triagnular matrix L and uper triangular matrix U, so we have det(A) = det(L) * det(U) (determinant multiplicativity)

    l,u = lu(A)
    print(l, u)


    det = 1
    for i in range(A.get_rows()):
        index = A.get_columns() * i + i

        #Determinant of a lower triangular/upper triangular matrix is the product of its diagonal
        #Here we skip calculating determinant of L because L diagonal's is all 1's
        det *= u.get_content()[index]

    return det



#2x2 Test Case
# A = Matrix(content = [1,12,3,4], rows = 2, columns = 2)
# print(determinant(A))

#3x3 Test Case
# A = Matrix(content = [1,12,3,4,5,6,7,8,9], rows = 3, columns = 3)
# print(determinant(A))

#nxn case
# A = Matrix(content = [1,12,3,4,5,6,7,8,9,10,11,12,14,25,30,32], rows = 4, columns = 4)
# print(determinant(A))
