import numpy as np

a = np.arange(5)
# array([0, 1, 2, 3, 4])

np.sin(a)  
# array([ 0.        ,  0.84147098,  0.90929743,  0.14112001, -0.7568025 ])

np.log(a)
# array([      -inf, 0.        , 0.69314718, 1.09861229, 1.38629436])

np.exp(a)
# array([ 1.        ,  2.71828183,  7.3890561 , 20.08553692, 54.59815003])

# shape mismatch
a = np.arange(4)

a + np.array([1, 2])
""" Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: operands could not be broadcast together with shapes (4,) (2,) """