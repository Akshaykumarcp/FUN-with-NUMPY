import numpy as np

# addition of vector with scalar
one_dim_array = np.array([11, 21, 31, 41]) #create an array
# array([11, 21, 31, 41])

one_dim_array + 1 # element wise addition
# array([12, 22, 32, 42])
 
one_dim_array ** 2 # element wise exponent
# array([ 121,  441,  961, 1681], dtype=int32)

one_dim_array - 1 # element wise subtraction
# array([10, 20, 30, 40])

# matrix multiplication

matrix1 = np.diag([1,2,3,4])
""" array([[1, 0, 0, 0],
       [0, 2, 0, 0],
       [0, 0, 3, 0],
       [0, 0, 0, 4]]) """

# way 1
matrix1 * matrix1
""" array([[ 1,  0,  0,  0],
       [ 0,  4,  0,  0],
       [ 0,  0,  9,  0],
       [ 0,  0,  0, 16]]) """

# way 2
matrix1.dot(matrix1)
""" array([[ 1,  0,  0,  0],
       [ 0,  4,  0,  0],
       [ 0,  0,  9,  0],
       [ 0,  0,  0, 16]]) """

