"""
1Dim array --> vector
2Dim array --> matrix
3,4,5,etc array --> tensors

"""

# 2 ways

# way 1 --> manual

import numpy as np

# 1-Dim
array = np.array([10,20,30])
# array([10, 20, 30])

# shape
array.shape
# (3,)

# dim
array.ndim
# 1

# 2-Dim
two_dim_array = np.array([[10,20,30],[40,50,60]])
# array([[10, 20, 30],
#        [40, 50, 60]])

# shape
two_dim_array.shape
# (2,3)

# dim
two_dim_array.ndim
# 2

len(two_dim_array)
# 2

# 3-Dim
three_dim_array = np.array([[[10,20],[40,50]],[[70,80],[40,50]]])
""" array([[[10, 20],
        [40, 50]],

       [[70, 80],
        [40, 50]]]) """

# shape
three_dim_array.shape
# (2,2,2)

# dim
three_dim_array.ndim
# 3

len(three_dim_array)
# 2

# way 2 --> via function

# 1-Dim
array2 = np.arange(5)
# array([0, 1, 2, 3, 4])

array3 = np.arange(1,10,2) # 2 = step size
# array([1, 3, 5, 7, 9])

array4 = np.linspace(0,1,5) # 5 = # of points
# array([0.  , 0.25, 0.5 , 0.75, 1.  ])

