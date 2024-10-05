# %%
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
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
f = np.logspace(7, 8.5, 1000)
fc = 100e6

A_dB = 10 * np.log10(1+(epsilon**2)*(chebyshev_3rd_order(omega_over_omega_c_prime(f/fc))**2))
# %%
fig1, ax1 = plt.subplots()

ax1.plot(f/1e6, -A_dB, label='Gain')

ax1.set_xlabel("Frequency [MHz]")

ax1.grid(which='both')
ax1.set_xscale('log')
ax1.get_xaxis().set_major_formatter(matplotlib.ticker.NullFormatter())
# ax1.xaxis.set_minor_formatter(matplotlib.ticker.FormatStrFormatter("%.1f"))
ax1.get_xaxis().set_minor_formatter(matplotlib.ticker.ScalarFormatter())

ax1.axhline(-1, c="r", label='-1 dB')
ax1.legend()
# %%
passband_ripple = np.min(-A_dB[f<70e6])
print(f"Passband Ripple: {passband_ripple}")
# %%
