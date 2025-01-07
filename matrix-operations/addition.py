from matrix import *

def addition(A: Matrix, B: Matrix):
    """Addition operation A + B"""
    #Validity check
    if not A.is_valid() or not B.is_valid():
        return f"One or more Matrices are invalid"
    
    #dimensions of matrix A and B must completely match
    elif A.get_rows() != B.get_rows() or A.get_columns() != B.get_columns():
        return f"Matrix A and B's dimensions do not match" 

    #Addition process
    final_matrix_content = []
    for i in range(len(A)):
        final_matrix_content.append(A.get_content()[i]+B.get_content()[i])

    return Matrix(content = final_matrix_content, rows = A.get_rows(), columns = A.get_columns())

"""Simple Test Case"""
# A = Matrix(content = [2,1,4,7], rows = 2, columns = 2)
# B = Matrix(content = [2,2,2,2], rows = 2, columns = 2)
# print(matrix_addition(A, B).get_content())

    
