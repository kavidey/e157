# %%
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
from pathlib import Path
from sympy import symbols, sqrt, Lambda, evaluate, lambdify, Eq, Symbol, solve
from IPython.display import display
from scipy.stats import linregress

data_path = Path("data")

def pprint_eqn(**kwargs):
    name = list(kwargs.keys())[0]
    return Eq(Symbol(name), kwargs[name], evaluate=False)
# %%
vout, vin, R, j, omega, L, Z = symbols(r"V_{out} V_{in} R j \omega L Z")
eqn = Eq(vout, vin * Z/(R+Z))
display(eqn)
L_sol = solve(eqn, Z)[0]
display(pprint_eqn(Z=L_sol))

L_subs = {
    R: 98.4 + 5, # Ohm + 5 for coil resistance
}
Z_eqn = lambdify([vout, vin], L_sol.subs(L_subs))
# %%
helmholz_impedance_data = pd.read_excel(data_path/"lab_data.xlsx", sheet_name="helmholz_impedance")
helmholz_impedance_data["Impedance"] = Z_eqn(np.minimum(9.64, helmholz_impedance_data["Vout [V]"]), helmholz_impedance_data["Vin [V]"])
# %%
plt.plot(helmholz_impedance_data["Frequency [Hz]"], np.log10(helmholz_impedance_data["Impedance"]))
# plt.plot(helmholz_impedance_data["Frequency [Hz]"], helmholz_impedance_data["Vout [V]"]*1000)
plt.xscale("log")
plt.grid(which="both")
plt.xlabel("Frequency [Hz]")
plt.ylabel("log(Impedance [$\Omega$])")
# %%
