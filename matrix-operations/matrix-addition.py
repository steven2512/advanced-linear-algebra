from matrix import Matrix

def matrix_addition(a: Matrix, b: Matrix):
    if not a.is_valid or not b.is_valid:
        return f"Invalid Matrix"
