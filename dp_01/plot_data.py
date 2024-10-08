# %%
from matplotlib import pyplot as plt
import numpy as np
import skrf as rf
from skrf import Network
import pandas as pd
import matplotlib
# %%
def plot_data(network):
    fig, axes = plt.subplots(1,3, figsize=(12,3), layout="constrained")

    network.plot_s_db(ax=axes[0], linewidth=3)
    axes[0].set_xscale('log')
    # axes[0].get_xaxis().set_major_formatter(matplotlib.ticker.NullFormatter())
    # axes[0].get_xaxis().set_minor_formatter(matplotlib.ticker.ScalarFormatter())
    axes[0].grid()

    network.plot_s_deg(ax=axes[1], linewidth=3)
    axes[1].set_xscale('log')
    # axes[1].get_xaxis().set_major_formatter(matplotlib.ticker.NullFormatter())
    # axes[1].get_xaxis().set_minor_formatter(matplotlib.ticker.ScalarFormatter())
    axes[1].grid()

    network.plot_s_smith(ax=axes[2], linewidth=3)

def find_nearest_idx(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx
# %%
s11_data = pd.read_csv("data/CSV5.csv", skiprows=13, header=None, names=["frequency", "resistance", "reactance", "hf", "label"])
s11 = ((s11_data.resistance/50+1j*s11_data.reactance/50) - 1) / ((s11_data.resistance/50+1j*s11_data.reactance/50) + 1)
s11_net = Network(frequency=s11_data.frequency, s=s11)
plot_data(s11_net)
# %%
s21_data = pd.read_csv("data/CSV6.csv", skiprows=13, header=None, names=["frequency", "resistance", "reactance", "hf", "label"])
s21 = ((s21_data.resistance/50+1j*s21_data.reactance/50) - 1) / ((s21_data.resistance/50+1j*s21_data.reactance/50) + 1)
s21_net = Network(frequency=s21_data.frequency, s=s21)
plot_data(s21_net)
# %%
insertion_loss = np.max(s21_net.s_db)
max_gain_freq = s21_net.f[find_nearest_idx(s21_net.s_db, insertion_loss)]

passband_edge = s21_net.f[find_nearest_idx(s21_net.s_db, insertion_loss-3)]
stopband_start = s21_net.f[find_nearest_idx(s21_net.s_db, insertion_loss-20)]

inband_db = s21_net.s_db[s21_net.f < max_gain_freq]
inband_ripple = np.max(inband_db) - np.min(inband_db)
worst_ripple_freq = s21_net.f[find_nearest_idx(s21_net.s_db, insertion_loss-inband_ripple)]

fig1, ax1 = plt.subplots()
ax1.grid(which='both')

# ax1.plot(s21_net.f, np.ravel(s21_net.s_db), linewidth=2, label="Magnitude DB")
s21_net.plot_s_db(ax=ax1, linewidth=2, label="Magnitude DB")
ax1.get_xaxis().set_major_formatter(matplotlib.ticker.NullFormatter())
ax1.get_xaxis().set_minor_formatter(matplotlib.ticker.ScalarFormatter())
ax1.set_xscale('log')

# ax1.axhline(insertion_loss, label="Insertion Loss")
# ax1.axhline(insertion_loss-inband_ripple, label="Minimum Ripple")
ax1.vlines(max_gain_freq, 0, insertion_loss, label="Insertion Loss", colors='green')
ax1.vlines(worst_ripple_freq, 0, insertion_loss-inband_ripple, label="Minimum Ripple", colors='orange')
ax1.scatter(passband_edge, insertion_loss-3, label="Pass band edge", c='red')

ax1.legend()
plt.show()

print(f"Insertion Loss: {insertion_loss}")
print(f"Pass band Edge: {passband_edge / 1e6} MHz")
print(f"Stop band Start: {stopband_start / 1e6} MHz")
print(f"In band Ripple: {inband_ripple}")
# %%
