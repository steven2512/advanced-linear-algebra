from matrix import Matrix
from validity import sub_add_check

def subtraction(A: Matrix, B: Matrix):
    if not sub_add_check(A, B):
        return