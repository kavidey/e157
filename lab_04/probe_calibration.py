# %%
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
from pathlib import Path
from sympy import symbols, sqrt, Lambda, evaluate, lambdify, Eq, Symbol
from IPython.display import display
from scipy.stats import linregress

data_path = Path("data")

def pprint_eqn(**kwargs):
    name = list(kwargs.keys())[0]
    return Eq(Symbol(name), kwargs[name], evaluate=False)
# %%
mu0, i, N, R = symbols(r"\mu_0, i, N, R")
with evaluate(False):
    B_helmholz = (mu0*8*i*N)/(5*sqrt(5) * R)
display(pprint_eqn(B=B_helmholz))

helmholz_subs = {
    mu0: 4*np.pi * 1e-7, # H/m
    N: 75,
    R: 1e-2*(2.51)/2, # cm
}
helmholz_field = lambdify(i, B_helmholz.subs(helmholz_subs))
# %%
low_f_data = pd.read_excel(data_path/"lab_data.xlsx", sheet_name="low_f")
low_f_data['B Field [uT]'] = helmholz_field(low_f_data["Current [mA]"]/1e3)*1e6
low_f_data["Power [mW]"] = np.power(10, low_f_data["Power [dBm]"]/10)*1e3

f_response_data = pd.read_excel(data_path/"lab_data.xlsx", sheet_name="f_response")
f_response_data['B Field [uT]'] = helmholz_field(f_response_data["Current [mA]"]/1e3)*1e6
f_response_data["Power [mW]"] = np.power(10, f_response_data["Power [dBm]"]/10)*1e3
# %%
fig, axs = plt.subplots(1, 2, figsize=(8,4))
fig.suptitle("100 kHz", fontsize=16)

for key, grp in low_f_data[low_f_data["Frequency [Hz]"] == 100e3].groupby(['Probe']):
    grp.plot(ax=axs[0], kind='line', x='B Field [uT]', y='Power [dBm]', label=key[0])

axs[0].grid()
axs[0].set_xlabel("B Field [$\mu$T]")
axs[0].set_ylabel("Output Power [dBm]")

for key, grp in low_f_data[low_f_data["Frequency [Hz]"] == 100e3].groupby(['Probe']):
    grp.plot(ax=axs[1], kind='line', x='B Field [uT]', y='Power [mW]', label=key[0])

axs[1].grid()
axs[1].set_xlabel("B Field [$\mu$T]")
axs[1].set_ylabel("Output Power [mW]")
plt.show()
# %%
fig, axs = plt.subplots(1, 2, figsize=(8,4))
fig.suptitle("5 MHz", fontsize=16)

for key, grp in low_f_data[low_f_data["Frequency [Hz]"] == 5e6].groupby(['Probe']):
    grp.plot(ax=axs[0], kind='line', x='B Field [uT]', y='Power [dBm]', label=key[0])

axs[0].grid()
axs[0].set_xlabel("B Field [$\mu$T]")
axs[0].set_ylabel("Output Power [dBm]")

for key, grp in low_f_data[low_f_data["Frequency [Hz]"] == 5e6].groupby(['Probe']):
    grp.plot(ax=axs[1], kind='line', x='B Field [uT]', y='Power [mW]', label=key[0])

axs[1].grid()
axs[1].set_xlabel("B Field [$\mu$T]")
axs[1].set_ylabel("Output Power [mW]")
plt.show()
# %%
fig, axs = plt.subplots(1, 2, figsize=(10,4))

fit_5mhz = {}

for key, grp in low_f_data[low_f_data["Frequency [Hz]"] == 5e6].groupby(['Probe']):
    grp.plot(ax=axs[0], kind='line', x='B Field [uT]', y='Power [dBm]', label=key[0])
    fit_5mhz[key[0]] = linregress(np.log(grp['B Field [uT]']), grp['Power [dBm]'])

axs[0].set_xlabel("B Field [$\mu$T]")
axs[0].set_ylabel("Output Power [dBm]")
axs[0].set_title("Response at 5 MHz")
axs[0].set_xscale('log')
axs[0].grid(which='both')
axs[0].get_xaxis().set_major_formatter(matplotlib.ticker.NullFormatter())
axs[0].get_xaxis().set_minor_formatter(matplotlib.ticker.ScalarFormatter())

fit_100khz = {}

for key, grp in low_f_data[low_f_data["Frequency [Hz]"] == 100e3].groupby(['Probe']):
    grp.plot(ax=axs[1], kind='line', x='B Field [uT]', y='Power [dBm]', label=key[0])
    fit_100khz[key[0]] = linregress(np.log(grp['B Field [uT]']), grp['Power [dBm]'])

axs[1].set_xlabel("B Field [$\mu$T]")
axs[1].set_ylabel("Output Power [dBm]")
axs[1].set_title("Response at 100 kHz")
axs[1].set_xscale('log')
axs[1].grid(which='both')
axs[1].get_xaxis().set_major_formatter(matplotlib.ticker.NullFormatter())
axs[1].get_xaxis().set_minor_formatter(matplotlib.ticker.ScalarFormatter())
plt.show()
# %%
regression_db = []

for probe in fit_5mhz.keys():
    regression_db.append([probe, "5 MHz", np.round(fit_5mhz[probe].slope,2), np.round(fit_5mhz[probe].intercept, 2)])

for probe in fit_100khz.keys():
    regression_db.append([probe, "100 kHz", np.round(fit_100khz[probe].slope,2), np.round(fit_100khz[probe].intercept, 2)])

print(pd.DataFrame(regression_db, columns=["Probe", "Frequency", "Slope", "Intercept"]).to_markdown(index=False, tablefmt="grid"))
# %%
fig, axs = plt.subplots(1, 2, figsize=(10,4))

fit_freq = {}
for key, grp in f_response_data.groupby(['Probe']):
    grp.plot(ax=axs[0], kind='line', x='Frequency [Hz]', y='Power [dBm]', label=key[0])
    fit_freq[key[0]] = linregress(np.log(grp['Frequency [Hz]']), grp['Power [dBm]'])

axs[0].set_xlabel("Frequency [Hz]")
axs[0].set_ylabel("Output Power [dBm]")
axs[0].set_xscale('log')
axs[0].grid(which='both')

for key, grp in f_response_data.groupby(['Probe']):
    grp.plot(ax=axs[1], kind='line', x='Frequency [Hz]', y='B Field [uT]', label=key[0])

axs[1].set_xlabel("Frequency [Hz]")
axs[1].set_ylabel("B Field [$\mu$T]")
axs[1].set_xscale('log')
axs[1].grid(which='both')
# %%
regression_db=[]
for probe in fit_freq.keys():
    regression_db.append([
        probe,
        np.round(fit_freq[probe].slope,2),
        np.round(fit_freq[probe].intercept, 2),
        f_response_data[f_response_data['Probe'] == probe]['B Field [uT]'].mean()
    ])

print(pd.DataFrame(regression_db, columns=["Probe", "Slope", "Intercept", "Avg. B Field [uT]"]).to_markdown(index=False, tablefmt="grid"))
# %%
measured_load_db = -31

calibration_field_strength = f_response_data[f_response_data['Probe'] == 'H5']['B Field [uT]'].mean()
expected_db = np.log(28e6) * fit_freq['H5'].slope + fit_freq['H5'].intercept

db_difference =  expected_db-measured_load_db

field = np.exp(np.log(calibration_field_strength) - (db_difference)/fit_5mhz['H5'].slope)
print(f"Field Strength: {field:.2f} uT")
# %%
E = (1.32/2) / 7e-3 # V/m
R = E * helmholz_subs[mu0] / (field*1e-6)

print(f"R: {R:.1f}")
# %%
