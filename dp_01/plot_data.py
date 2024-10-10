# %%
from matplotlib import pyplot as plt
import numpy as np
import skrf as rf
from skrf import Network
import pandas as pd
import matplotlib
import util
# %%
s11_data_dc_stop = pd.read_csv("data/CSV9.csv", skiprows=13, header=None, names=["frequency", "resistance", "reactance", "hf", "label"])
s11_dc_stop = Network(frequency=s11_data_dc_stop.frequency, s=util.resistance_reactance_to_gamma(s11_data_dc_stop.resistance, s11_data_dc_stop.reactance))
util.plot_network(s11_dc_stop)
# %%
s21_data_dc_stop = pd.read_csv("data/CSV10.csv", skiprows=13, header=None, names=["frequency", "resistance", "reactance", "hf", "label"])
s21_dc_stop = Network(frequency=s21_data_dc_stop.frequency, s=util.resistance_reactance_to_gamma(s21_data_dc_stop.resistance, s21_data_dc_stop.reactance))
util.plot_network(s21_dc_stop)
# %%
s21_data_pass = pd.read_csv("data/CSV13.csv", skiprows=13, header=None, names=["frequency", "resistance", "reactance", "hf", "label"])
s21_pass = Network(frequency=s21_data_pass.frequency, s=util.resistance_reactance_to_gamma(s21_data_pass.resistance, s21_data_pass.reactance))
util.plot_network(s21_pass)
# %%
fig1, ax1 = plt.subplots()
s21_pass.plot_s_db(ax=ax1, label=None)
ax1.set_xscale("linear")
ax1.grid(which='both')
util.plot_s21_metrics(ax1, util.calc_s21_metrics(s21_pass.f, s21_pass.s_db))
plt.savefig("report/figures/4.assembled.pdf")
# %%
fig1, ax1 = plt.subplots()
s21_dc_stop.plot_s_db(ax=ax1, label=None)
ax1.set_xscale('log')
ax1.grid(which='both')
util.plot_s21_metrics(ax1, util.calc_s21_metrics(s21_dc_stop.f, s21_dc_stop.s_db), skip_ripple=True, skip_stopband=False)
plt.savefig("report/figures/6.assembled.pdf")
# %%
fig1, ax1 = plt.subplots()
s11_dc_stop.plot_s_db(ax=ax1, label=None)
ax1.set_xscale('log')
ax1.grid(which='both')

passband_freq = util.calc_s21_metrics(s21_pass.f, s21_pass.s_db)['passband_edge']
stopband_freq = util.calc_s21_metrics(s21_dc_stop.f, s21_dc_stop.s_db)['stopband_start']

passband_db = s11_dc_stop.s_db[util.find_nearest_idx(s11_dc_stop.f, passband_freq)]
ax1.scatter(
    passband_freq,
    passband_db,
    c='red', zorder=10,
    label=f"Pass band edge: {passband_db[0,0]:.2f} dB at {passband_freq / 1e6:.2f} MHz"
)
stopband_db = s11_dc_stop.s_db[util.find_nearest_idx(s11_dc_stop.f, stopband_freq)]
ax1.scatter(
    stopband_freq,
    stopband_db,
    c='orange', zorder=10,
    label=f"Stop band edge: {stopband_db[0,0]:.2f} dB at {stopband_freq / 1e6:.2f} MHz"
)

ax1.legend()
plt.savefig("report/figures/7.assembled.pdf")
# %%
s11_dc_stop.plot_s_smith(show_legend=False)
plt.savefig("report/figures/8.s11.assembled.pdf")
# %%
s21_dc_stop.plot_s_smith(show_legend=False)
plt.savefig("report/figures/8.s21.assembled.pdf")
# %%
