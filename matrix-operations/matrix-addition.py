from matrix import *

def matrix_addition(a: Matrix, b: Matrix):
    
    #Validity check
    if not a.is_valid or not b.is_valid:
        return f"One or more Matrices are invalid"
    
    #dimensions of matrix A and B must completely match
    elif a.get_rows() != b.get_rows() or a.get_columns() != b.get_columns():
        return f"Matrix A and B's dimensions do not match" 

    #Addition process
    final_matrix_content = []
    for i in range(len(a)):
        final_matrix_content.append(a.get_content()[i]+b.get_content()[i])

    return Matrix(content = final_matrix_content, rows = a.get_rows(), columns = a.get_columns())

"""Simple Test Case"""
# a = Matrix(content = [2,1,4,7], rows = 2, columns = 2)
# b = Matrix(content = [2,2,2,2], rows = 2, columns = 2)
# print(matrix_addition(a, b).get_content())

    
