"""
Put data in numpy array. Use raw eyetracker data, psycopy origin is at center.
Create raw mne object from numpy array, shape: (n_channels, n_samples) <-- what is channels? (x, y)?
Use mne to make heatmaps
"""
import pandas as pd
import numpy as np
import h5py
import tables
import mne


file_path = "../data/oliver_calib_ET_2024-10-27_01h43.34.319.hdf5"

file = h5py.File(file_path, 'r')

eye_data = file['data_collection']['events']['eyetracker']['GazepointSampleEvent']
eye_df = pd.DataFrame(np.array(eye_data))
#print(eye_df.columns)
eye_df = eye_df[['experiment_id', 'time', 'left_gaze_x', 'left_gaze_y', 'left_raw_x', 'left_raw_y']]
#print(eye_df)


mne_array = eye_df.values

# Create info object
info = mne.create_info(
    ch_names=['time', 'left_raw_x', 'left_raw_y'],
    sfreq=1000, # sampling frequency
    ch_types=['misc', 'misc', 'misc']
)

# Create raw object
raw_obj = mne.io.RawArray(mne_array.T, info) # Transpose to match (n_channles, n_times)

print(raw)
