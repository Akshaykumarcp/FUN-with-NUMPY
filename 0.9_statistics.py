import numpy as np

one_dim_array = np.array([1, 2, 3, 1])
# array([1, 2, 3, 1])

two_dim_array = np.array([[1, 2, 3], [5, 6, 1]])
""" array([[1, 2, 3],
       [5, 6, 1]]) """

# compute mean of one_dim_array
one_dim_array.mean()
# 1.75

# compute median (central value) of matrix based on axis command
np.median(one_dim_array,)
# 1.5

# median by row wise
np.median(two_dim_array, axis=1)
# array([2., 5.])

# standard variation
np.std(one_dim_array)
# 0.82915619758885