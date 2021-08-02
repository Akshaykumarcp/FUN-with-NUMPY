""" Indexing with the np.newaxis object allows us to add an axis to an array

newaxis is used to increase the dimension of the existing array by one more dimension, when used once. Thus,

1D array will become 2D array

2D array will become 3D array

3D array will become 4D array and so on """

import numpy as np

one_dim_array = np.array([1, 2, 3])
# array([1, 2, 3])

# convert 1Dim to 2Dim
one_dim_array[:,np.newaxis]
""" array([[1],
       [2],
       [3]]) """

# dimension shuffle

three_dim_array = np.arange(4*3*2).reshape(4, 3, 2)
""" array([[[ 0,  1],
        [ 2,  3],
        [ 4,  5]],

       [[ 6,  7],
        [ 8,  9],
        [10, 11]],

       [[12, 13],
        [14, 15],
        [16, 17]],

       [[18, 19],
        [20, 21],
        [22, 23]]]) """

three_dim_array.shape
# (4, 3, 2) 4 matrices with 3 X 2 matrices

# get value for 0 matrix, 2nd row and 1st column
three_dim_array[0,2,1]
# 5

# resizing

one_dim_array1 = np.arange(4)
# array([0, 1, 2, 3])

one_dim_array1.resize((8,))
# array([0, 1, 2, 3, 0, 0, 0, 0])

d1 = one_dim_array1
one_dim_array1.resize((4,))
""" Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: cannot resize an array that references or is referenced
by another array in this way.
Use the np.resize function or refcheck=False """

# sort data

two_dim_array = np.array([[5, 4, 6], [2, 3, 2]])
""" array([[5, 4, 6],
       [2, 3, 2]]) """

# sort based on row wise
sorted_array = np.sort(two_dim_array, axis=1)
""" array([[4, 5, 6],
       [2, 2, 3]]) """

# sort based on arg
one_dim_array = np.array([4, 3, 1, 2])
# array([4, 3, 1, 2])

arg_sorted_array = np.argsort(one_dim_array)
# array([2, 3, 1, 0], dtype=int64)

one_dim_array[arg_sorted_array]
# array([1, 2, 3, 4])