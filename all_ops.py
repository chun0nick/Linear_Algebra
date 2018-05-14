from matrix_ops import *

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

def determinant(matrix):
    assert rows(matrix) == columns(matrix), "Matrix is not square."
    if rows(matrix) == 2 and columns(matrix) == 2:
        a, b = value(row(matrix, 0), 0), value(row(matrix, 0), 1)
        c, d = value(row(matrix, 1), 0), value(row(matrix, 1), 1)
        return (a * d) - (b * c)
    else:
        expansion_list = []
        for ind in range(rows(matrix)):
            new_matrix, new_val = shear_matrix(matrix, ind)
            if new_val == 0:
                expansion_val = 0
            elif ind % 2 == 0:
                expansion_val = new_val * determinant(new_matrix)
            else:
                expansion_val = (-1 * new_val) * determinant(new_matrix)
            expansion_list.append(expansion_val)
        return sum(expansion_list)

def invert(matrix, steps=False):
    if not square(matrix):
        print("Matrix is not square.")
    elif determinant(matrix) == 0:
        print("Determinant of matrix is 0. Not invertible.")
    else:
        new_matrix = matrix[:]
        matrix_columns = columns(new_matrix)
        augmented = append_identity(new_matrix)
        full_matrix = reducer_invert(augmented, steps)
        returned_matrix = remove_original(full_matrix, matrix_columns)
        readable_matrix(round_matrix1(returned_matrix))
        return returned_matrix

def multiply(matrix1, matrix2):
    row_m1, col_m1 = rows(matrix1), columns(matrix1)
    row_m2, col_m2 = rows(matrix2), columns(matrix2)
    if col_m1 != row_m2:
        print("Matricies of size {0} by {1} and {2} by {3} cannot be multiplied together.".format(row_m1, col_m1, row_m2, col_m2))
    else:
        result_matrix = round_matrix(multiplier(matrix1, matrix2))
        readable_matrix(result_matrix)
        return round_matrix(result_matrix)
