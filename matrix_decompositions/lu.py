from matrix_operations.matrix import Matrix

def lu(A: Matrix):
    A.is_valid()

    row = A.get_rows()
    col = A.get_columns()
    iters = row - 1

    content_l = []
    content_u = []

    for i in range(iters):
        under_pivot = iters - i
        for j in range(under_pivot):
            index = col * (j+1) + i


