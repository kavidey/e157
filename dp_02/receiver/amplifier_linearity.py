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
two_tone = pd.read_excel(data_path/"iip3.xlsx")
# %%
regressions = {}

OIP1 = two_tone['Output Power [dBm]']
mask = ~np.isnan(OIP1)
IIP1 = two_tone["Input Power [dBm]"][mask]
OIP1 = OIP1[mask]
regressions['Linear'] = linregress(IIP1[:7], OIP1[:7])
plt.plot(IIP1, OIP1, label="Linear Term")

OIP3 = two_tone['IM3 [dBm]']
mask = ~np.isnan(OIP3)
IIP3 = two_tone["Input Power [dBm]"][mask]
OIP3 = OIP3[mask]
regressions['3rd Order'] = linregress(IIP3[:2], OIP3[:2])
plt.plot(IIP3, OIP3, label="3rd Order Products")

plt.grid()
plt.legend()

plt.show()
# %%
regression_db = []
for k in regressions.keys():
    regression_db.append([k, np.round(regressions[k].slope,2), np.round(regressions[k].intercept, 2)])
df = pd.DataFrame(regression_db, columns=["Term", "Slope", "Intercept"])
print(df.to_markdown(index=False, tablefmt="grid"))
print(df.to_latex(float_format="{:.12}".format, index=False))
# %%
input_power = np.linspace(-80, 20)
OIP1_extended = input_power*regressions["Linear"].slope + regressions["Linear"].intercept
OIP3_extended = input_power*regressions["3rd Order"].slope + regressions["3rd Order"].intercept

IP3 = line_intersect(regressions["Linear"].slope, regressions["Linear"].intercept, regressions["3rd Order"].slope, regressions["3rd Order"].intercept)

plt.plot(input_power, OIP1_extended, '--', label="Linear Term - extended")
plt.plot(input_power, OIP3_extended, '--', label="3rd Order Products - extended")

plt.plot(IIP1, OIP1)
plt.plot(IIP3, OIP3)

plt.scatter(IP3[0], IP3[1], label=f"IP3: ({IP3[0]:.2f}, {IP3[1]:.2f})", zorder=10)

IIP3_theoretical = -62.5
OIP3_theoretical = 7
plt.scatter(IIP3_theoretical, OIP3_theoretical, label=f"Theoretical IP3: ({IIP3_theoretical}, {OIP3_theoretical})", zorder=10)

plt.grid()
plt.legend()

plt.savefig("../report/figures/iip3_regression.pdf")
plt.show()
# %%