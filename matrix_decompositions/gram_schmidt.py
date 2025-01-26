from matrix_operations.matrix import Matrix
from matrix_operations.multiplication import multiplication
from vector_operations.projection import scalar_projection, vector_projection
from matrix_operations.subtraction import subtraction
import pdb



def gram_schmidt(vectors: list[Matrix]):
    u = []
    for i in range(len(vectors)):
        current = vectors[i]
        for j in range(0,i):
            current = subtraction(current, vector_projection(vectors[i], u[j]))
        u.append(current)
    for i in range(len(u)):
        u[i] = u[i].normalize_vector()
    return u

# v0 = Matrix([1,1,0], 3, 1)
# v1 = Matrix([1,0,1], 3, 1)
# v2 = Matrix([0,1,1], 3, 1)

# print(*gram_schmidt([v0, v1, v2]))
