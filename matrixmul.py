from matrix_ops import rows, columns
from rowreducer import random_matrix_gen

def multiply(matrix1, matrix2):
    row_m1, col_m1 = rows(matrix1), columns(matrix1)
    row_m2, col_m2 = rows(matrix2), columns(matrix2)
    if col_m1 != row_m2:
        print("Matricies of size {0} by {1} and {2} by {3} cannot be multiplied together.".format(row_m1, col_m1, row_m2, col_m2))
    else:
        converted_matrix = row_to_column(matrix2)
        resulting_matrix = []
        for i in matrix1:
            new_row = []
            for column in converted_matrix:
                new_row.append(dot_product(i, column))
            resulting_matrix.append(new_row)
        


a = random_matrix_gen(3, 4)
b = random_matrix_gen(4, 3)
