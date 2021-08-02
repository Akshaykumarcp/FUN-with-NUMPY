import numpy as np

# INT
int_array = np.arange(10)
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

int_array.dtype
# dtype('int32')

# FLOAT
float_array = np.arange(10,dtype='float64')
# array([0., 1., 2., 3., 4., 5., 6., 7., 8., 9.])

float_array.dtype
# dtype('float64')

# COMPLEX
complex_arr = np.array([1+2j, 2+4j])
# array([1.+2.j, 2.+4.j])

complex_arr.dtype
# dtype('complex128')

# BOOLEAN
boolean_arr = np.array([True, False, True, False])

boolean_arr.dtype
# bool

# for other datatypes refer https://numpy.org/doc/stable/user/basics.types.html