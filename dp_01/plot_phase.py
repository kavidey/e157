# %%
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import skrf as rf
from skrf import Network
import pandas as pd
import util
# %%
real_pass = pd.read_csv("sim/real.pass.txt", skiprows=1, names=['f', 'S11r', 'S11i', 'S21r', 'S21i'], sep='	|,', engine='python')
real_pass_s21 = Network(frequency=real_pass.f, s=real_pass.S21r + 1j * real_pass.S21i)
real_pass_metrics = util.calc_s21_metrics(real_pass_s21.f, real_pass_s21.s_db)

# %%
ideal_pass = pd.read_csv("sim/ideal.pass.txt", skiprows=1, names=['f', 'S11r', 'S11i', 'S21r', 'S21i'], sep='	|,', engine='python')
ideal_pass_s21 = Network(frequency=ideal_pass.f, s=ideal_pass.S21r + 1j * ideal_pass.S21i)
ideal_pass_metrics = util.calc_s21_metrics(ideal_pass_s21.f, ideal_pass_s21.s_db)
# %%
s21_data_pass = pd.read_csv("data/CSV13.csv", skiprows=13, header=None, names=["frequency", "resistance", "reactance", "hf", "label"])
s21_pass = Network(frequency=s21_data_pass.frequency, s=util.resistance_reactance_to_gamma(s21_data_pass.resistance, s21_data_pass.reactance))
s21_pass_metrics = util.calc_s21_metrics(s21_pass.f, s21_pass.s_db)
# %%
fig1, ax1 = plt.subplots(figsize=(10,8))
ax1.set_xscale('linear')
ax1.grid()
ideal_pass_s21.plot_s_deg(ax=ax1, label='Ideal Simulation', c='b')
edge_idx = util.find_nearest_idx(ideal_pass_s21.f,ideal_pass_metrics['passband_edge'])
ax1.scatter(
    ideal_pass_metrics['passband_edge'],
    ideal_pass_s21.s_deg[edge_idx],
    c='b',
    label=f"{ideal_pass_s21.s_deg[edge_idx][0][0]:.2f} deg at {ideal_pass_metrics['passband_edge']/1e6:.2f} MHz"
)

real_pass_s21.plot_s_deg(ax=ax1, label='Real Simulation', c='orange')
edge_idx = util.find_nearest_idx(real_pass_s21.f,real_pass_metrics['passband_edge'])
ax1.scatter(
    real_pass_metrics['passband_edge'],
    real_pass_s21.s_deg[edge_idx],
    c='orange',
    label=f"{real_pass_s21.s_deg[edge_idx][0][0]:.2f} deg at {real_pass_metrics['passband_edge']/1e6:.2f} MHz"
)

s21_pass.plot_s_deg(ax=ax1, label='Assembled Filter', c='g')
edge_idx = util.find_nearest_idx(s21_pass.f,s21_pass_metrics['passband_edge'])
ax1.scatter(
    s21_pass_metrics['passband_edge'],
    s21_pass.s_deg[edge_idx],
    c='g',
    label=f"{s21_pass.s_deg[edge_idx][0][0]:.2f} deg at {s21_pass_metrics['passband_edge']/1e6:.2f} MHz"
)
ax1.legend()
plt.savefig("report/figures/5.phase.pdf")
# %%
phase_compensation = np.exp(1j * (-s21_pass.f * 2*np.pi)/(3e8*0.66) * 0.0508)
s21_pass.s /= np.expand_dims(phase_compensation, (1,2))

fig1, ax1 = plt.subplots(figsize=(8,6))
ax1.set_xscale('linear')
ax1.grid()
ideal_pass_s21.plot_s_deg(ax=ax1, label='Ideal Simulation', c='b')
edge_idx = util.find_nearest_idx(ideal_pass_s21.f,ideal_pass_metrics['passband_edge'])
ax1.scatter(
    ideal_pass_metrics['passband_edge'],
    ideal_pass_s21.s_deg[edge_idx],
    c='b',
    label=f"{ideal_pass_s21.s_deg[edge_idx][0][0]:.2f} deg at {ideal_pass_metrics['passband_edge']/1e6:.2f} MHz"
)

real_pass_s21.plot_s_deg(ax=ax1, label='Real Simulation', c='orange')
edge_idx = util.find_nearest_idx(real_pass_s21.f,real_pass_metrics['passband_edge'])
ax1.scatter(
    real_pass_metrics['passband_edge'],
    real_pass_s21.s_deg[edge_idx],
    c='orange',
    label=f"{real_pass_s21.s_deg[edge_idx][0][0]:.2f} deg at {real_pass_metrics['passband_edge']/1e6:.2f} MHz"
)

s21_pass.plot_s_deg(ax=ax1, label='Assembled Filter', c='g')
edge_idx = util.find_nearest_idx(s21_pass.f,s21_pass_metrics['passband_edge'])
ax1.scatter(
    s21_pass_metrics['passband_edge'],
    s21_pass.s_deg[edge_idx],
    c='g',
    label=f"{s21_pass.s_deg[edge_idx][0][0]:.2f} deg at {s21_pass_metrics['passband_edge']/1e6:.2f} MHz"
)
ax1.legend()
plt.savefig("report/figures/9.phase_fixed.pdf")
# %%
