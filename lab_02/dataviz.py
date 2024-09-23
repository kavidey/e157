# %%
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import numpy as np
plt.ion()
# %%
data = pd.read_csv("data/SDS00012.csv", skiprows=11)
data['Second'] = data['Second']*1e9
# %%
# plt.plot(data['Second']*1e9, data['Volt'])
# plt.plot(data['Second']*1e9, data['Volt.1'])
# plt.plot(data['Second']*1e9, data['Volt.2'])
# plt.show()
# %%
fig = px.line(data, x="Second", y=data.columns[1:])
fig.show()
# %%
