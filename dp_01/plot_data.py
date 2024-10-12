# %%
from matplotlib import pyplot as plt
import numpy as np
import skrf as rf
from skrf import Network
import pandas as pd
import matplotlib
import util
# %%
s11_data_dc_stop = pd.read_csv("data/CSV9.csv", skiprows=13+2, header=None, names=["frequency", "resistance", "reactance", "hf", "label"])
s11_dc_stop = Network(frequency=s11_data_dc_stop.frequency, s=util.resistance_reactance_to_gamma(s11_data_dc_stop.resistance, s11_data_dc_stop.reactance))
util.plot_network(s11_dc_stop)
# %%
s21_data_dc_stop = pd.read_csv("data/CSV10.csv", skiprows=13+2, header=None, names=["frequency", "resistance", "reactance", "hf", "label"])
s21_dc_stop = Network(frequency=s21_data_dc_stop.frequency, s=util.resistance_reactance_to_gamma(s21_data_dc_stop.resistance, s21_data_dc_stop.reactance))
util.plot_network(s21_dc_stop)
# %%
s21_data_pass = pd.read_csv("data/CSV13.csv", skiprows=13, header=None, names=["frequency", "resistance", "reactance", "hf", "label"])
s21_pass = Network(frequency=s21_data_pass.frequency, s=util.resistance_reactance_to_gamma(s21_data_pass.resistance, s21_data_pass.reactance))
util.plot_network(s21_pass)
# %%
fig1, ax1 = plt.subplots()
s21_dc_stop.plot_s_db(ax=ax1, label=None)
ax1.set_xscale('log')
ax1.grid(which='both')
metrics = util.calc_s21_metrics(s21_dc_stop.f, s21_dc_stop.s_db)
util.plot_s21_dc_stop_metrics(ax1, metrics)
plt.savefig("report/figures/6.assembled.pdf")

stop_band_idx = util.find_nearest_idx(s21_dc_stop.f, metrics['stopband_start'])
print(f"Frequency Resolution @ Stop band: {(s21_dc_stop.f[stop_band_idx+1] - s21_dc_stop.f[stop_band_idx-1]) / 1e6} MHz")
# %%
fig1, ax1 = plt.subplots()
s21_pass.plot_s_db(ax=ax1, label=None)
ax1.set_xscale("linear")
ax1.grid(which='both')

idx_50_mhz = util.find_nearest_idx(s21_pass.f, 50e6)
loss_50_mhz = s21_pass.s_db[idx_50_mhz][0,0]

ax1.vlines(50e6, 0+0.03, loss_50_mhz, label=f"50 MHz Attenuation: {-loss_50_mhz:.2f} dB", colors='purple', linewidth=3)
ax1.scatter([50e6, 50e6], [0+0.03, loss_50_mhz-0.03], color='purple', marker="_", s=50, zorder=5)

util.plot_s21_pass_metrics(ax1, util.calc_s21_metrics(s21_pass.f, s21_pass.s_db, provided_insertion_loss=metrics['insertion_loss']), insertion_loss=metrics['insertion_loss'])

plt.savefig("report/figures/4.assembled.pdf")
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
