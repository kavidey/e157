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
f = np.logspace(0, np.log10(300e6), 10000)
fc = 100e6

A_dB = -10 * np.log10(1+(epsilon**2)*(chebyshev_3rd_order(omega_over_omega_c_prime(f/fc))**2))

metrics = util.calc_s21_metrics(f, A_dB)

inband_db = A_dB[f <= 85e6]
inband_ripple = np.max(inband_db) - np.min(inband_db)
worst_ripple_freq = f[util.find_nearest_idx(A_dB, metrics['insertion_loss']-inband_ripple)]
metrics['inband_ripple'] = inband_ripple
metrics['worst_ripple_freq'] = worst_ripple_freq

fig1, ax1 = plt.subplots()
ax1.grid(which='both')
ax1.set_axisbelow(True)
ax1.set_xscale('log')

ax1.plot(f, A_dB, zorder=-1)

util.plot_s21_dc_stop_metrics(ax1, metrics)

ax1.set_xlim(f[0], f[-1])

ax1.set_xlabel("Frequency (Hz)")
ax1.set_ylabel("Magnitude (dB)")

plt.savefig('report/figures/6.analytical.pdf')
# %%
S21 = np.power(10, A_dB)
S11 = np.sqrt(1-np.power(S21,2))

fig1, ax1 = plt.subplots()
ax1.grid(which='both')
ax1.set_axisbelow(True)
ax1.set_xscale('log')

s11_db = 10*np.log10(S11)

ax1.plot(f, s11_db, zorder=-1)

passband_freq = util.calc_s21_metrics(f, A_dB)['passband_edge']
stopband_freq = util.calc_s21_metrics(f, A_dB)['stopband_start']

passband_db = s11_db[util.find_nearest_idx(f, passband_freq)]
ax1.scatter(
    passband_freq,
    passband_db,
    c='red', zorder=10,
    label=f"Pass band edge: {passband_db:.2f} dB at {passband_freq / 1e6:.2f} MHz"
)
stopband_db = s11_db[util.find_nearest_idx(f, stopband_freq)]
ax1.scatter(
    stopband_freq,
    stopband_db,
    c='orange', zorder=10,
    label=f"Stop band edge: {stopband_db:.2f} dB at {stopband_freq / 1e6:.2f} MHz"
)
ax1.legend()

ax1.set_xlim(f[0], f[-1])

ax1.set_xlabel("Frequency (Hz)")
ax1.set_ylabel("Magnitude (dB)")

plt.savefig("report/figures/7.analytical.pdf")
# %%
f = np.logspace(np.log10(40e6), np.log10(130e6), 10000)
fc = 100e6

A_dB = -10 * np.log10(1+(epsilon**2)*(chebyshev_3rd_order(omega_over_omega_c_prime(f/fc))**2))

metrics = util.calc_s21_metrics(f, A_dB, provided_insertion_loss=metrics['insertion_loss'])

fig1, ax1 = plt.subplots()
ax1.grid(which='both')
ax1.set_axisbelow(True)
ax1.set_xscale('linear')

ax1.plot(f, A_dB, zorder=-10)

util.plot_s21_pass_metrics(ax1, metrics, 0)

ax1.set_xlim(f[0], f[-1])

ax1.set_xlabel("Frequency (Hz)")
ax1.set_ylabel("Magnitude (dB)")

plt.savefig('report/figures/4.analytical.pdf')
# %%
f = np.logspace(0, np.log10(300e6), 10000)
fc = 111.4396e6

A_dB = -10 * np.log10(1+(epsilon**2)*(chebyshev_3rd_order(omega_over_omega_c_prime(f/fc))**2))

print(f[util.find_nearest_idx(A_dB, -1)])
print(f[util.find_nearest_idx(A_dB, -20)])

fig1, ax1 = plt.subplots()
ax1.grid(which='both')
ax1.set_axisbelow(True)
ax1.set_xscale('log')

ax1.plot(f, A_dB, zorder=-1)

ax1.set_xlabel("Frequency (Hz)")
ax1.set_ylabel("Magnitude (dB)")
# %%
