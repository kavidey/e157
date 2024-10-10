# %%
from matplotlib import pyplot as plt
import numpy as np
import skrf as rf
from skrf import Network
import pandas as pd
import matplotlib
import util
# %%
def resistance_reactance_to_gamma(resistance, reactance):
    return ((resistance/50+1j*reactance/50) - 1) / ((resistance/50+1j*reactance/50) + 1)
# %%
s11_data_dc_stop = pd.read_csv("data/CSV9.csv", skiprows=13, header=None, names=["frequency", "resistance", "reactance", "hf", "label"])
s11_dc_stop = Network(frequency=s11_data_dc_stop.frequency, s=resistance_reactance_to_gamma(s11_data_dc_stop.resistance, s11_data_dc_stop.reactance))
util.plot_network(s11_dc_stop)
# %%
s21_data_dc_stop = pd.read_csv("data/CSV10.csv", skiprows=13, header=None, names=["frequency", "resistance", "reactance", "hf", "label"])
s21_dc_stop = Network(frequency=s21_data_dc_stop.frequency, s=resistance_reactance_to_gamma(s21_data_dc_stop.resistance, s21_data_dc_stop.reactance))
util.plot_network(s21_dc_stop)
# %%
s21_data_pass = pd.read_csv("data/CSV13.csv", skiprows=13, header=None, names=["frequency", "resistance", "reactance", "hf", "label"])
s21_pass = Network(frequency=s21_data_pass.frequency, s=resistance_reactance_to_gamma(s21_data_pass.resistance, s21_data_pass.reactance))
util.plot_network(s21_pass)
# %%
fig1, ax1 = plt.subplots()
s21_pass.plot_s_db(ax=ax1, label=None)
ax1.set_xscale("linear")
ax1.grid(which='both')
util.plot_s21_metrics(ax1, util.calc_s21_metrics(s21_pass.f, s21_pass.s_db))
plt.savefig("report/figures/4.assembled.png")
# %%
fig1, ax1 = plt.subplots()
s21_dc_stop.plot_s_db(ax=ax1, label=None)
ax1.set_xscale('log')
ax1.grid(which='both')
util.plot_s21_metrics(ax1, util.calc_s21_metrics(s21_dc_stop.f, s21_dc_stop.s_db), skip_ripple=True, skip_stopband=False)
plt.savefig("report/figures/6.assembled.png")
# %%
fig1, ax1 = plt.subplots()
s11_dc_stop.plot_s_db(ax=ax1, label=None)
ax1.set_xscale('log')
ax1.grid(which='both')

passband_freq = util.calc_s21_metrics(s21_pass.f, s21_pass.s_db)['passband_edge']
stopband_freq = util.calc_s21_metrics(s21_dc_stop.f, s21_dc_stop.s_db)['stopband_start']

ax1.scatter(passband_freq, s11_dc_stop.s_db[util.find_nearest_idx(s11_dc_stop.f, passband_freq)], c='red', zorder=10, label=f"Pass band edge: {passband_freq / 1e6:.2f} MHz")
ax1.scatter(stopband_freq, s11_dc_stop.s_db[util.find_nearest_idx(s11_dc_stop.f, stopband_freq)], c='orange', zorder=10, label=f"Stop band edge: {stopband_freq / 1e6:.2f} MHz")

ax1.legend()
plt.savefig("report/figures/7.assembled.png")
# %%
s11_dc_stop.plot_s_smith(label=None)
plt.savefig("report/figures/8.s11.assembled.png")
# %%
s21_dc_stop.plot_s_smith(label=None)
plt.savefig("report/figures/8.s21.assembled.png")
# %%
