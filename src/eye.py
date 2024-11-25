import pandas as pd
import h5py
import tables
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
import seaborn as sns

np.random.seed(42)


file_path = "../data/oliver_calib_ET_2024-10-27_01h43.34.319.hdf5"

file = h5py.File(file_path, 'r')

eye_data = file['data_collection']['events']['eyetracker']['GazepointSampleEvent']
#eye_data = file['data_collection']['events']['eyetracker'].keys()
#print(eye_data)

eye_df = pd.DataFrame(np.array(eye_data))
eye_df = eye_df[['experiment_id', 'time', 'left_gaze_x', 'left_gaze_y']]
print(eye_df)


x = eye_df['left_gaze_x']
y = eye_df['left_gaze_y']

image_width = 1920
image_height = 1080

# Un-normalize gaze coordinates to get pixel values
pixel_x = (x + 1) / 2 * image_width
pixel_y = (y + 1) / 2 * image_height
print("pixel_x")
print(pixel_x)

# Make matrix of coordinate data
coords_matrix = eye_df[['left_gaze_x', 'left_gaze_y']].to_numpy()
#coords_matrix = np.vstack((pixel_x, pixel_y))
print("coords_matrix")
print(coords_matrix)
# Apply smoothing to data points for better heatmap
smoothed_matrix = gaussian_filter(coords_matrix, sigma=5)
print("Smoothed matrix")
print(smoothed_matrix)

# Plot data
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2,
                               sharex=False, sharey=True,
                               figsize=(9, 4))

# Plot the original coords
ax1.hist2d(pixel_x, pixel_y, bins=40)
ax1.set_title("Original coordinates")

# Plot smoothed coords
ax2.hist2d(smoothed_matrix[:, 0], smoothed_matrix[:, 1], bins=40)
ax2.set_title("Smoothed coordinates")

plt.tight_layout()
plt.show()



"""
Notes (from class):
- Psychopy origin (0,0) is at center
- Gazepoint analysis origin (0,0) is at top left
- Try using the raw data (try plotting, seeing how its different than left_gaze_x, etc.)

> Try using MNE -- you will likely need to manually create an mne data object bc they don't support gazepoint.
    > Look how they preprocess the data for eyelinks, replicate w gazepoint and hdf5 file. Should convert your
    data into epochs or raw?
"""





"""
- The plot will show for more sparse data?
- Apply an "activation" function to your dataset so that it will thin out the dataset?
"""


"""
# Plot datapoints
plt.figure(figsize=(10,5))
plt.scatter(pixel_x, pixel_y, s=10, c='blue', alpha=0.5)
plt.title("Eye movement data points")
plt.xlabel("X Coordinate (pixels)")
plt.ylabel("Y Coordinate (pixels)")
plt.gca().invert_yaxis() # Invert y-axis to match the top-left corner origin
plt.show()
"""

"""
# Create heatmap
heatmap, xedges, yedges = np.histogram2d(pixel_x, pixel_y, bins=(image_width//10, image_height//10))

plt.figure(figsize=(10, 5))
plt.imshow(heatmap.T, origin='lower', cmap='hot', interpolation='nearest', extent=[0, image_width, 0, image_height])
plt.title("Heatmap of eye movement")
plt.xlabel("X coordinate (pixels)")
plt.ylabel("Y coordinate (pixels)")
plt.gca().invert_yaxis()
plt.colorbar(label="Number of fixations")
plt.show()
"""

"""
next:
    - apply smoothing
    - configure background image to be resume
    - set heatmaps transparency (using alpha parameter)
"""
