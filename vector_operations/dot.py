from matrix_operations.matrix import Matrix

def dot(v: Matrix, q: Matrix):
    v.is_valid()
    q.is_valid()
    if not v.is_vector():
        raise ValueError(f"v or q is not a valid vector")
    elif len(v) != len(q):
        raise ValueError(f"v and q does have equal dimensions")
    dot = 0
    for i in range(len(v)):
        dot += v.get_content()[i] * q.get_content()[i]

    return dot
