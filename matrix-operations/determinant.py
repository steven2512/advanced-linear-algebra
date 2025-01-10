from matrix import Matrix

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
    
    return det

#3x3 Test Case
A = Matrix(content = [1,12,3,4,5,6,7,8,9], rows = 3, columns = 3)
print(determinant(A))
