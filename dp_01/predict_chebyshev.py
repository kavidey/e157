# %%
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import util
# %% Constants & Functions
order = 3
passband_ripple_db = 0.5
epsilon = np.sqrt(np.power(10, passband_ripple_db/10)-1)

def chebyshev_3rd_order(x):
    return 4*np.power(x, 3) - 3*x

B = (1/order) * np.arccosh(1/epsilon)
def omega_over_omega_c_prime(omega_over_omega_c):
    return omega_over_omega_c*np.cosh(B)
# %%
f = np.linspace(25e6, 200e6, 10000)
fc = 100e6

A_dB = -10 * np.log10(1+(epsilon**2)*(chebyshev_3rd_order(omega_over_omega_c_prime(f/fc))**2))
# %%
metrics = util.calc_s21_metrics(f, A_dB)

fig1, ax1 = plt.subplots()
ax1.grid(which='both')
ax1.set_axisbelow(True)

ax1.plot(f, A_dB, zorder=-1)

util.plot_s21_metrics(ax1, metrics)

ax1.set_xlabel("Frequency (Hz)")
ax1.set_ylabel("Magnitude (dB)")

plt.show()

print(f"Insertion Loss: {metrics['insertion_loss']}")
print(f"Pass band Edge: {metrics['passband_edge'] / 1e6} MHz")
print(f"Stop band Start: {metrics['stopband_start'] / 1e6} MHz")
print(f"In band Ripple: {metrics['inband_ripple']}")
# %%