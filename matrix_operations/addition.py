from matrix_operations.matrix import Matrix
from matrix_operations.validity import sub_add_check

def addition(A: Matrix, B: Matrix):
    """Addition operation A + B"""
    #validity check
    sub_add_check(A, B)

    #Addition process
    final_matrix_content = []
    for i in range(len(A)):
        final_matrix_content.append(A.get_content()[i] + B.get_content()[i])

    return Matrix(
                content = final_matrix_content, 
                rows = A.get_rows(), 
                columns = A.get_columns()
                )

"""Simple Test Case"""
A = Matrix(content = [2,1,4,7], rows = 2, columns = 2)
B = Matrix(content = [2,2,2,2], rows = 2, columns = 2)
print(addition(A, B).get_content())

    
