from matrix_operations.matrix import Matrix

def tranpose(A: Matrix):
    """Tranpose of a matrix A, invert columns and rows"""
    A.is_valid()
    
    final_matrix_content = []
    for i in range(A.get_columns()):
        for j in range(A.get_rows()):
            index = i + A.get_columns() * j
            final_matrix_content.append(A.get_content()[index])
    
    return Matrix(
            content = final_matrix_content,
            rows = A.get_columns(),
            columns = A.get_rows()
    )

# """Small Test Case"""
# A = Matrix(content = [1,7,2,4,5,6,1,1,1,2,1,1], rows = 4, columns = 3)
# print(tranpose(A).get_content())

    

