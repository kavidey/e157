# %%
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
from pathlib import Path
from sympy import symbols, sqrt, Lambda, evaluate, lambdify, Eq, Symbol, log, pi
from IPython.display import display
import skrf as rf

data_path = Path("data")

def pprint_eqn(**kwargs):
    name = list(kwargs.keys())[0]
    return Eq(Symbol(name), kwargs[name], evaluate=False)

def find_nearest_idx(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx
# %%
S21, Gcal, l, r = symbols(r"S21, G_{cal}, \lambda, r")

with evaluate(False):
    Gtx = S21 - Gcal - 20*log(l/(4*pi*r), 10)
display(pprint_eqn(G_tx=Gtx))

gtx_subs = {
    Gcal: 12.97, # dB
    l: 3e8/2276e6, # C/f
    r: 1.4478 # 57 in -> m
}
Gtx = lambdify([S21], Gtx.subs(gtx_subs))
# %%
angles = np.array([0, 20, 40, 60, 80, 90, 100, 120, 140, 160, 180, 200, 220, 240, 260, 270, 280, 300, 320, 340, 0])
s21 = []

for deg in angles:
    net = rf.Network(data_path/f'{deg}.S1P')
    s21.append(net["2276mhz"].s_db.item())

net = rf.Network(data_path/'0.S2P', name="H-A16SD")
db = Gtx(np.array(s21))
# %%
net.plot_s_db()
plt.grid()
plt.savefig("../report/figures/antenna.sparams.pdf")
plt.show()
# %% [markdown]
# $$ \Gamma = \frac{Z_l-Z_0}{Z_l+Z_0} \implies Z_l = Z_0 \frac{1+\Gamma}{1-\Gamma} $$
# $$ RL = 20 \log_{10}(|\Gamma|) \implies |\Gamma| = 10^{RL/20}$$
# %%
gamma = np.power(10, net.s11.s_db.flatten() / 20)
Zl = 50 * (1+gamma)/(1-gamma)
plt.plot(net.f, Zl)
plt.grid()
plt.xlabel("Frequency [Hz]")
plt.ylabel("|$Z_l$| [Ohm]")
plt.ylim(-100, 1000)
plt.show()
idx = find_nearest_idx(net.f, 2276e6)
print(f"S11 at 2276 MHz: {net.s11.s_db[idx][0][0]:.2f}")
print(f"Gamma at 2276 MHz: {gamma[idx]:.2f}")
print(f"Impedance at 2276 MHz: {Zl[idx]:.2f}")
# %%
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(angles*(np.pi/180), db)
ax.set_theta_offset(np.pi/2)
ax.set_ylabel("dB")
plt.savefig("../report/figures/antenna.radiation.pdf")
plt.show()
print(f"Antenna Directivity: {np.max(db):.2f}")
# %%
