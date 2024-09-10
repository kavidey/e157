# %% Imports
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.signal import hilbert, find_peaks, find_peaks_cwt
# %%
def hl_envelopes_idx(s, dmin=1, dmax=1, split=False):
    """
    Input :
    s: 1d-array, data signal from which to extract high and low envelopes
    dmin, dmax: int, optional, size of chunks, use this if the size of the input signal is too big
    split: bool, optional, if True, split the signal in half along its mean, might help to generate the envelope in some cases
    Output :
    lmin,lmax : high/low envelope idx of input signal s

    Copied from: https://stackoverflow.com/a/60402647
    """

    # locals min      
    lmin = (np.diff(np.sign(np.diff(s))) > 0).nonzero()[0] + 1 
    # locals max
    lmax = (np.diff(np.sign(np.diff(s))) < 0).nonzero()[0] + 1 
    
    if split:
        # s_mid is zero if s centered around x-axis or more generally mean of signal
        s_mid = np.mean(s) 
        # pre-sorting of locals min based on relative position with respect to s_mid 
        lmin = lmin[s[lmin]<s_mid]
        # pre-sorting of local max based on relative position with respect to s_mid 
        lmax = lmax[s[lmax]>s_mid]

    # global min of dmin-chunks of locals min 
    lmin = lmin[[i+np.argmin(s[lmin[i:i+dmin]]) for i in range(0,len(lmin),dmin)]]
    # global max of dmax-chunks of locals max 
    lmax = lmax[[i+np.argmax(s[lmax[i:i+dmax]]) for i in range(0,len(lmax),dmax)]]
    
    return lmin,lmax

# %%
start_freq = 2e6
end_freq = 13e6
start_t = 127920
end_t = 1138060
# end_t = start_t + 100
data = pd.read_csv("data/SDS00013.csv", skiprows=11)
# %%
freq = np.linspace(start_freq, end_freq, end_t - start_t)
volt = data['Volt'][start_t:end_t].to_numpy()

w_size = 10
lmin, lmax = hl_envelopes_idx(volt, split=True, dmin=w_size, dmax=w_size)
env_v = volt[lmax]
env_f = freq[lmax]
# %%
max_peaks, _ = find_peaks(env_v, width=1e3, distance=1e4)
min_peaks, _ = find_peaks(-env_v, width=1e3, distance=1e4)
# %%
plt.plot(freq/1e6, volt, label="Voltage", zorder=-1)
plt.plot(env_f/1e6, env_v, label="Envelope", zorder=0)
plt.scatter(env_f[max_peaks]/1e6, env_v[max_peaks], c='green', label='Max', zorder=1)
plt.scatter(env_f[min_peaks]/1e6, env_v[min_peaks], c='red', label='Min', zorder=1)
plt.legend()
plt.xlabel("Frequency [MHz]")
plt.ylabel("Voltage [V]")
plt.show()
# %%
for m in max_peaks:
    print(f"Max Amplitude {env_v[m]:.3f} at {env_f[m]/1e6:.3f} MHz")
print()
for m in min_peaks:
    print(f"Min Amplitude {env_v[m]:.3f} at {env_f[m]/1e6:.3f} MHz")
print()
print(f"VWSR: {np.mean(env_v[max_peaks]) / np.mean(env_v[min_peaks]):.3f}")
# %%
