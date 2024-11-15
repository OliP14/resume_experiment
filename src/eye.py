import pandas as pd
import h5py
import tables
import numpy as np
import matplotlib.pyplot as plt


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

"""
# Plot datapoints
plt.figure(figsize=(10,5))
plt.scatter(pixel_x, pixel_y, s=10, c='blue', alpha=0.5)
plt.title("Eye movement data points")
plt.xlabel("X Coordinate (pixels)")
plt.ylabel("Y Coordinate (pixels)")
plt.gca().invert_yaxis() # Invert y-axis to match the top-left corner origin
plt.savefig('plot.png')
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
plt.savefig("heatmap.png")


"""
next:
- un-normalize x,y to get px coords
- make time to be since beginning of exp
- add col for time diff? --> it should be the same val thoughout...
"""
