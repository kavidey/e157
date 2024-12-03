# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.stats import linregress

data_path = Path("data")
# %%
def line_intersect(m1, b1, m2, b2):
    if m1 == m2:
        return None
    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    return x,y
# %%
one_tone = pd.read_excel(data_path/"lab_data.xlsx", sheet_name="one_tone")
one_tone["Output Power [dBm]"] = one_tone["Measured Power [dBm]"] + one_tone["Attenuation [dB]"]

two_tone = pd.read_excel(data_path/"lab_data.xlsx", sheet_name="two_tone")
two_tone_double = pd.read_excel(data_path/"lab_data.xlsx", sheet_name="two_tone_double")
for column in two_tone.columns:
    if column not in ["Input Power [dBm]", "Attenuation [dB]"]:
        two_tone[column] += two_tone["Attenuation [dB]"]

for column in two_tone_double.columns:
    if column not in ["Input Power [dBm]", "Attenuation [dB]"]:
        two_tone_double[column] += two_tone_double["Attenuation [dB]"]
# %%
input_power = one_tone["Input Power [dBm]"]
gain = (one_tone["Output Power [dBm]"] - one_tone["Input Power [dBm]"]).median()
output_power = input_power + gain

fig, axs = plt.subplots(1, 2, figsize=(10,5))
fig.subplots_adjust(wspace=0.3)

axs[0].plot(input_power, output_power, '--', label="Ideal")
axs[0].plot(one_tone["Input Power [dBm]"], one_tone["Output Power [dBm]"], label="Measured")
axs[0].grid()
axs[0].set_xlabel("Input Power [dBm]")
axs[0].set_ylabel("Output Power [dBm]")
axs[0].legend()
axs[0].set_title("One Tone Gain")

axs[1].plot(one_tone["Input Power [dBm]"], one_tone["Output Power [dBm]"] - output_power, label="Measured")
axs[1].grid()
axs[1].set_xlabel("Input Power [dBm]")
axs[1].set_ylabel("Output Power Relative to Expected [dBm]")
axs[1].set_xlim(-20, -10)
axs[1].set_title("Zoomed in on $P_{-1dB}$")
# %%
regressions = {}

OIP1 = (two_tone[600] + two_tone[601])/2
mask = ~np.isnan(OIP1)
IIP1 = two_tone["Input Power [dBm]"][mask]
OIP1 = OIP1[mask]
regressions['Linear'] = linregress(IIP1, OIP1)
plt.plot(IIP1, OIP1, label="Linear Term")

OIP2 = two_tone[1201]
mask = ~np.isnan(OIP2)
IIP2 = two_tone["Input Power [dBm]"][mask]
OIP2 = OIP2[mask]
regressions['2nd Order'] = linregress(IIP2, OIP2)
plt.plot(IIP2, OIP2, label="2nd Order Products")

OIP3 = (two_tone[1801] + two_tone[1802]) / 2
mask = ~np.isnan(OIP3)
IIP3 = two_tone["Input Power [dBm]"][mask]
OIP3 = OIP3[mask]
regressions['3rd Order'] = linregress(IIP3, OIP3)
plt.plot(IIP3, OIP3, label="3rd Order Products")

plt.grid()
plt.legend()

plt.show()
# %%
regression_db = []
for k in regressions.keys():
    regression_db.append([k, np.round(regressions[k].slope,2), np.round(regressions[k].intercept, 2)])
print(pd.DataFrame(regression_db, columns=["Term", "Slope", "Intercept"]).to_markdown(index=False, tablefmt="grid"))
# %%
input_power = np.linspace(-40, 30)
OIP1_extended = input_power*regressions["Linear"].slope + regressions["Linear"].intercept
OIP2_extended = input_power*regressions["2nd Order"].slope + regressions["2nd Order"].intercept
OIP3_extended = input_power*regressions["3rd Order"].slope + regressions["3rd Order"].intercept

IP2 = line_intersect(regressions["Linear"].slope, regressions["Linear"].intercept, regressions["2nd Order"].slope, regressions["2nd Order"].intercept)
IP3 = line_intersect(regressions["Linear"].slope, regressions["Linear"].intercept, regressions["3rd Order"].slope, regressions["3rd Order"].intercept)

plt.plot(input_power, OIP1_extended, '--', label="Linear Term - extended")
plt.plot(input_power, OIP2_extended, '--', label="2nd Order Products - extended")
plt.plot(input_power, OIP3_extended, '--', label="3rd Order Products - extended")

plt.plot(IIP1, OIP1)
plt.plot(IIP2, OIP2)
plt.plot(IIP3, OIP3)

plt.scatter(IP2[0], IP2[1], label="IP2", zorder=10)
plt.scatter(IP3[0], IP3[1], label="IP3", zorder=10)

plt.grid()
plt.legend()

plt.show()

print(f"IP2: ({IP2[0]:.2f}, {IP2[1]:.2f})")
print(f"IP3: ({IP3[0]:.2f}, {IP3[1]:.2f})")
# %%
regressions = {}

OIP1 = (two_tone_double[600] + two_tone_double[601])/2
mask = ~np.isnan(OIP1)
IIP1 = two_tone_double["Input Power [dBm]"][mask]
OIP1 = OIP1[mask]
regressions['Linear'] = linregress(IIP1, OIP1)
plt.plot(IIP1, OIP1, label="Linear Term")

OIP3 = (two_tone_double[1801] + two_tone_double[1802]) / 2
mask = ~np.isnan(OIP3)
IIP3 = two_tone_double["Input Power [dBm]"][mask]
OIP3 = OIP3[mask]
regressions['3rd Order'] = linregress(IIP3, OIP3)
plt.plot(IIP3, OIP3, label="3rd Order Products")

plt.grid()
plt.legend()

plt.show()
# %%
regression_db = []
for k in regressions.keys():
    regression_db.append([k, np.round(regressions[k].slope,2), np.round(regressions[k].intercept, 2)])
print(pd.DataFrame(regression_db, columns=["Term", "Slope", "Intercept"]).to_markdown(index=False, tablefmt="grid"))
# %%
input_power = np.linspace(-60, -30)
OIP1_extended = input_power*regressions["Linear"].slope + regressions["Linear"].intercept
OIP3_extended = input_power*regressions["3rd Order"].slope + regressions["3rd Order"].intercept

IP3 = line_intersect(regressions["Linear"].slope, regressions["Linear"].intercept, regressions["3rd Order"].slope, regressions["3rd Order"].intercept)

plt.plot(input_power, OIP1_extended, '--', label="Linear Term - extended")
plt.plot(input_power, OIP3_extended, '--', label="3rd Order Products - extended")

plt.plot(IIP1, OIP1)
plt.plot(IIP3, OIP3)

plt.scatter(IP3[0], IP3[1], label="IP3", zorder=10)

plt.grid()
plt.legend()

plt.show()

print(f"IP3: ({IP3[0]:.2f}, {IP3[1]:.2f})")
# %%
