from matrix_ops import *
def orthogonal_basis(matrix):
    copy = matrix[:]
    if orthogonal(copy):
        print("Matrix is already orthogonal.")
        return copy
    return gram_schmidt(copy)
