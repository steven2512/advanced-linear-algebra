from matrix import Matrix

def multiplication_check(A: Matrix, B: Matrix):
    #Individual Matrix Validity check
    if not matrix_check(A, B):
        return False
    
    #A's column == B's rows check for a valid C = AB
    elif A.get_columns() != B.get_rows():
        print("A's columns does not match B's rows")
        return False
    return True

def sub_add_check(A: Matrix, B: Matrix):
    #Individual Matrix Validity check
    if not matrix_check(A, B):
        return False
    
    #dimensions of matrix A and B must completely match
    elif A.get_rows() != B.get_rows() or A.get_columns() != B.get_columns():
        print("Matrix A and B's dimensions do not match")
        return False
    return True

def matrix_check(A: Matrix, B: Matrix):
    if not A.is_valid() or not B.is_valid():
        print("One or more matrices are invalid")
        return False
    return True
    