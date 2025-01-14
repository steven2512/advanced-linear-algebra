from matrix_operations.matrix import Matrix

def scalar(A: Matrix, scalar: int):
    "Scalar Multiplication cA"
    A.is_valid()

    cont = A.get_content()

    for i in range(len(A)):
        cont[i] = scalar * cont[i]
    
    return A
