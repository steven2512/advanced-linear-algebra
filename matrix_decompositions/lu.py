from matrix_operations.matrix import Matrix

def lu(A: Matrix):
    A.is_valid()
    content = A.get_content()

    row = A.get_rows()
    col = A.get_columns()
    iters = row - 1

    content_l = [0] * len(A)
    content_u = [0] * (col**2)

    for i in range(iters):
        under_pivot = iters - i
        pivot_idx = col * i + i

        #Fill up L and U diagonal's with pivots and 1's on the go for efficiency
        content_l[pivot_idx] = 1
        content_u[pivot_idx] = content[pivot_idx]

        # if content[pivot_idx] == 0:
        #     pivoting()
        for j in range(under_pivot):
            k = col * (j+1) + i
            mp = content[k] / content[pivot_idx] 
            content_l[k] = mp
            content_u[k] = 0
    
    l = Matrix(content = content_l, rows = row, columns = col)
    u = Matrix(content = content_u, rows = col, columns = col)

    return l,u

A = Matrix(content = [2,1,4,5,3,2,1,2,1], rows = 3, columns = 3)

l,u = lu(A)
print(f"Matrix L is {l}")
print(f"Matrix U is {u}")
            
            


