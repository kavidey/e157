import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def resistance_reactance_to_gamma(resistance, reactance):
    return ((resistance/50+1j*reactance/50) - 1) / ((resistance/50+1j*reactance/50) + 1)

def find_nearest_idx(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx

def calc_s21_metrics(f, db):
    insertion_loss = np.max(db)
    max_gain_freq = f[find_nearest_idx(db, insertion_loss)]

    passband_edge = f[find_nearest_idx(db, insertion_loss-3)]
    stopband_start = f[find_nearest_idx(db, insertion_loss-20)]

    inband_db = db[f <= max_gain_freq]
    inband_ripple = np.max(inband_db) - np.min(inband_db)
    worst_ripple_freq = f[find_nearest_idx(db, insertion_loss-inband_ripple)]

    return {
        "insertion_loss": np.abs(insertion_loss),
        "max_gain_freq": max_gain_freq,
        "passband_edge": passband_edge,
        "stopband_start": stopband_start,
        "inband_ripple": inband_ripple,
        "worst_ripple_freq": worst_ripple_freq
    }

def plot_s21_mag(net, log=True):
    metrics = calc_s21_metrics(net.f, net.s_db)

    fig1, ax1 = plt.subplots()
    ax1.grid(which='both')

    net.plot_s_db(ax=ax1, linewidth=2)

    if log:
        ax1.get_xaxis().set_major_formatter(matplotlib.ticker.NullFormatter())
        ax1.get_xaxis().set_minor_formatter(matplotlib.ticker.ScalarFormatter())
        ax1.set_xscale('log')

    plot_s21_metrics(ax1, metrics)

def plot_s21_metrics(ax, metrics, skip_ripple=False, skip_stopband=True):
    ax.vlines(metrics['max_gain_freq'], 0, -metrics['insertion_loss'], label=f"Insertion Loss: {metrics['insertion_loss']:.2f} dB", colors='green', linewidth=3)
    ax.scatter([metrics['max_gain_freq'], metrics['max_gain_freq']], [0, -metrics['insertion_loss']], color='green', marker="_", s=50, zorder=5)
    
    if not skip_ripple:
        ax.vlines(metrics['worst_ripple_freq'], -metrics['insertion_loss'], -metrics['insertion_loss']-metrics['inband_ripple'], label=f"Minimum Ripple: {metrics['inband_ripple']:.2f} dB", colors='orange', linewidth=3)
        ax.scatter([metrics['worst_ripple_freq'], metrics['worst_ripple_freq']], [-metrics['insertion_loss'], -metrics['insertion_loss']-metrics['inband_ripple']], color='orange', marker="_", s=50, zorder=5)
    
    ax.scatter(metrics['passband_edge'], -metrics['insertion_loss']-3, label=f"Pass band edge: {metrics['passband_edge']/1e6:.2f} MHz", c='red', zorder=10)

    if not skip_stopband:
        ax.scatter(metrics['stopband_start'], -metrics['insertion_loss']-20, label=f"Stop band start: {metrics['stopband_start']/1e6:.2f} MHz", c='orange', zorder=10)

    ax.legend()

def plot_network(network):
    fig, axes = plt.subplots(1,3, figsize=(12,3), layout="constrained")

    network.plot_s_db(ax=axes[0], linewidth=3)
    axes[0].set_xscale('log')
    # axes[0].get_xaxis().set_major_formatter(matplotlib.ticker.NullFormatter())
    # axes[0].get_xaxis().set_minor_formatter(matplotlib.ticker.ScalarFormatter())
    axes[0].grid()

    network.plot_s_deg(ax=axes[1], linewidth=3)
    axes[1].set_xscale('log')
    # axes[1].get_xaxis().set_major_formatter(matplotlib.ticker.NullFormatter())
    # axes[1].get_xaxis().set_minor_formatter(matplotlib.ticker.ScalarFormatter())
    axes[1].grid()

    network.plot_s_smith(ax=axes[2], linewidth=3)