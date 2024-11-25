import numpy as np
import matplotlib.pyplot as plt
from scipy import sparse
from scipy.ndimage import gaussian_filter
np.random.seed(42)

non_zero_entries = sparse.random(50, 60)
sparse_matrix = np.zeros(non_zero_entries.shape) + non_zero_entries
sparse_matrix[sparse_matrix == 0] = None

sparse_matrix[np.isnan(sparse_matrix)] = 0

smoothed_matrix = gaussian_filter(sparse_matrix, sigma=5)

sparse_matrix[sparse_matrix == 0] =  None
print("Smoothed matrix")
print(smoothed_matrix)

# PLot
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2,
                               sharex=False, sharey=True,
                               figsize=(9, 4))
ax1.matshow(sparse_matrix)
ax1.set_title("Original matrix")
ax2.matshow(smoothed_matrix)
ax2.set_title("Smoothed matrix")
plt.tight_layout()
plt.show()
