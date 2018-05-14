from matrix_ops import *
from random import randint

def reducer(matrix, steps=False):
    if not proper_structure(matrix):
        print("Matrix is malformed.")
        return
    new_matrix = matrix[:]
    if in_reduced_echelon(new_matrix):
        #new_matrix = reorder(new_matrix, steps)
        final_scale_pivots(new_matrix, steps)
        readable_matrix(new_matrix)
        return new_matrix
    for i in new_matrix:
        row_ops(new_matrix, i, steps)
    new_matrix = reorder(new_matrix, steps)
    #scale_pivots(new_matrix, steps)
    if steps and not in_reduced_echelon(new_matrix):
        readable_matrix(round_vals(new_matrix))
    try:
        return reducer(new_matrix, steps)
    except RecursionError:
        final_scale_pivots(new_matrix, steps)
        readable_matrix(new_matrix)
        return new_matrix

test_matrix = [[1, 1, 2], [2, 2, 0], [-1, 1, 3]]
bad_matrix = [[3, 6, 3], [3, 0, 2], [3, 6, 2]]
test_matrix2 = [[2, 0, 3, 0], [0, 4, 0, 0], [5, 0, 0, 0], [0, 0, 0, 6]]
edge_case = [[0,0,0], [1,1,1]]
