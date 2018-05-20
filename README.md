# Linear Algebra
Matricies are of the form [[row1],[row2],[row3]]  
Example:  
1 2 3  
4 5 6  
7 8 9  
would be [[1, 2, 3],[4, 5, 6],[7, 8, 9]]  
There are currently 5 functions.  
All of them are contained in all_ops.py.    
# 1. reducer(matrix, steps=False)  
Prints and returns the matrix in reduced row echelon form  

Example:  
\>>> matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]  
\>>> reduced = reducer(matrix)  
[1.0, 0.0, -1.0]  
[0.0, 1.0, 2.0]  
[0.0, 0.0, 0.0]  
\>>> reduced  
[[1.0, 0.0, -1.0], [0.0, 1.0, 2.0], [0.0, 0.0, 0.0]]  
\>>> reduced = reducer(matrix, True) # Would print steps  

# 2. invert(matrix)
Prints and returns the inverse of a matrix  

Example:  
\>>> matrix = [[-2, -1, 2],[4, -4, 5],[-1, -2, 2]]  
\>>> inverted = invert(matrix)  
[-0.1333, 0.1333, -0.2]  
[0.867, 0.1333, -1.2]  
[0.8, 0.2, -0.8]  
\>>> inverted  
[[-0.13333, 0.13333, -0.2],[0.86667, 0.13333, -1.2],[0.8, 0.19999, -0.8]]  

# 3. determinant(matrix)  
Returns the determinant of the matrix  

Example:  
\>>> matrix = [[-2, -1, 2],[4, -4, 5],[-1, -2, 2]]  
\>>> determinant(matrix)  
-15  

# 4. multiply(matrix, matrix)  
Prints and returns the result of multiplying two matricies together  

Example:  
\>>> matrix1 = [[-2, -1, 2],[4, -4, 5],[-1, -2, 2]]  
\>>> matrix2 = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]  
\>>> multiplied = multiply(matrix1, matrix2)  
[8, 7, 6]  
[23, 28, 33]  
[5, 4, 3]  
\>>> multiplied  
[[8, 7, 6],[23, 28, 33],[5, 4, 3]]  

# 5. orthogonal_basis(matrix, normalized=False)  
returns an orthogonal basis for the matrix  

Example:  
\>>> matrix = [[1, 1, 0],[1, 0, 2],[1, 0, 1],[1, 1, -1]]  
\>>> orthogonal_basis(matrix)  
[[1, 0.5, 0.5], [1, -0.5, 0.5], [1, -0.5, -0.5], [1, 0.5, -0.5]]  
\>>> orthogonal_basis(matrix, True)  
[[0.5, 0.5, 0.5], [0.5, -0.5, 0.5], [0.5, -0.5, -0.5], [0.5, 0.5, -0.5]]  

# 6. eigen_values(matrix)  
returns eigen values of a matrix  

Example:  
\>>> matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]  
\>>> eigen_vals = eigen_values(matrix)  
Real eigen values are:  
16.1168  
-1.1168  
There are no imaginary eigen values  
\>>> eigen_vals  
[16.116843969807043, -1.116843969807043]  
