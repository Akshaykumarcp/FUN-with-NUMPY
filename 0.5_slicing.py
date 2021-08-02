import numpy as np

one_dim_array = np.arange(10)
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

one_dim_array[1:5:2]
# array([1, 3])

# assign value using slicing
one_dim_array[8:] = 20
# array([ 0,  1,  2,  3,  4,  5,  6,  7, 20, 20])

# create a copy of sliced data
sliced_data = one_dim_array[8:] 
# array([20, 20])

# create a copy of sliced data using copy() func
sliced_data = one_dim_array[::3].copy()
# array([20, 20])