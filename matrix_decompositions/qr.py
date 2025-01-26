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

def qr_algorithm(A: Matrix) -> list[float]:
    A.is_valid()
    A.is_square()
    Q,R = qr(A)
    # pdb.set_trace()
    current = multiplication(R, Q)
    while not current.is_upper_triangular():
        print(current)
        current = multiplication(*qr(current)[::-1])
    return [current.get_content()[i*A.get_columns()+i] for i in range(A.get_rows())]
       
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

A = Matrix(
    content=[
         4, -2, -1,
        -1,  4,  0,
         2, -1,  2
    ],
    rows=3,
    columns=3
)
print(qr_algorithm(A))