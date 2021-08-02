import numpy as np

one_dim_array= np.array([1, 2, 3, 4, 5])
# array([1, 2, 3, 4, 5])

np.sum(one_dim_array)
# 15

# column wise sum on 2-Dim array
two_dim_array = np.array([[1, 1], [2, 2]])
""" array([[1, 1],
       [2, 2]]) """

two_dim_array.sum(axis=0)
# array([3, 3])

# row wise sum on 2-Dim array
two_dim_array.sum(axis=1)
# array([2, 4])

# minimum value in 1-Dim array
one_dim_array.min()
# 1

# maximum value in 1-Dim array
one_dim_array.max()
# 5

# argmin --> returns index of minimum element
one_dim_array.argmin()
# 0

# argmax --> returns index of maximum element
one_dim_array.argmax()
# 4
