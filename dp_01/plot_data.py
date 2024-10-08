# %%
from matplotlib import pyplot as plt
import numpy as np
import skrf as rf
from skrf import Network
import pandas as pd
import matplotlib
import util
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
s11_data = pd.read_csv("data/CSV9.csv", skiprows=13, header=None, names=["frequency", "resistance", "reactance", "hf", "label"])
s11 = ((s11_data.resistance/50+1j*s11_data.reactance/50) - 1) / ((s11_data.resistance/50+1j*s11_data.reactance/50) + 1)
s11_net = Network(frequency=s11_data.frequency, s=s11)
plot_data(s11_net)
# %%
s21_data = pd.read_csv("data/CSV6.csv", skiprows=13, header=None, names=["frequency", "resistance", "reactance", "hf", "label"])
s21 = ((s21_data.resistance/50+1j*s21_data.reactance/50) - 1) / ((s21_data.resistance/50+1j*s21_data.reactance/50) + 1)
s21_net = Network(frequency=s21_data.frequency, s=s21)
plot_data(s21_net)
# %%
util.plot_s21_mag(s21_net)
plt.show()

metrics = util.calc_s21_metrics(s21_net.f, s21_net.s_db)
print(f"Insertion Loss: {metrics['insertion_loss']}")
print(f"Pass band Edge: {metrics['passband_edge'] / 1e6} MHz")
print(f"Stop band Start: {metrics['stopband_start'] / 1e6} MHz")
print(f"In band Ripple: {metrics['inband_ripple']}")
# %%
