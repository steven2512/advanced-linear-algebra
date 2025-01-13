from matrix_operations.matrix import Matrix
from matrix_operations.validity import multiplication_check

def multiplication(A: Matrix, B: Matrix):
    """Mathematical Matrix Multiplication C = AB (Naive Method)"""
    multiplication_check(A, B)
    
    final_matrix_content = []
    for i in range(A.get_rows()):
        for j in range(B.get_columns()):
            sum = 0
            for k in range(B.get_rows()):
                l = i * A.get_columns() + k
                o = k * B.get_columns() + j
                sum+= A.get_content()[l] * B.get_content()[o]
            final_matrix_content.append(sum)
    
    return Matrix(
                content = final_matrix_content, 
                rows = A.get_rows(), 
                columns = B.get_columns()
                )


"""Small Test Case"""
# A = Matrix(content = [2,4,3,2,1,1], rows = 3, columns = 2)
# B = Matrix(content = [1, 2, 3, 4, 4, 5, 6, 7], rows = 2, columns = 4)
# print(multiplication(A, B).get_content())