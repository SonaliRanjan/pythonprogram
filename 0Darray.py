# 0 Dimensional array
import numpy as np
x= np.array(35)
print("X:",x)
print("Type of X:",type(x))
print("dimension of X:",np.ndim(x))

# 1 Dimentional array
F= np.array([1,4,6,4,8,7])
V= np.array([2.3,6.9,66.7])
print("F:",F)
print("V:",V)
print("type of F:",F.dtype)
print("type of V:",V.dtype)
print("dimension of F:",np.ndim(F))
print ("dimensionof V:",np.ndim(V))

# 2 dimentional array
A=np.array([[32.6,53.7,45.7],
			[22.5,76.8,89.0],
			[66.7,98.6,86.6]])
print(A)
print(A.ndim)

B=np.array([ [[22,34], [34,76]],
			[[54,98], [65,89]]
			[[87,99], [43,39]] ])
print(B)
print(B.ndim)