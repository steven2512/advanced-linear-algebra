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
    content_u = content.copy()


    for i in range(iters):
        under_pivot = iters - i #m-1
        pivot_row = col * i
        pivot_idx = pivot_row + i
        
        #Fill up L's diagonal entries with 1's on the go for efficiency
        content_l[pivot_idx] = 1
        # if content[pivot_idx] == 0:
        #     pivoting()
        for j in range(under_pivot):
            start_idx = col * (i+j+1) + i
            mp = content_u[start_idx] / content_u[pivot_idx]
            content_u[start_idx] = 0
            content_l[start_idx] = mp
            
            for k in range(1, col-i): 
                index = start_idx + k          
                #Update U matrix
                content_u[index] = content_u[index] - mp * content_u[pivot_idx+k]

        

    #Fill up the last pivot positions in L and U
    content_l[col * (row-1) + (row-1)] = 1
        
    l = Matrix(content = content_l, rows = row, columns = col)
    u = Matrix(content = content_u, rows = col, columns = col)

    return l,u


#3x3 matrix
# A = Matrix(content = [2,1,4,5,3,2,1,2,1], rows = 3, columns = 3)
# print(f"Matrix A is {A}")
# l,u = lu(A)
# print(f"Matrix L is {l}")
# print(f"Matrix U is {u}")
# print(f"Matrix LU is equal to {multiplication(l,u)}")
            
            


