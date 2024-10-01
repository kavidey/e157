# %%
from matplotlib import pyplot as plt
import numpy as np
import skrf as rf
from skrf import Network
# %%
base_vna = Network('schematics/p2a.base_vna.s1p')
# base_vna.s = base_vna.s * np.expand_dims(np.linspace(1, 0.9, len(base_vna.s)), (1,2))
base_vna.plot_s_smith(linewidth=3)
# %%
vna_open = Network('schematics/p2a.vna_open.s1p')
# vna_open.s = vna_open.s * np.expand_dims(np.linspace(1, 0.9, len(vna_open.s)), (1,2))
vna_open.plot_s_smith(linewidth=3)
# %%
vna_matched = Network('schematics/p2a.vna_matched.s1p')
# vna_matched.s = vna_matched.s * np.expand_dims(np.linspace(1, 0.9, len(vna_matched.s)), (1,2))
vna_matched.plot_s_smith(linewidth=3)
# %%
vna_short = Network('schematics/p2a.vna_short.s1p')
# vna_short.s = vna_short.s * np.expand_dims(np.linspace(1, 0.9, len(vna_short.s)), (1,2))
vna_short.plot_s_smith(linewidth=3)
# %%
vna_short_10m = Network('schematics/p2a.vna_short.10m.s1p')
vna_short_10m.s = vna_short_10m.s * np.expand_dims(np.linspace(1, 0.9, vna_short_10m.s.shape[0]), (1,2))
vna_short_10m.plot_s_smith(linewidth=2)
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
t_match.plot_s_smith()
# %%
