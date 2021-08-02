import numpy as np

array1 = np.ones((3,3)) 
""" array([[1., 1., 1.],
       [1., 1., 1.],
       [1., 1., 1.]]) """

# 2-Dim, with diagonal values 1 and rest of the values 0 i,e identity matrix
array2 = np.eye(3)
""" array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]]) """

# create matrix using diag function
array3 = np.diag([10,20,30,40])
""" array([[10,  0,  0,  0],
       [ 0, 20,  0,  0],
       [ 0,  0, 30,  0],
       [ 0,  0,  0, 40]]) """

# retrieve diagonal values of the matrix
np.diag(array2)
# array([1., 1., 1.])

# create matrix using diag random
array4 = np.random.rand(4)
# array([0.79959924, 0.49119588, 0.60578439, 0.53968689])


