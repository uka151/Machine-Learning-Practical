import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(8, 6), dpi=80)
X = np.linspace(-np.pi, np.pi, 256)
s = np.sin(X)
c = np.cos(X)
plt.plot(X, s, color='green', linewidth=6, linestyle='--', label='sin graph')
plt.plot(X, c, color='red', linewidth=6, linestyle='-', label='cos graph')
plt.legend(loc='upper left')
plt.xlim(-4, 4)
plt.ylim(-1, 1)
plt.xticks(np.linspace(-4, 4, 9, endpoint=True))
plt.yticks(np.linspace(-1, 1, 9, endpoint=True))


plt.show()