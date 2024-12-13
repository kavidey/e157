# %%
import scipy.signal
import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

data_path = Path("data/")
# %%
# np.savez_compressed(data_path/"tree.npz", pd.read_csv(data_path / "SDS00001.csv", skiprows=11).to_numpy())
# np.savez_compressed(data_path/"physics_door.npz", pd.read_csv(data_path / "SDS00002.csv", skiprows=11).to_numpy())
# np.savez_compressed(data_path/"close.npz", pd.read_csv(data_path / "SDS00003.csv", skiprows=11).to_numpy())
# np.savez_compressed(data_path/"womens_bathroom.npz", pd.read_csv(data_path / "SDS00004.csv", skiprows=11).to_numpy())
np.savez_compressed(data_path/"3m.npz", pd.read_csv(data_path / "SDS00005.csv", skiprows=11).to_numpy())
# %%
sample = np.load(data_path/"3m.npz")['arr_0'].T
fs = 1/(sample[0,1] - sample[0,0])

plt.plot(sample[0], sample[1], linewidth=0.1)
# %%
iq_signal = scipy.signal.hilbert(sample[1])
amp_env = np.abs(iq_signal)
phase = np.unwrap(np.angle(iq_signal))
freq = (np.diff(phase) / (2.0*np.pi) * fs)

plt.plot(sample[0][:-1], freq, linewidth=0.1)
plt.xlim(0, 0.0001)
# %%
lpf = scipy.signal.butter(10, 25e3, 'lp', fs=fs, output='sos')
filtered_freq = scipy.signal.sosfilt(lpf, freq)

plt.plot(sample[0][:-1], filtered_freq, linewidth=0.5)
# %%
