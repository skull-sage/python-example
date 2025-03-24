import numpy as np

X = np.array([[1], [2], [3], [4]], np.int32)
Y = np.array([[5], [6], [7], [8]], np.int32)

print("Shape: ", X.shape, "Dimension", X.ndim)
print(X[0, 0]) # should be 3 

# Scalar multiplication
alpha = 3;
print(alpha * X)

#dot multiplication
