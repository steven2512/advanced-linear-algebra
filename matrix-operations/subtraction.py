from matrix import Matrix
from validity import sub_add_check

def subtraction(A: Matrix, B: Matrix):
    """Mathematical Matrix Subtraction A - B"""
    sub_add_check(A, B)
    
    final_matrix_content = []
    for i in range(len(A)):
        final_matrix_content.append(A.get_content()[i]-B.get_content()[i])
    
    return Matrix(
                content = final_matrix_content, 
                rows = A.get_rows(), 
                columns = A.get_columns()
                )