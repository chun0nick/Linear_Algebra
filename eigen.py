from matrix_ops import *
import numpy as np
class Poly:
    def __init__(self, coefficient, power):
        self.coefficient = coefficient
        self.power = power
    def multiply_poly(self, other_poly):
        return Poly(self.coefficient * other_poly.coefficient, self.power + other_poly.power)
    def multiply_int(self, int):
        return Poly(self.coefficient * int, self.power)
    def __repr__(self):
        if self.power == 0:
            return str(self.coefficient)
        elif self.coefficient == 1:
            return 'x**' + str(self.power)
        return str(self.coefficient) + 'x**' + str(self.power)

def eigen_values(matrix):
    copy = matrix[:]
    copy = str_determinant(poly_matrix(subtract_variable(copy)))
    eigen_vals = np.roots(clean_polynomial(copy))
    real_roots = []
    imaginary_roots = []
    for i in range(len(eigen_vals)):
        if np.isreal(eigen_vals[i]):
            real_roots.append(eigen_vals[i])
        else:
            imaginary_roots.append(eigen_vals[i])
    if len(real_roots) > 0:
        print("Real eigen values are:")
        for i in real_roots:
            print(np.round(i, 4))
    else:
        print("There are no real eigen values")
    if len(imaginary_roots) > 0:
        print("Imaginary eigen values are:")
        for i in imaginary_roots:
            np.set_printoptions(precision=5)
            print(np.round(i, 4))
    else:
        print("There are no imaginary eigen values")
    return eigen_vals.tolist()

def clean_polynomial(poly):
    new_poly = []
    new_int = []
    for polynom in poly:
        if isinstance(polynom, int):
            if polynom == 0:
                pass
            else:
                new_int.append(polynom)
        elif polynom.coefficient == 0 and polynom.power == 0:
            pass
        else:
            new_poly.append(polynom)
    new_poly = list(sorted(new_poly, reverse=True, key=lambda x:x.power))
    new_poly = list(map(lambda x: x.coefficient, new_poly))
    new_int.extend(new_poly)
    return new_int

def str_determinant(matrix):
    assert rows(matrix) == columns(matrix), "Matrix is not square."
    if rows(matrix) == 2 and columns(matrix) == 2:
        a, b = value(row(matrix, 0), 0), value(row(matrix, 0), 1)
        c, d = value(row(matrix, 1), 0), value(row(matrix, 1), 1)
        return gather_like_terms(sub(foil_poly(a, d), foil_poly(b, c)))
    else:
        for ind in range(rows(matrix)):
            new_matrix, new_val = shear_matrix(matrix, ind)
            if ind == 0:
                expansion_poly = foil_poly(new_val, str_determinant(new_matrix))
            elif ind % 2 == 0:
                expansion_val = foil_poly(new_val, str_determinant(new_matrix))
            else:
                new_poly = list(map(lambda x: Poly(-x.coefficient, x.power), new_val))
                expansion_val = foil_poly(new_poly, str_determinant(new_matrix))
            if ind != 0:
                expansion_poly = add(expansion_poly, expansion_val)
        return expansion_poly

def make_poly(string):
    listed_poly = []
    if 'x' in string:
        listed_poly.append(Poly(-1, 1))
        listed_poly.append(Poly(get_int(string), 0))
    else:
        listed_poly.append(Poly(int(string), 0))
    return listed_poly

def get_int_index(string):
    position = 1
    for i in string[1:]:
        if string[position] == ' ':
            return position
        position += 1

def get_int(string):
    up_until = get_int_index(string)
    return int(string[1:up_until])

def poly_matrix(matrix):
    copy = matrix[:]
    new_matrix = []
    for i in matrix:
        new_matrix.append(list(map(make_poly, i)))
    return new_matrix

def subtract_variable(matrix):
    copy = []
    for row in matrix:
        str_row = list(map(str, row))
        copy.append(str_row[:])
    counter = 0
    for row in copy:
        row[counter] = '(' + row[counter] + ' - x' + ')'
        counter += 1
    return copy

def add(first, second):
    polynomials_second = list(filter(lambda x: isinstance(x, Poly), second))
    integers_second = list(filter(lambda x: isinstance(x, int), second))
    first.extend(polynomials_second)
    first.extend(integers_second)
    return gather_like_terms(first)

def sub(first, second):
    polynomials_second = list(filter(lambda x: isinstance(x, Poly), second))
    integers_second = list(filter(lambda x: isinstance(x, int), second))
    negative_poly = list(map(lambda x: Poly(-x.coefficient, x.power), polynomials_second))
    negative_integer = list(map(lambda x: -x, integers_second))
    first.extend(negative_poly)
    first.extend(negative_integer)
    return gather_like_terms(first)

def foil_poly(first, second):
    new_poly = []
    for i in first:
        for val in second:
            new_poly.append(combine(i, val))
    return gather_like_terms(new_poly)

def gather_like_terms(poly):
    polynomials = list(filter(lambda x: isinstance(x, Poly), poly))
    integers = list(filter(lambda x: isinstance(x, int), poly))
    powers = unique(list(map(lambda x: x.power, polynomials)))
    new_poly = [sum(integers)]
    for i in powers:
        with_power = list(filter(lambda x: x.power == i, polynomials))
        coefficient = sum(map(lambda x: x.coefficient, with_power))
        new_poly.append(Poly(coefficient, i))
    return new_poly

def combine(first, second):
    first_numerical = False
    second_numerical = False
    if isinstance(first, int):
        first_numerical = True
    if isinstance(second, int):
        second_numerical = True
    if first_numerical and not second_numerical:
        return second.multiply_int(first)
    elif second_numerical and not first_numerical:
        return first.multiply_int(second)
    elif first_numerical and second_numerical:
        return first * second
    else:
        return first.multiply_poly(second)

def unique(list):
    seen = []
    for i in list:
        if i in seen:
            pass
        else:
            seen.append(i)
    return seen
