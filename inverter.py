from inverter_ops import reducer_invert
from determinant import determinant
from rowreducer import random_matrix_gen, readable_matrix

def invert(matrix, steps=False):
    if not square(matrix):
        print("Matrix is not square.")
    elif determinant(matrix) == 0:
        print("Determinant of matrix is 0. Not invertible.")
    else:
        new_matrix = matrix[:]
        matrix_columns = columns(new_matrix)
        augmented = append_identity(new_matrix)
        full_matrix = reducer_invert(augmented)
        returned_matrix = remove_original(full_matrix, matrix_columns)
        readable_matrix(returned_matrix)
        return returned_matrix
