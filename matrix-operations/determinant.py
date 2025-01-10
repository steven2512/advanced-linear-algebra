from matrix import Matrix

def determinant(A: Matrix):
    """Determinant of a matrix A/ Scaling factor of linear transformation A"""
    A.is_valid()

    #Square check
    if not A.is_square():
        raise ValueError("Non-square Matrix does not have a determinant")
    
    #2x2 case
    if A.get_rows() == 2 and A.get_columns() == 2:
        return A.get_content()[0] * A.get_content()[3] - A.get_content()[1] * A.get_content()[2]
