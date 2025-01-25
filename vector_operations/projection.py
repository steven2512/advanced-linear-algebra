from matrix_operations.matrix import Matrix
from vector_operations.dot import dot
from matrix_operations.scalar import scalar
import pdb

def scalar_projection(v: Matrix, q: Matrix):
    """Project vector v onto vector q"""
    # pdb.set_trace()
    return dot(v, q)/q.get_norm()

def vector_projection(v: Matrix, q: Matrix):
    return scalar(q.normalize_vector(), scalar_projection(v, q))
# v = Matrix([2,3,6], 3, 1)
# q = Matrix([1,-1,2], 3, 1)
# print(scalar_projection(v,q))