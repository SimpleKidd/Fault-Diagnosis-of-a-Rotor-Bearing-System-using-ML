# -*- coding: utf-8 -*-
"""Template_Mel_Spectrogram.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ycpibAjgQ9tMKs6rIYWEdEXlt71J22S7
"""

#@title Import Data
import numpy as np
import pandas as pd
from scipy.signal import stft
import matplotlib.pyplot as plt

# Load the time-series data
data = pd.read_csv('/content/Pressure.csv')
data = pd.DataFrame(data,index=[i for i in range(len(data))])
data

#@title Null_Values
data.isnull().sum()

#@title DataTypes
data.dtypes

"""## **Method 1** 

Mel_spectrogram
"""

#@title MelSpectrogram And Save that in .jpg format
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# load your data into a pandas dataframe
df = pd.read_csv('/content/Pressure.csv')

# loop through each column of the dataframe
for col_name in df.columns:
    # get the audio signal data from the column
    y = np.array(df[col_name])
    # compute the spectrogram
    S = librosa.feature.melspectrogram(y, sr=44100)
    # convert the power spectrogram to decibel units
    S_db = librosa.power_to_db(S, ref=np.max)
    # plot the spectrogram
    plt.figure(figsize=(4, 4))
    librosa.display.specshow(S_db, x_axis='time', y_axis='mel', sr=44100, fmax=8000)
    plt.tight_layout()
    plt.ylim(0,200)
    plt.xlim(0,0.1)
    # save the spectrogram as an image
    plt.savefig(f'{col_name}.jpg')

"""## **Method 2** 

Mel_spectrogram
"""

#@title MelSpectrogram And Save that in .npy format
# Select the column to be used as the audio signal
signal = data['Column_Nmae_for which melspectrogram need to form'].values

# Compute the spectrogram of the audio signal using STFT
f, t, Zxx = stft(signal, fs=44100, nperseg=1024)
S1_NF = np.abs(Zxx)

# Plot the spectrogram
plt.pcolormesh(t, f, S1_NF)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.ylim(0,200)
plt.xlim(0,0.1)
plt.show()

# Save the spectrogram data as a .npy file
np.save('spectrogram_P1(NON_FAULTY).npy', S1_NF)

#@title Saving .npy melspectrogram in .jpeg format
import numpy as np
import matplotlib.pyplot as plt

def load_spectrogram(filename):
    return np.load(filename)

def save_spectrogram(spectrogram, filename):
    fig = plt.figure(figsize=(2, 2))
    plt.matshow(spectrogram, origin='lower', aspect='auto', cmap='jet')
    plt.colorbar()
    plt.tight_layout()
    plt.savefig(filename, format='jpeg')
    plt.close(fig)

spectrogram = load_spectrogram('spectrogram_P1(NON_FAULTY).npy')
save_spectrogram(spectrogram, 'spectrogram_P1(NON_FAULTY).jpeg')

#@title Melsectrogram in DataFrame form
pd.DataFrame(S1_NF)

#@title Make a one common Mel spectrogram DataFrame
data_dir = [S1_NF, S2_NF,S3_NF,S1_F_RB,S2_F_RB,S3_F_RB,S1_F_RLB,S2_F_RLB,S3_F_RLB,S1_F_UBF,S2_F_UBF,S3_F_UBF] # list of spectrogram list names
spectrogram_list = []
for filename in data_dir:
    for i in filename: 
        spectrogram_list.append(i)
spectrogram_list = np.array(spectrogram_list)
spectrogram_list = pd.DataFrame(spectrogram_list)
spectrogram_list #making one common data frame