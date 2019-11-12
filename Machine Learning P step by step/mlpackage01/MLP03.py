# List does not provide broadcasting
list = [1, 2, 3, 4]
print(list)
# but in numpy provide broadcasting
import numpy as np
narr = np.array([1, 2, 3, 4])
print(narr)
print(narr+4)
print(narr*4)
print(narr/2)
print(narr.size)
a = 4
b = 2
print(a/b)
print(narr.dtype)
print(len(narr))
print(narr.shape)
