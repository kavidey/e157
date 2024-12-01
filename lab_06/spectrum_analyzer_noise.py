# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from pathlib import Path
from scipy.stats import linregress

data_path = Path("data")
# %%
sweep_time = pd.read_excel(data_path/"lab_data.xlsx", sheet_name="sweep_time")
# %%
plt.tricontourf(sweep_time["RBW [Hz]"],
                sweep_time["VBW [Hz]"],
                sweep_time["Sweep Time [ms]"], 
                norm=matplotlib.colors.LogNorm(),
)
plt.plot(sweep_time["RBW [Hz]"], sweep_time["VBW [Hz]"], 'ko', ms=3)
plt.colorbar(label="Scan Time [ms]")

plt.xscale("log")
plt.yscale("log")
plt.xlabel("RBW [Hz]")
plt.ylabel("VBW [Hz]")
plt.show()
# %%
