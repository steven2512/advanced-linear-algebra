from matrix import *

def matrix_multiplication(a: Matrix, b: Matrix):
    if not a.is_valid() or not b.is_valid():
        return f"One or more matrices are invalid"
    elif a.get_columns() != b.get_rows():
        return f"A's columns does not match B's rows"
    final_matrix_content = []
    for i in range(a.get_rows()):
        for j in range(b.get_columns()):
            sum = 0
            for k in range(b.get_rows()):
                l = i*a.get_columns()+k
                o = k*b.get_columns()+j
                sum+=a.get_content()[l]*b.get_content()[o]
            final_matrix_content.append(sum)
    return Matrix(content = final_matrix_content, rows = a.get_rows(), columns = b.get_columns())


# #Test cases
# a = Matrix(content = [2,4,3,2,1,1], rows = 3, columns = 2)
# b = Matrix(content = [1, 2, 3, 4, 4, 5, 6, 7], rows = 2, columns = 4)
# print(matrix_multiplication(a, b).is_valid())