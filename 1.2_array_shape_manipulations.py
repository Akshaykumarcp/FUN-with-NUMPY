import numpy as np

# flattening
two_dim_array = np.array([[1, 2, 3], [4, 5, 6]])
""" array([[1, 2, 3],
       [4, 5, 6]]) """

# convert 2Dim to 1Dim
two_dim_array.ravel() 
# array([1, 2, 3, 4, 5, 6])

# transpose
two_dim_array.T
""" array([[1, 4],
       [2, 5],
       [3, 6]]) """

# re-shaping
one_dim_array = two_dim_array.ravel()
# array([1, 2, 3, 4, 5, 6])

two_dim_array = one_dim_array.reshape((2,3))
""" array([[1, 2, 3],
       [4, 5, 6]]) """

# assign value
two_dim_array[0,1] = 500
""" array([[  1, 500,   3],
       [  4,   5,   6]]) """

       
