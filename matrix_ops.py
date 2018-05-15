from random import randint

# decision function for row operations
def row_ops(matrix, row1, steps):
    row_index = matrix.index(row1)
    check_rows = [ind for ind, i in enumerate(matrix) if ind > row_index] # all rows under selected row
    for ind in check_rows:
        first_pivot = pivot(row(matrix, row_index)) # find pivot position of selected row
        second_pivot = pivot(row(matrix, ind)) # find pivot position of a row under selected row
        if first_pivot == None: # if the selected row is a list of just zeros
            matrix.append(row(matrix, row_index)) # append the row to the end of the matrix
            matrix.pop(row_index)# remove the row from its original location
            return
        elif second_pivot == None: # if the other row is a list of just zeros
            matrix.append(row(matrix, ind)) # append the other row to the end of the matrix
            matrix.pop(ind) # remove the other row from its original location
            return
        elif first_pivot < second_pivot: # if the pivot positon of the second row is to the right of the pivot position in the first row
                if value(row(matrix, row_index), second_pivot) != 0: # if the value of the first row at the second row's pivot position is non-zero
                    row_change(matrix, row_index, scale_and_sub(matrix, row(matrix, ind), row(matrix, row_index), second_pivot, steps))
                    # change the first row to an updated version made from scaling and subtracting the second row from the first
        elif first_pivot == second_pivot: # if the pivots are in the same position
            row_change(matrix, row_index, scale_and_sub(matrix, row(matrix, ind), row(matrix, row_index), first_pivot, steps))
            # change the first row to an updated version made from scaling and subtracting the second row from the first
        elif first_pivot > second_pivot: # if the first pivot is to the right of the second pivot
            switch(matrix, row(matrix, row_index), row(matrix, ind), steps) # switch the two rows
            return # return because the original row has changed

# reorders rows of a matrix
def reorder(matrix, steps):
    indeces_and_pivots = {}
    possible_nones = []
    new_matrix = []
    for ind,i in enumerate(matrix): # for rows in the matrix
        if pivot(i) == None: # if it is a row of zeros
            possible_nones.append(i) # append the row to the possible_nones list
        else:
            indeces_and_pivots[ind] = pivot(i) # add to the dict using the index of the row as a key, and the pivot position as a value
    while len(new_matrix) != len(matrix): # while the new matrix is not the same size as the old matrix
        if len(indeces_and_pivots) == 0 and len(possible_nones) > 0:
            # if length of dict containing nonzero rows is zero and length of list containing rows of zeros is greater than zero
            for i in possible_nones:
                new_matrix.append(i) # append rows of zeros to new matrix
            if steps:
                print("Row(s) of zeros have been replaced to bottom of matrix.")
        else:
            left_pivot = min(indeces_and_pivots, key=indeces_and_pivots.get) # find the index of the row with the leftmost pivot position
            new_matrix.append(row(matrix, left_pivot)) # append the row with the leftmost pivot position to the new matrix
            if steps and left_pivot != new_matrix.index(row(matrix, left_pivot)):
                print("Row {0} is now row {1}.".format(left_pivot+1, new_matrix.index(row(matrix, left_pivot))+1))
            indeces_and_pivots.pop(left_pivot) # pop off the appended row from the dict containing nonzero rows
    return new_matrix


def append_identity(matrix):
    identity = construct_identity(matrix)
    n = 0
    augmented = []
    for i in matrix:
        unmute = i[:]
        newest_row = unmute + identity[n]
        augmented.append(newest_row)
        n += 1
    return augmented

def remove_original(matrix, matrix_columns):
    new_matrix = []
    for i in matrix:
        appended_row = i[matrix_columns:]
        new_matrix.append(appended_row)
    return new_matrix

def square(matrix):
    if rows(matrix) == columns(matrix):
        return True
    return False

def construct_identity(matrix):
    identity = []
    n = 0
    length_row = columns(matrix)
    for i in range(rows(matrix)):
        zero_row = [0] * length_row
        zero_row[n] = 1
        identity.append(zero_row)
        n += 1
    return identity

# returns whether or not a matrix is in reduced echelon form
def in_reduced_echelon(matrix):
    comp_piv = 0 # pivot position to compare the next row to, originally assigned a value to prevent errors
    for ind, i in enumerate(matrix): # for rows in matrix
        if pivot(i) == None: # if the row is a row of zeros
            for i in matrix[ind:]: # for all rows from the row of zeros and on
                if pivot(i) != None: # if a pivot exists (nonzero row)
                    return False # a row of zeros is above a row of nonzeros, return False
        elif ind == 0: # if the row is the first row in the matrix
            comp_piv = pivot(i) # the pivot position to compare the next row to is the pivot position of the first row
        elif pivot(i) > comp_piv: # if the pivot of the row is to the right of the pivot position its being compared to
            above_vals = [x[pivot(i)] for x in matrix[:ind]] # take all values above the pivot position of the row
            for val in above_vals: # iterate over values above the pivot position
                if val != 0: # if a value is nonzero
                    return False # its not in reduced row echelon form, return False
            comp_piv = pivot(i) # new pivot to compare the next row to is pivot of current row
        elif pivot(i) <= comp_piv: # if the pivot position of a row is to the left or is equal to the pivot position of the row above
            return False # its not in reduced row echelon form, return False
    return True

# Ensures that the matrix taken as the input is of proper structure
def proper_structure(matrix):
    previous_length = len(matrix[0])
    for i in matrix[1:]:
        length = len(i)
        if length != previous_length:
            return False
        previous_length = length
    return True

# scales the pivots of a matrix
def scale_pivots(matrix, steps):
    for ind, i in enumerate(matrix): # for rows of matrix
        if pivot(i) != None: # if the row is not a row of zeros
            if -0.00001 < value(i, pivot(i)) and value(i, pivot(i)) < 0.00001:
                # python sometimes assigns a zero achieved through arithmetic a very small, nonzero value
                # if a value is very, very close to zero, but nonzero, make the value zero
                i[pivot(i)] = 0.0
            else:
                scalar = 1 / value(row(matrix, ind), pivot(i)) # find scalar for the row by taking 1 / the value of the pivot
                values = [x for x in scale_row(scalar, i)] # scale the row by the scalar
                for index, x in enumerate(values): # necessary iteration. python sometimes returns -0.0 instead of just 0.0
                    if x == 0:
                        values[index] = 0.0
                row_change(matrix, ind, values) # change row to scaled version of itself
                if scalar != 1 and steps:
                    print("Scaling row {0} by {1}.".format(ind+1, round(scalar, 3)))

def make_zero(row1):
    new_row = []
    for ind, i in enumerate(row1):
        if i <= 0.0001:
            if i >= -0.0001:
                new_row.append(0.0)
            else:
                new_row.append(i)
        else:
            new_row.append(i)
    return new_row


def make_matrix_zero(matrix):
    not_terrible_matrix = []
    for i in matrix:
        not_terrible_matrix.append(make_zero(i))
    return not_terrible_matrix

# same as scale_pivots, just rounds off values to 4 decimal places
def final_scale_pivots(matrix, steps):
    for ind, i in enumerate(matrix):
        if pivot(i) != None:
            if -0.001 < value(i, pivot(i)) < 0.001:
                i[pivot(i)] = 0.0
            else:
                scalar = 1 / value(i, pivot(i))
                values = [round(x, 4) for x in scale_row(scalar, i)]
                for index, x in enumerate(values):
                    if x == 0:
                        values[index] = 0.0
                row_change(matrix, ind, values)
                if scalar != 1 and steps:
                    print("Scaling row {0} by {1}.".format(ind+1, round(scalar, 3)))

        elif pivot(i) == None:
            new_zeros = [0.0 for x in i]
            row_change(matrix, ind, new_zeros)

#ROW OPERATIONS:
# scales and subtracts a row from another
def scale_and_sub(matrix, row1, row2, val_col, steps):
    make_zero, val = value(row2, val_col), value(row1, val_col) # finds values of the rows at the position specified
    scalar = make_zero / val # calculates the scalar needed to scale one row by to get the other value to be zero
    scaled_row1 = scale_row(scalar, row1) # scales row by the scalar
    if scalar != 1 and scalar != -1 and steps:
        if scalar < 0:
            print("Adding {0} times row {1} to row {2}.".format((-1 * round(scalar, 3)), matrix.index(row1) + 1, matrix.index(row2) + 1))
        else:
            print("Subtracting {0} times row {1} from row {2}.".format(round(scalar, 3), matrix.index(row1) + 1, matrix.index(row2) + 1))
    elif steps:
        if scalar == -1:
            print("Adding row {0} to row {1}.".format(matrix.index(row1) + 1, matrix.index(row2) + 1))
        else:
            print("Subtracting row {0} from row {1}.".format(matrix.index(row1) + 1, matrix.index(row2) + 1))
    return sub_row(scaled_row1, row2) # returns the result of subtracting the original row by the scaled row

def shear_matrix(matrix, ind):
        new_matrix = []
        current = row(matrix, ind)
        new_val = value(current, 0)
        copy_matrix = matrix[:]
        copy_matrix.pop(ind)
        for i in copy_matrix:
            new_row = i[:]
            new_row.pop(0)
            new_matrix.append(new_row)
        return new_matrix, new_val

def construct_identity(matrix):
    identity = []
    n = 0
    length_row = columns(matrix)
    for i in range(rows(matrix)):
        zero_row = [0] * length_row
        zero_row[n] = 1
        identity.append(zero_row)
        n += 1
    return identity

def dot_product(v1, v2):
    return sum([x * y for x, y in zip(v1, v2)])

def row_to_column(matrix):
    copied_matrix = matrix[:]
    all_columns = columns(copied_matrix)
    column_matrix = []
    for ind in range(all_columns):
        new_column = []
        for i in copied_matrix:
            new_column.append(i[ind])
        column_matrix.append(new_column)
    return column_matrix

def column_to_row(matrix):
    copied_matrix = matrix[:]
    all_columns = columns(copied_matrix)
    row_matrix = []
    for ind in range(all_columns):
        new_row = []
        for i in copied_matrix:
            new_row.append(i[ind])
        row_matrix.append(new_row)
    return row_matrix

def single_gram(vector, current_basis):
    original_vector = vector[:]
    for v in current_basis:
        numerator = dot_product(original_vector, v)
        denominator = dot_product(v, v)
        scalar = -1 * numerator / denominator
        gram_vector = scale_row(scalar, v)
        vector = add_vector(gram_vector, vector)
    return make_zero([round(i, 3) for i in vector])

def orthogonal(matrix):
    vector_matrix = row_to_column(matrix[:])
    for ind, vector in enumerate(vector_matrix):
        for other in vector_matrix[ind+1:]:
            if not (0.05 >= dot_product(vector, other) >= -0.05):
                return False
    return True

def gram_schmidt(matrix, normalized):
    copy = row_to_column(matrix[:])
    orthogonal_matrix = [copy[0][:]]
    for vector in copy[1:]:
        orthogonal_vector = single_gram(vector, orthogonal_matrix)
        orthogonal_matrix.append(orthogonal_vector)
    if normalized:
        normalized_matrix = []
        for vector in orthogonal_matrix:
            normalized_matrix.append(normalize_vector(vector))
        return column_to_row(normalized_matrix)
    return column_to_row(orthogonal_matrix)

def normalize_vector(vector):
    scalar = dot_product(vector, vector) ** 0.5
    return make_zero([round(i, 4) for i in scale_row(1 / scalar, vector)])


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
acon = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

def reducer_invert(matrix, steps=False):
    if not proper_structure(matrix):
        print("Matrix is malformed.")
        return
    new_matrix = matrix[:]
    if in_reduced_echelon(new_matrix):
        #new_matrix = reorder(new_matrix, steps)
        scale_pivots(new_matrix, steps)
        return new_matrix
    for i in new_matrix:
        row_ops(new_matrix, i, steps)
    new_matrix = reorder(new_matrix, steps)
    #scale_pivots(new_matrix, steps)
    if steps and not in_reduced_echelon(new_matrix):
        readable_matrix(round_vals(new_matrix))
    try:
        return reducer_invert(new_matrix, steps)
    except RecursionError:
        scale_pivots(new_matrix, steps)
        return new_matrix

def random_matrix_gen(m, n):
    row = []
    random_new_matrix = []
    for x in range(m):
        for i in range(n):
            row.append(randint(-5, 5))
        random_new_matrix.append(row)
        row = []
    return random_new_matrix

def add_vector(v1, v2):
    return [x + y for x, y in zip(v1, v2)]

# subtracts one row from another
def sub_row(row1, row2):
    new_row = [i - n for i,n in zip(row2, row1)] # subtract values of one row by another
    make_zero(new_row)
    return new_row

# scales a row by a scalar
def scale_row(c, row1):
    return [c * i for i in row1] # scale all values in a row by a value

#switches two rows
def switch(matrix, row1, row2, steps):
    row1_index = matrix.index(row1)
    row2_index = matrix.index(row2)
    if steps:
        print("Switching row {0} and row {1}.".format(row1_index + 1, row2_index + 1))
    matrix[row2_index], matrix[row1_index] = row1, row2

# SELECTORS:
#changes a row of a matrix to a new row
def row_change(matrix, row_index, new_row):
    matrix[row_index] = new_row


def rows(matrix):
    return len(matrix)

def columns(matrix):
    return len(matrix[0])

#selects a row
def row(matrix, row):
    return matrix[row]

#selects a value in a row
def value(row, position):
    return row[position]

# returns index of pivot in a row
def pivot(row1):
    for ind, i in enumerate(row1):
        if i != 0:
            return ind

def round_vals(matrix):
    rounded_matrix = []
    for i in matrix:
        values = [round(float(x), 3) for x in i]
        rounded_matrix.append(values)
    return rounded_matrix

def round_matrix(matrix):
    rounded_matrix = []
    for i in matrix:
        new_row = []
        for val in i:
            new_row.append(round(val, 2))
        rounded_matrix.append(new_row)
    returned_matrix = make_matrix_zero(rounded_matrix)
    return returned_matrix

def round_matrix1(matrix):
    rounded_matrix = []
    for i in matrix:
        new_row = []
        for val in i:
            new_row.append(round(val, 4))
        rounded_matrix.append(new_row)
    returned_matrix = make_matrix_zero(rounded_matrix)
    return returned_matrix

def multiplier(matrix1, matrix2):
    converted_matrix = row_to_column(matrix2)
    resulting_matrix = []
    for i in matrix1:
        new_row = []
        for column in converted_matrix:
            new_row.append(dot_product(i, column))
        resulting_matrix.append(new_row)
    return resulting_matrix



# prints an easily readable matrix
def readable_matrix(matrix):
    for i in matrix:
        print(i)

def readable_matrix_space(matrix):
    print("")
    for i in matrix:
        print(i)
