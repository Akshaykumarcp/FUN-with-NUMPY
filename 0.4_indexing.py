import numpy as np

one_dim_array = np.arange(10)
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

one_dim_array[6]
# 6

multidim_array = np.diag([1,2,3,4])
""" array([[1, 0, 0, 0],
       [0, 2, 0, 0],
       [0, 0, 3, 0],
       [0, 0, 0, 4]]) """

multidim_array[2,2] # index begin from zero (0)
# 3

# assign value
multidim_array[1,0] = 4
# 4

