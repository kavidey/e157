# %%
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(seed=42)

# %matplotlib widget
# %%
def fft(x, fs):
    N = x.shape[0]

    X = np.fft.rfft(x)

    freq = np.arange(N / 2) / (float(N) / fs)

    return X, freq

def sample_signal(x, fs_original, fs, bits, scale):
    # Quantize in time
    ratio = int(fs_original/fs)
    x = x[::ratio]

    # Quantize in voltage
    normalized = (x / scale) 
    digital = (normalized * 2**bits).astype(int)

    return (digital / 2**bits) * scale

# %%
f = 20e3 # 20 kHz
fs = 2e6 # 2 MHz
cycles = 20


# https://markimicrowave.com/tools/power-to-voltage.pdf
R = 50 # ohms
Vrms = np.sqrt(1e-3 * R) # V = sqrt(PR)
Vp = Vrms*np.sqrt(2)
# %%
t = np.arange(0, cycles * 1/f, 1/fs)
raw_samples = Vp*np.sin(2*np.pi*f*t)

noise = rng.normal(0, 10e-3, t.shape[0])
samples = raw_samples + noise

fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].plot(t*1e3, samples)
axs[0].set_xlabel("Time [ms]")
axs[0].set_ylabel("Voltage [V]")
axs[0].grid()

X, freq = fft(samples, fs)
P = 2 * np.power(np.abs(X/samples.shape[0]),2)/R/1e-3

axs[1].plot(freq/1e3, 10*np.log10(P))
axs[1].grid()
axs[1].set_xlabel("Frequency [kHz]")
axs[1].set_ylabel("Power [dBm]")

plt.suptitle("Original Signal", fontsize=15)
plt.show()
# %%
#signal = np.sin(np.linspace(0, 2*np.pi, 1000))
signal = np.linspace(-1,1,1000)
plt.plot(signal, label="Original")
plt.plot(sample_signal(signal, 1, 1, 4, 5), label="Sampled")
plt.plot(sample_signal(signal*5, 1, 1, 4, 5), label="Sampled with Gain of 5")
plt.xlabel("Sample Number")
plt.ylabel("Voltage")
plt.grid()
plt.show()
# %%
new_fs = 500e3
t = np.arange(0, cycles * 1/f, 1/new_fs)
adc_sampled = sample_signal(samples, fs, new_fs, 4, Vp*5)

fig, axs = plt.subplots(1, 2, figsize=(10, 5))
# axs[0].plot(t*1e3, adc_sampled[:-1])
axs[0].plot(t*1e3, adc_sampled)
axs[0].plot(t*1e3, samples[::int(fs/new_fs)])
axs[0].set_xlabel("Time [ms]")
axs[0].set_ylabel("Voltage [V]")
axs[0].grid()
axs[0].set_xlim(0, 0.2)

X, freq = fft(adc_sampled, new_fs)
P = 2 * np.power(np.abs(X/adc_sampled.shape[0]),2)/R/1e-3

axs[1].plot(freq/1e3, 10*np.log10(P))
axs[1].grid()
axs[1].set_xlabel("Frequency [kHz]")
axs[1].set_ylabel("Power [dBm]")

plt.suptitle("Sampled Signal", fontsize=15)
plt.show()
# %%
new_fs = 500e3
t = np.arange(0, cycles * 1/f, 1/new_fs)
adc_sampled = sample_signal(samples*5, fs, new_fs, 4, Vp*5)

fig, axs = plt.subplots(1, 2, figsize=(10, 5))
# axs[0].plot(t*1e3, adc_sampled[:-1])
axs[0].plot(t*1e3, adc_sampled)
axs[0].plot(t*1e3, samples[::int(fs/new_fs)]*5)
axs[0].set_xlabel("Time [ms]")
axs[0].set_ylabel("Voltage [V]")
axs[0].grid()
axs[0].set_xlim(0, 0.2)

X, freq = fft(adc_sampled, new_fs)
P = 2 * np.power(np.abs(X/adc_sampled.shape[0]),2)/R/1e-3

axs[1].plot(freq/1e3, 10*np.log10(P))
axs[1].grid()
axs[1].set_xlabel("Frequency [kHz]")
axs[1].set_ylabel("Power [dBm]")

plt.suptitle("Sampled & Scaled Signal", fontsize=15)
plt.show()
# %%
