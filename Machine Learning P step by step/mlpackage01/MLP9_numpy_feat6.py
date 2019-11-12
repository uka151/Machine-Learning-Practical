# Element wise comparision

print("<-------Element wise Comparision-------->")
import numpy as np
n1 = np.array([4, 5, 4, 2])
n2 = np.array([4, 5, 4, 2])
print("n1==n2", n1==n2)
print("n1>n2", n1>n2)
print("array wise equal:", np.array_equal(n1, n2))

# Logical operation
a = np.array([0, 1, 0, 1])
b = np.array([1, 1, 0, 0])
print("Logical_or :", np.logical_or(a, b))
print("Logical_and :", np.logical_and(a, b))

# Pi
print(np.pi)
print(np.linspace(-np.pi, np.pi, 256))
print(np.linspace(-5, 5, 10))
