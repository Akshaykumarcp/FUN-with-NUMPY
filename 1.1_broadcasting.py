""" Basic operations on numpy arrays (addition, etc.) are elementwise

This works on arrays of the same size. Nevertheless, It’s also possible to do operations on arrays of different sizes if NumPy can transform these arrays so that they all have the same size: this conversion is called broadcasting. """

import numpy as np

a = np.tile(np.arange(0, 40, 10), (3,1))
""" array([[ 0, 10, 20, 30],
       [ 0, 10, 20, 30],
       [ 0, 10, 20, 30]]) """

a=a.T
""" array([[ 0,  0,  0],
       [10, 10, 10],
       [20, 20, 20],
       [30, 30, 30]]) """

c = np.tile(np.arange(0, 40, 10), (3,2))
""" array([[ 0, 10, 20, 30,  0, 10, 20, 30],
       [ 0, 10, 20, 30,  0, 10, 20, 30],
       [ 0, 10, 20, 30,  0, 10, 20, 30]]) """

b = np.array([0, 1, 2])
# array([0, 1, 2])

a + b # b is replicated as many required for a element wise addition
""" array([[ 0,  1,  2],
       [10, 11, 12],
       [20, 21, 22],
       [30, 31, 32]]) """

# ---------------------------

one_dim_array = np.arange(0, 40, 10)
# array([ 0, 10, 20, 30])
one_dim_array.shape
# (4,)

# convert one_dim_array to two_dim_array

two_dim_array = one_dim_array[:, np.newaxis]  # adds new axis -> 2D array
""" array([[ 0],
       [10],
       [20],
       [30]]) """

two_dim_array.shape
# (4, 1)