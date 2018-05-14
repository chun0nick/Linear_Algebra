# Linear_Algebra
Matricies are of the form [[row1],[row2],[row3]]  
Example:  
1 2 3  
4 5 6  
7 8 9  
would be [[1, 2, 3],[4, 5, 6],[7, 8, 9]]  
There are currently 4 functions.  
All of them are contained in all_ops.py.    
# 1. reducer(matrix)
prints the matrix in readable reduced row echelon form and 
returns the matrix in reduced row echelon form  
Example:  
\>>> matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]  
\>>> reduced = reducer(matrix)  
[1.0, 0.0, -1.0]  
[0.0, 1.0, 2.0]  
[0.0, 0.0, 0.0]  
\>>> reduced  
[[1.0, 0.0, -1.0], [0.0, 1.0, 2.0], [0.0, 0.0, 0.0]]  

# 2. invert(matrix)
returns the inverse of a matrix  
Example:  
\>>> matrix = [[-2, -1, 2],[4, -4, 5],[-1, -2, 2]]  
\>>> inverted = invert(matrix)  
[-0.1333, 0.1333, -0.2]  
[0.867, 0.1333, -1.2]  
[0.8, 0.2, -0.8]  
\>>> inverted  
[[-0.13333, 0.13333, -0.2],[0.86667, 0.13333, -1.2],[0.8, 0.19999, -0.8]]  

# 3. determinant(matrix)  
returns the determinant of the matrix  
Example:  
\>>> matrix = [[-2, -1, 2],[4, -4, 5],[-1, -2, 2]]  
\>>> determinant(matrix)  
-15  

# 4. multiply(matrix, matrix)  
returns the result of multiplying two matricies together  

Example:  
\>>> matrix1 = [[-2, -1, 2],[4, -4, 5],[-1, -2, 2]]  
\>>> matrix2 = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]  
\>>> multiplied = multiply(matrix1, matrix2)  
[8, 7, 6]  
[23, 28, 33]  
[5, 4, 3]  
\>>> multiplied  
[[8, 7, 6],[23, 28, 33],[5, 4, 3]]  