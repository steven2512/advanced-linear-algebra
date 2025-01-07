from matrix import *

def multiplication(A: Matrix, B: Matrix):
    if not valid_check(A,B):
        return False
    
    final_matrix_content = []
    for i in range(A.get_rows()):
        for j in range(B.get_columns()):
            sum = 0
            for k in range(B.get_rows()):
                l = i*A.get_columns()+k
                o = k*B.get_columns()+j
                sum+=A.get_content()[l]*B.get_content()[o]
            final_matrix_content.append(sum)
    return Matrix(content = final_matrix_content, rows = A.get_rows(), columns = B.get_columns())

def valid_check(A: Matrix, B: Matrix):
    if not A.is_valid() or not B.is_valid():
        print("One or more matrices are invalid")
        return False
    elif A.get_columns() != B.get_rows():
        print("A's columns does not match B's rows")
        return False
    return True

"""Small Test Case"""
# A = Matrix(content = [2,4,3,2,1,1], rows = 3, columns = 2)
# B = Matrix(content = [1, 2, 3, 4, 4, 5, 6, 7], rows = 2, columns = 4)
# print(matrix_multiplication(A, B).is_valid())