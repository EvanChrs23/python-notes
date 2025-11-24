import numpy as np
import matplotlib.pyplot as plt

sizes = []
max_dims = []

for i in range(1, 20):
    for n in range(1, 10000):
        try:
            a = np.zeros([i]*n)
        except Exception:
            sizes.append(i)
            max_dims.append(n)
            break

sizes_array = np.array(sizes, dtype=float)
inv_curve = 64 / sizes_array

plt.plot(sizes, max_dims, marker='o')
plt.plot(sizes, inv_curve, 'r--', label="Scaled 1/x") 
plt.xlabel("Elements per dimension (i)")
plt.ylabel("Max supported dimensions (n)")
plt.title("NumPy: Max dimensions vs. Size per dimension")
plt.grid(True)
plt.show()
