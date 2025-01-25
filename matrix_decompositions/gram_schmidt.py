from matrix_operations.matrix import Matrix
from matrix_operations.multiplication import multiplication
from vector_operations.projection import *
import pdb



def gram_schmidt(vectors: list[Matrix]):
    u = []
    for i in range(len(vectors)):
        current = vectors[i]
        for j in range(0,i):
            current = subtraction(current, vector_projection(vectors[j]))
        u.append(current)