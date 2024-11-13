# %%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path
from sympy import symbols, sqrt, Lambda, evaluate, lambdify, Eq, Symbol, pi
from IPython.display import display

data_path = Path("data")

def pprint_eqn(**kwargs):
    name = list(kwargs.keys())[0]
    return Eq(Symbol(name), kwargs[name], evaluate=False)
# %%
mu0, i, R = symbols(r"\mu_0, i, R")
with evaluate(False):
    B_wire = (mu0*i)/(2*pi * R)
display(pprint_eqn(B=B_wire))

wire_subs = {
    mu0: 4*np.pi * 10e-7, # H/m
}
wire_field = lambdify([i, R], B_wire.subs(wire_subs))
# %%
infinite_wire_data = pd.read_excel(data_path/"lab_data.xlsx", sheet_name="infinite_wire")
infinite_wire_data["Distance [m]"] = infinite_wire_data["Distance [cm]"]/100
# f_response_data['B Field [uT]'] = wire_field(f_response_data["Current [mA]"]/1e3)*1e6
# f_response_data["Power [mW]"] = np.power(10, f_response_data["Power [dBm]"]/10)*1e3

wire_current = 10/(1.96e3) # 20 Vpp / 1.96 kOhm

t20_fit_5mhz = {
    "slope": 9.55,
    "intercept": -49.22
}

t20_fit_100khz = {
    "slope": 12.35,
    "intercept": -75.88
}

t20_fit_constant_field = {
    "slope": 8.36,
    "intercept": -125.19
}
calibration_field = 25.79 # uT

dists = np.linspace(0.001, 0.3, 1000)
fields = wire_field(wire_current, dists)
# %%
plt.plot(dists, fields*1e6, label="Predicted Field")

field_5mhz = np.exp((infinite_wire_data[infinite_wire_data["Frequency [Hz]"]==5e6]["Power [dBm]"] - t20_fit_5mhz["intercept"]) / t20_fit_5mhz["slope"])
plt.plot(infinite_wire_data[infinite_wire_data["Frequency [Hz]"]==5e6]["Distance [m]"], field_5mhz, label="5 MHz")

field_100khz = np.exp((infinite_wire_data[infinite_wire_data["Frequency [Hz]"]==100e3]["Power [dBm]"] - t20_fit_100khz["intercept"]) / t20_fit_100khz["slope"])
plt.plot(infinite_wire_data[infinite_wire_data["Frequency [Hz]"]==100e3]["Distance [m]"], field_100khz, label="100 kHz")

# expected_db = np.log(500e3) * t20_fit_constant_field["slope"] + t20_fit_constant_field["intercept"]
# db_difference = expected_db-infinite_wire_data[infinite_wire_data["Frequency [Hz]"]==500e3]["Power [dBm]"]
# field_500khz = np.exp(np.log(calibration_field) - db_difference/t20_fit_5mhz["slope"])
# plt.plot(infinite_wire_data[infinite_wire_data["Frequency [Hz]"]==500e3]["Distance [m]"], field_500khz, label="500 kHz")

plt.grid()
plt.xlabel("Distance [m]")
plt.ylabel("B Field [$\mu$T]")
plt.legend()
plt.ylim(0, 4)
# %%
