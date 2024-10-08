# %%
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import skrf as rf
from skrf import Network
import pandas as pd
import util
# %%
ideal_dcstop = pd.read_csv("sim/ideal.dc_to_stop.txt", skiprows=1, names=['f', 'S11r', 'S11i', 'S21r', 'S21i'], sep='	|,', engine='python')

ideal_dcstop_s11 = Network(frequency=ideal_dcstop.f, s=ideal_dcstop.S11r + 1j * ideal_dcstop.S11i)
ideal_dcstop_s21 = Network(frequency=ideal_dcstop.f, s=ideal_dcstop.S21r + 1j * ideal_dcstop.S21i)

util.plot_network(ideal_dcstop_s21)
# %%
ideal_pass = pd.read_csv("sim/ideal.pass.txt", skiprows=1, names=['f', 'S11r', 'S11i', 'S21r', 'S21i'], sep='	|,', engine='python')

ideal_pass_s11 = Network(frequency=ideal_pass.f, s=ideal_pass.S11r + 1j * ideal_pass.S11i)
ideal_pass_s21 = Network(frequency=ideal_pass.f, s=ideal_pass.S21r + 1j * ideal_pass.S21i)

util.plot_network(ideal_pass_s21)
# %%
real_dcstop = pd.read_csv("sim/real.dc_to_stop.txt", skiprows=1, names=['f', 'S11r', 'S11i', 'S21r', 'S21i'], sep='	|,', engine='python')

real_dcstop_s11 = Network(frequency=real_dcstop.f, s=real_dcstop.S11r + 1j * real_dcstop.S11i)
real_dcstop_s21 = Network(frequency=real_dcstop.f, s=real_dcstop.S21r + 1j * real_dcstop.S21i)

util.plot_network(real_dcstop_s21)
# %%
real_pass = pd.read_csv("sim/real.pass.txt", skiprows=1, names=['f', 'S11r', 'S11i', 'S21r', 'S21i'], sep='	|,', engine='python')

real_pass_s11 = Network(frequency=real_pass.f, s=real_pass.S11r + 1j * real_pass.S11i)
real_pass_s21 = Network(frequency=real_pass.f, s=real_pass.S21r + 1j * real_pass.S21i)

util.plot_network(real_pass_s21)
# %%
