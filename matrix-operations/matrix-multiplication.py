from matrix import *

def matrix_multiplication(a: Matrix, b: Matrix):
    if not a.is_valid() or not b.is_valid():
        return f"One or more matrices are invalid"
    elif a.get_columns() != b.get_rows():
        return f"A's columns does not match B's rows"