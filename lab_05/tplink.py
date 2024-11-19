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
# %%
S21, Gcal, l, r = symbols(r"S21, G_{cal}, \lambda, r")

with evaluate(False):
    Gtx = S21 - Gcal - 20*log(l/(4*pi*r), 10)
display(pprint_eqn(G_tx=Gtx))

gtx_subs = {
    Gcal: 12.49, # dB
    l: 3e8/2.4e9, # C/f
    r: 1.4478 # 57 in -> m
}
Gtx = lambdify([S21], Gtx.subs(gtx_subs))
# %%
angles = np.arange(0, 370, 10)
s21 = []

for deg in angles:
    net = rf.Network(data_path/'tplink'/f'{deg}.S2P')
    s21.append(net["2.4ghz"].s21.s_db.item())

db = Gtx(np.array(s21))
# %%
net.plot_s_db()
plt.grid()
plt.show()
# %% [markdown]
# $$ \Gamma = \frac{Z_l-Z_0}{Z_l+Z_0} \implies Z_l = Z_0 \frac{1+\Gamma}{1-\Gamma} $$
# $$ RL = 20 \log_{10}(|\Gamma|) \implies |\Gamma| = 10^{RL/20}$$
# %%
gamma = np.power(10, net.s21.s_db.flatten() / 20)
Zl = 50 * (1+gamma)/(1-gamma)
plt.plot(net.f, Zl)
plt.grid()
plt.xlabel("Frequency [Hz]")
plt.ylabel("|$Z_l$| [Ohm]")
plt.show()
# %%
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(angles*(np.pi/180), db)
ax.set_theta_offset(np.pi/2)
ax.set_ylim(-30, 10)
ax.set_ylabel("dB")
ax.set_yticks([-30, -20, -10, 0, 10])
plt.show()
# %%
