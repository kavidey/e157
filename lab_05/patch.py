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
    r: 1.4478 # 57 in -> m
}
Gtx = lambdify([S21, Gcal, l], Gtx.subs(gtx_subs))
# %%
angles_1455mhz = np.arange(0, 360, 20)
s21_1455mhz = []

for deg in angles_1455mhz:
    net_1455mhz = rf.Network(data_path/'patch'/'1455_mhz'/f'{deg}.S1P')
    s21_1455mhz.append(net_1455mhz["1455mhz"].s_db.item())

s21_728mhz = []
angles_728mhz = np.array([0, 20, 40, 60, 80, 90, 100, 120, 140, 160, 180, 200, 220, 240, 260, 270, 280, 300, 320, 340, 0])
for deg in angles_728mhz:
    net_728mhz = rf.Network(data_path/'patch'/'728_mhz'/f'{deg}.S2P')
    s21_728mhz.append(net_728mhz["728.155mhz"].s21.s_db.item())

db_1455mhz = Gtx(np.array(s21_1455mhz), 10.93, 3e8/1455e6)
db_728mhz = Gtx(np.array(s21_728mhz), 4.51, 3e8/728.155e6)
# %%
net_1455mhz.plot_s_db()
plt.grid()
# %%
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(angles_1455mhz*(np.pi/180), db_1455mhz)
ax.set_theta_offset(np.pi/2)
ax.set_ylabel("dB")
plt.show()
# %%
net_728mhz.plot_s_db()
plt.grid()
# %%
gamma = np.power(10, net_728mhz.s11.s_db.flatten() / 20)
Zl = 50 * (1+gamma)/(1-gamma)
plt.plot(net_728mhz.f, Zl)
plt.grid()
plt.xlabel("Frequency [Hz]")
plt.ylabel("|$Z_l$| [Ohm]")
plt.show()
# %%
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(angles_728mhz*(np.pi/180), db_728mhz)
ax.set_theta_offset(np.pi/2)
ax.set_ylabel("dB")
ax.set_yticks([-25, -20, -15, -10, -5, 0])
plt.show()

# %%
