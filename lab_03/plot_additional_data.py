# %% Imports
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# %%
mag = pd.read_csv("data/CSV4.csv", skiprows=13, header=None, names=["frequency", "db"])
phase = pd.read_csv("data/CSV5.csv", skiprows=13, header=None, names=["frequency", "phase"])
smith = pd.read_csv("data/CSV6.csv", skiprows=13, header=None, names=["frequency", "real", "imag"])
# %%
plt.ylim(-50, 50)
plt.plot(mag.frequency/1e6, mag.db)
plt.xlabel("Frequency [MHz]")
plt.ylabel("Gain [dB]")
# %%
plt.ylim(-300, 300)
plt.plot(phase.frequency/1e6, phase.phase)
plt.xlabel("Frequency [MHz]")
plt.ylabel("Phase [deg]")
# %%
plt.gca().set_aspect('equal')
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.plot(smith.real, smith.imag)
# %% Reconstruct gain and angle measurements from smith chart
smith = pd.read_csv("data/CSV29.csv", skiprows=13, header=None, names=["frequency", "real", "imag", "other", "label"])
measurements = smith.real + 1j * smith.imag
# %%
plt.ylim(-50, 50)
plt.plot(smith.frequency/1e6, 20*np.log10(np.abs(measurements)))
plt.xlabel("Frequency [MHz]")
plt.ylabel("Gain [dB]")
plt.grid()
# %%
plt.ylim(-300, 300)
plt.plot(smith.frequency/1e6, np.angle(measurements, deg=True))
plt.xlabel("Frequency [MHz]")
plt.ylabel("Phase [deg]")
plt.grid()
# %%
mag = pd.read_csv("data/CSV32.csv", skiprows=13, header=None, names=["frequency", "db"])
phase = pd.read_csv("data/CSV31.csv", skiprows=13, header=None, names=["frequency", "phase"])
# %%
plt.ylim(-50, 50)
plt.plot(mag.frequency/1e6, mag.db)
plt.xlabel("Frequency [MHz]")
plt.ylabel("Gain [dB]")
plt.grid()
# %%
plt.ylim(-300, 300)
plt.plot(phase.frequency/1e6, phase.phase)
plt.xlabel("Frequency [MHz]")
plt.ylabel("Phase [deg]")
plt.grid()
# %%
# reflection coefficient of 270 ohm resistor
smith = pd.read_csv("data/CSV23.csv", skiprows=13, header=None, names=["frequency", "real", "imag", "other", "label"])
print(np.mean(np.abs(smith.real+1j*smith.imag)))
# %%
import plotly.express as px
mag = pd.read_csv("data/CSV36.csv", skiprows=13, header=None, names=["frequency", "db"])
fig = px.line(mag, x="frequency", y="db")
fig.show()
# %%
f0 = 100e6
fs = [80.6e6, 145.9e6]
plt.plot(mag.frequency, mag.db)
plt.axhline(-6.3, c='r')
plt.scatter(fs, [-6.3, -6.3], c='g')
plt.grid()
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude [dB]")

Q = f0/(fs[1]-fs[0])
print(Q)
# %%