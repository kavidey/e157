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
angles = np.arange(0, 370, 20)
s21_1455mhz = []
s21_728mhz = []

for deg in angles:
    net_1455mhz = rf.Network(data_path/'patch'/'1455_mhz'/f'{deg}.S1P')
    s21_1455mhz.append(net_1455mhz["2.4ghz"].s_db.item())

    net_728mhz = rf.Network(data_path/'patch'/'1455_mhz'/f'{deg}.S1P')
    s21_728mhz.append(net_728mhz["2.4ghz"].s_db.item())

db_1455mhz = Gtx(np.array(s21_1455mhz))
db_728mhz = Gtx(np.array(s21_728mhz))
# %%
net_1455mhz.plot_s_db()
plt.grid()
# %%
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(angles*(np.pi/180), db_1455mhz)
ax.set_theta_offset(np.pi/2)
ax.set_ylabel("dB")
plt.show()
# %%
net_728mhz.plot_s_db()
plt.grid()
# %%
gamma = np.power(10, net_728mhz.s_db.flatten() / 20)
Zl = 50 * (1+gamma)/(1-gamma)
plt.plot(net_728mhz.f, Zl)
plt.grid()
plt.xlabel("Frequency [Hz]")
plt.ylabel("|$Z_l$| [Ohm]")
plt.show()
# %%
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(angles*(np.pi/180), db_728mhz)
ax.set_theta_offset(np.pi/2)
ax.set_ylabel("dB")
plt.show()

# %%
