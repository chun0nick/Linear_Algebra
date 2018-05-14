from matrix_ops import *

def determinant(matrix):
    if rows(matrix) != columns(matrix):
        print("Matrix is not square.")
    if rows(matrix) == 2 and columns(matrix) == 2:
        a, b = value(row(matrix, 0), 0), value(row(matrix, 0), 1)
        c, d = value(row(matrix, 1), 0), value(row(matrix, 1), 1)
        return (a * d) - (b * c)
    else:
        expansion_list = []
        for ind in range(rows(matrix)):
            new_matrix, new_val = rebound_matrix(matrix, ind)
            if ind % 2 == 0:
                expansion_val = new_val * determinant(new_matrix)
            else:
                expansion_val = (-1 * new_val) * determinant(new_matrix)
            expansion_list.append(expansion_val)
        return sum(expansion_list)
