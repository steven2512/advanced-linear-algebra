from matrix_operations.matrix import Matrix
from matrix_operations.tranpose import tranpose
from matrix_operations.multiplication import multiplication
from matrix_decompositions.gram_schmidt import gram_schmidt
import pdb

def qr(A: Matrix):
    v = separate_columns(A)
    Q = combine_columns(gram_schmidt(v))
    R = multiplication(tranpose(Q), A)
    return Q, R

def separate_columns(A: Matrix) -> list[Matrix]:
    v= []
    for i in range(A.get_columns()):
        v.append(Matrix(A.get_column_content(i), A.get_rows(), 1))
    # pdb.set_trace()
    return v

def combine_columns(u: list[Matrix]):
    content = []
    for i in range(len(u)):
        content.extend(u[i].get_content())
    return tranpose(Matrix(content, u[0].get_rows(), len(u)))

# A = Matrix([1,1,0,1,0,1,0,1,1], 3, 3)
# print(*qr(A))