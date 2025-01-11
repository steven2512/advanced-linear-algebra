from matrix import Matrix

def multiplication_check(A: Matrix, B: Matrix):
    #Individual Matrix Validity check
    A.is_valid()
    B.is_valid()
    
    #A's column == B's rows check for a valid C = AB
    if A.get_columns() != B.get_rows():
        raise ValueError("Matrix mulplitcation requires A.columns = B.rows")

def sub_add_check(A: Matrix, B: Matrix):
    #Individual Matrix Validity check
    A.is_valid()
    B.is_valid()
    #dimensions of matrix A and B must completely match
    if A.get_rows() != B.get_rows() or A.get_columns() != B.get_columns():
        raise ValueError("Matrix Addition/Subtraction requires A.rows == B.rows & A.columns == B.columns")
    