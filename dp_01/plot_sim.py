# %%
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import skrf as rf
from skrf import Network
import pandas as pd
# %%
def plot_data(network):
    fig, axes = plt.subplots(1,3, figsize=(12,3), layout="constrained")
    network.plot_s_db(ax=axes[0], linewidth=3)
    axes[0].grid()
    network.plot_s_deg(ax=axes[1], linewidth=3)
    axes[1].grid()
    network.plot_s_smith(ax=axes[2], linewidth=3)
# %%
ideal_sim_data = pd.read_csv('schematics/Simulation/ideal_sim.csv')
ideal_sim = Network(frequency=ideal_sim_data.Hz_real, s=ideal_sim_data.Vout_real + 1j * ideal_sim_data.Vout_imag)
plot_data(ideal_sim)
# %%
fig1, ax1 = plt.subplots()
ideal_sim.plot_s_db(ax=ax1, label="Gain")

ax1.grid(which='both')
ax1.set_xscale('log')
ax1.get_xaxis().set_major_formatter(matplotlib.ticker.NullFormatter())
ax1.get_xaxis().set_minor_formatter(matplotlib.ticker.ScalarFormatter())

ax1.axhline(-6, c="r", label='-6 dB')
ax1.legend()
# %%
insertion_loss = np.max(ideal_sim.s_db) + 6
print(f"Insertion Loss: {insertion_loss}")
# %%
passband_ripple = np.min(ideal_sim.s_db[ideal_sim.f<70e6]) + 6
print(f"Passband Ripple: {passband_ripple}")
# %%
def find_nearest_idx(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx
passband_edge = ideal_sim.f[find_nearest_idx(ideal_sim.s_db, -9)]
print(f"Passband Edge: {passband_edge}")

stopband_start = ideal_sim.f[find_nearest_idx(ideal_sim.s_db, -26)]
print(f"Stopband Start: {stopband_start}")
# %%
