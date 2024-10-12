# %%
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import skrf as rf
from skrf import Network
import pandas as pd
import util
# %%
ideal_dcstop = pd.read_csv("sim/ideal.dc_to_stop.txt", skiprows=1, names=['f', 'S11r', 'S11i', 'S21r', 'S21i'], sep='	|,', engine='python')

ideal_dcstop_s11 = Network(frequency=ideal_dcstop.f, s=ideal_dcstop.S11r + 1j * ideal_dcstop.S11i)
ideal_dcstop_s21 = Network(frequency=ideal_dcstop.f, s=ideal_dcstop.S21r + 1j * ideal_dcstop.S21i)

util.plot_network(ideal_dcstop_s21)
# %%
ideal_pass = pd.read_csv("sim/ideal.pass.txt", skiprows=1, names=['f', 'S11r', 'S11i', 'S21r', 'S21i'], sep='	|,', engine='python')

ideal_pass_s11 = Network(frequency=ideal_pass.f, s=ideal_pass.S11r + 1j * ideal_pass.S11i)
ideal_pass_s21 = Network(frequency=ideal_pass.f, s=ideal_pass.S21r + 1j * ideal_pass.S21i)

util.plot_network(ideal_pass_s21)
# %%
real_dcstop = pd.read_csv("sim/real.dc_to_stop.txt", skiprows=1, names=['f', 'S11r', 'S11i', 'S21r', 'S21i'], sep='	|,', engine='python')

real_dcstop_s11 = Network(frequency=real_dcstop.f, s=real_dcstop.S11r + 1j * real_dcstop.S11i)
real_dcstop_s21 = Network(frequency=real_dcstop.f, s=real_dcstop.S21r + 1j * real_dcstop.S21i)

util.plot_network(real_dcstop_s21)
# %%
real_pass = pd.read_csv("sim/real.pass.txt", skiprows=1, names=['f', 'S11r', 'S11i', 'S21r', 'S21i'], sep='	|,', engine='python')

real_pass_s11 = Network(frequency=real_pass.f, s=real_pass.S11r + 1j * real_pass.S11i)
real_pass_s21 = Network(frequency=real_pass.f, s=real_pass.S21r + 1j * real_pass.S21i)

util.plot_network(real_pass_s21)
# %%
fig1, ax1 = plt.subplots()
real_dcstop_s21.plot_s_db(ax=ax1, label=None)
ax1.set_xscale('log')
ax1.grid(which='both')
ideal_metrics = util.calc_s21_metrics(real_dcstop_s21.f, real_dcstop_s21.s_db)
util.plot_s21_dc_stop_metrics(ax1, ideal_metrics)
plt.savefig("report/figures/6.real.pdf")
# %%
fig1, ax1 = plt.subplots()
ideal_dcstop_s21.plot_s_db(ax=ax1, label=None)
ax1.set_xscale('log')
ax1.grid(which='both')
real_metrics = util.calc_s21_metrics(ideal_dcstop_s21.f, ideal_dcstop_s21.s_db)
util.plot_s21_dc_stop_metrics(ax1, real_metrics)
plt.savefig("report/figures/6.ideal.pdf")
# %%
fig1, ax1 = plt.subplots()
ideal_pass_s21.plot_s_db(ax=ax1, label=None)
ax1.set_xscale("linear")
ax1.grid(which='both')
util.plot_s21_pass_metrics(ax1, util.calc_s21_metrics(ideal_pass_s21.f, ideal_pass_s21.s_db, provided_insertion_loss=ideal_metrics['insertion_loss']), ideal_metrics['insertion_loss'])
plt.savefig("report/figures/4.ideal.pdf")
# %%
fig1, ax1 = plt.subplots()
real_pass_s21.plot_s_db(ax=ax1, label=None)
ax1.set_xscale("linear")
ax1.grid(which='both')
util.plot_s21_pass_metrics(ax1, util.calc_s21_metrics(real_pass_s21.f, real_pass_s21.s_db, provided_insertion_loss=real_metrics['insertion_loss']), real_metrics['insertion_loss'])
plt.savefig("report/figures/4.real.pdf")
# %%
fig1, ax1 = plt.subplots()
ideal_dcstop_s11.plot_s_db(ax=ax1, label=None)
ax1.set_xscale('log')
ax1.grid(which='both')

passband_freq = util.calc_s21_metrics(ideal_pass_s21.f, ideal_pass_s21.s_db)['passband_edge']
stopband_freq = util.calc_s21_metrics(ideal_dcstop_s21.f, ideal_dcstop_s21.s_db)['stopband_start']

passband_db = ideal_pass_s11.s_db[util.find_nearest_idx(ideal_pass_s11.f, passband_freq)]
ax1.scatter(
    passband_freq,
    passband_db,
    c='red', zorder=10,
    label=f"Pass band edge: {passband_db[0,0]:.2f} dB at {passband_freq / 1e6:.2f} MHz"
)
stopband_db = ideal_pass_s11.s_db[util.find_nearest_idx(ideal_pass_s11.f, stopband_freq)]
ax1.scatter(
    stopband_freq,
    stopband_db,
    c='orange', zorder=10,
    label=f"Stop band edge: {stopband_db[0,0]:.2f} dB at {stopband_freq / 1e6:.2f} MHz"
)

ax1.legend()
plt.savefig("report/figures/7.ideal.pdf")
# %%
fig1, ax1 = plt.subplots()
real_dcstop_s11.plot_s_db(ax=ax1, label=None)
ax1.set_xscale('log')
ax1.grid(which='both')

passband_freq = util.calc_s21_metrics(real_pass_s21.f, real_pass_s21.s_db)['passband_edge']
stopband_freq = util.calc_s21_metrics(real_dcstop_s21.f, real_dcstop_s21.s_db)['stopband_start']

passband_db = real_pass_s11.s_db[util.find_nearest_idx(real_pass_s11.f, passband_freq)]
ax1.scatter(
    passband_freq,
    passband_db,
    c='red', zorder=10,
    label=f"Pass band edge: {passband_db[0,0]:.2f} dB at {passband_freq / 1e6:.2f} MHz"
)
stopband_db = real_pass_s11.s_db[util.find_nearest_idx(real_pass_s11.f, stopband_freq)]
ax1.scatter(
    stopband_freq,
    stopband_db,
    c='orange', zorder=10,
    label=f"Stop band edge: {stopband_db[0,0]:.2f} dB at {stopband_freq / 1e6:.2f} MHz"
)

ax1.legend()
plt.savefig("report/figures/7.real.pdf")
# %%
ideal_dcstop_s11.plot_s_smith(show_legend=False)
plt.savefig("report/figures/8.s11.ideal.pdf")
# %%
ideal_dcstop_s21.plot_s_smith(show_legend=False)
plt.savefig("report/figures/8.s21.ideal.pdf")
# %%
real_dcstop_s11.plot_s_smith(show_legend=False)
plt.savefig("report/figures/8.s11.real.pdf")
# %%
real_dcstop_s21.plot_s_smith(show_legend=False)
plt.savefig("report/figures/8.s21.real.pdf")
# %%