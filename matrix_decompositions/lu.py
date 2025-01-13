from matrix_operations.matrix import Matrix
from matrix_operations.multiplication import multiplication

import pdb

def lu(A: Matrix):
    A.is_valid()
    content = A.get_content()

    row = A.get_rows()
    col = A.get_columns()
    iters = row - 1

    content_l = [0] * len(A)
    content_u = content


    for i in range(iters):
        under_pivot = iters - i
        pivot_row = col * i
        pivot_idx = pivot_row + i
        
        #Fill up L and U diagonal's with pivots and 1's on the go for efficiency
        content_l[pivot_idx] = 1
        print(f"Pivot index is {pivot_idx}")
        # if content[pivot_idx] == 0:
        #     pivoting()
        for j in range(under_pivot):
            start_idx = col * (i+j+1)
            mp = content_u[start_idx] / content_u[pivot_idx]

            content_u[start_idx] = 0
            content_l[start_idx] = mp
            
            for k in range(1, col-i-1): 
                index = start_idx + k          
                #Update U matrix
                content_u[index] = content_u[index] - mp * content_u[pivot_idx+k]

            

    #Fill up the last pivot positions in L and U
    content_l[col * (row-1) + (row-1)] = 1
    content_u[col * (row-1) + (row-1)] = content[col * (row-1) + (row-1)]
        
    l = Matrix(content = content_l, rows = row, columns = col)
    u = Matrix(content = content_u, rows = col, columns = col)

    return l,u

A = Matrix(content = [2,1,4,5,3,2,1,2,1], rows = 3, columns = 3)

l,u = lu(A)
print(f"Matrix A is {A}")
print(f"Matrix L is {l}")
print(f"Matrix U is {u}")
print(f"Matrix LU is equal to {multiplication(l,u)}")
            
            


