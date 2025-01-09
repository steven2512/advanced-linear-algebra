from matrix import Matrix

def multiplication_check(A: Matrix, B: Matrix):
    #Individual Matrix Validity check
    A.is_valid()
    B.is_valid()
    
    #A's column == B's rows check for a valid C = AB
    if A.get_columns() != B.get_rows():
        raise ValueError("A's columns does not match B's rows")

def sub_add_check(A: Matrix, B: Matrix):
    #Individual Matrix Validity check
    A.is_valid()
    B.is_valid()
    #dimensions of matrix A and B must completely match
    if A.get_rows() != B.get_rows() or A.get_columns() != B.get_columns():
        raise ValueError("Matrix A and B's dimensions do not match")
    