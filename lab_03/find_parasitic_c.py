# %%
from matplotlib import pyplot as plt
import numpy as np
import skrf as rf
from skrf import Network
import pandas as pd
# %%
def plot_data(network):
    fig, axes = plt.subplots(1,3, figsize=(12,3), layout="constrained")
    network.plot_s_db(ax=axes[0], linewidth=3)
    network.plot_s_deg(ax=axes[1], linewidth=3)
    network.plot_s_smith(ax=axes[2], linewidth=3)
# %%
part1 = pd.read_csv("data/CSV46.csv", skiprows=13, header=None, names=["frequency", "resistance", "reactance", "hf", "label"])
s11 = ((part1.resistance/50+1j*part1.reactance/50) - 1) / ((part1.resistance/50+1j*part1.reactance/50) + 1)
part1_net = Network(frequency=part1.frequency, s=s11)

plot_data(part1_net)

print("Slope")
print(np.mean(np.gradient(np.ravel(part1_net.s_deg), part1_net.frequency.f)))
# %%
part2_shunt = pd.read_csv("data/CSV47.csv", skiprows=13, header=None, names=["frequency", "resistance", "reactance", "hf", "label"])
s11 = ((part2_shunt.resistance/50+1j*part2_shunt.reactance/50) - 1) / ((part2_shunt.resistance/50+1j*part2_shunt.reactance/50) + 1)
part2_shunt_net = Network(frequency=part2_shunt.frequency, s=s11)

plot_data(part2_shunt_net)
print("Slope")
print(np.mean(np.gradient(np.ravel(part2_shunt_net.s_deg), part2_shunt_net.frequency.f)))
# %%
part2_l = pd.read_csv("data/CSV47.csv", skiprows=13, header=None, names=["frequency", "resistance", "reactance", "hf", "label"])
s11 = ((part2_l.resistance/50+1j*part2_l.reactance/50) - 1) / ((part2_l.resistance/50+1j*part2_l.reactance/50) + 1)
part2_l_net = Network(frequency=part2_l.frequency, s=s11)

plot_data(part2_l_net)
print("Slope")
print(np.mean(np.gradient(np.ravel(part2_l_net.s_deg), part2_l_net.frequency.f)))
# %%
