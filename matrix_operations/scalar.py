from matrix_operations.matrix import Matrix

def scalar(A: Matrix, scalar: int):
    "Scalar Multiplication cA"
    A.is_valid()

    for i in range(len(A)):
        A[i] = scalar * A[i]
    
    return A
