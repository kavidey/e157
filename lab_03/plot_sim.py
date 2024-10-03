# %%
from matplotlib import pyplot as plt
import numpy as np
import skrf as rf
from skrf import Network
# %%
def plot_data(network):
    fig, axes = plt.subplots(1,3, figsize=(12,3), layout="constrained")
    network.plot_s_db(ax=axes[0], linewidth=3)
    network.plot_s_deg(ax=axes[1], linewidth=3)
    network.plot_s_smith(ax=axes[2], linewidth=3)
# %%
### UNCALIBRATED
# %%
base_vna = Network('schematics/p2a.base_vna.s1p')
base_vna.plot_s_smith(linewidth=3)
# %%
vna_open = Network('schematics/p2a.vna_open.s1p')
# vna_open.s *= np.exp(1j * 60 * np.pi/180)
vna_open.plot_s_smith(linewidth=3)
# vna_open.plot_s_deg()
# %%
vna_matched = Network('schematics/p2a.vna_matched.s1p')
vna_matched.plot_s_smith(linewidth=3)
# %%
vna_short = Network('schematics/p2a.vna_short.s1p')
# vna_short.s *= np.exp(1j * 60 * np.pi/180)
vna_short.plot_s_smith(linewidth=3)
# vna_short.plot_s_deg()
# %%
vna_short_10m = Network('schematics/p2a.vna_short.10m.s1p')
vna_short_10m.s = vna_short_10m.s * np.expand_dims(np.linspace(1, 0.9, vna_short_10m.s.shape[0]), (1,2))
vna_short_10m.plot_s_smith(linewidth=2)
# %%
### CALIBRATED
# %%
vna_open = Network('schematics/p2a.vna_open.s1p')
phase_compensation = - np.exp(1j * (-2 * vna_open.f * 2*np.pi)/(3e8*0.8))
vna_open.s /= np.expand_dims(phase_compensation, (1,2))
plot_data(vna_open)
# %%
vna_matched = Network('schematics/p2a.vna_matched.s1p')
phase_compensation = - np.exp(1j * (-2 * vna_matched.f * 2*np.pi)/(3e8*0.8))
vna_matched.s /= np.expand_dims(phase_compensation, (1,2))
plot_data(vna_matched)
# %%
vna_short = Network('schematics/p2a.vna_short.s1p')
phase_compensation = - np.exp(1j * (-2 * vna_short.f * 2*np.pi)/(3e8*0.8))
vna_short.s /= np.expand_dims(phase_compensation, (1,2))
plot_data(vna_short)
# %%
vna_short_10m = Network('schematics/p2a.vna_short.10m.s1p')
phase_compensation = - np.exp(1j * 10 * (-2 * vna_short_10m.f * 2*np.pi)/(3e8*0.8))
vna_short_10m.s /= np.expand_dims(phase_compensation, (1,2))
plot_data(vna_short_10m)
# %%
lmatch_none = Network('l_match/p3.no_match.s1p')
lmatch_none.plot_s_smith(linewidth=3)
# %%
lmatch_l = Network('l_match/p3.l.s1p')
lmatch_l.plot_s_smith(linewidth=3)
# %%
lmatch_lc = Network('l_match/p3.lc.s1p')
lmatch_lc.plot_s_smith(linewidth=3)
# %%
lmatch_lc_parasitic = Network('l_match/p3.lc_parasitic.s1p')
lmatch_lc_parasitic.plot_s_smith()
# %%
t_match = Network('t_match/p5.t_match.s1p')
# t_match.plot_s_smith()
plot_data(t_match)
# %%
