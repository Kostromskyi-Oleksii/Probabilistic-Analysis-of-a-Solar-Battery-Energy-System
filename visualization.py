import matplotlib.pyplot as plt
import numpy as np

def plot_battery_distribution(final_battery):
    if not final_battery:
        print("No successful days available to build the histogram")
        return

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.hist(final_battery, bins=20, color='skyblue', edgecolor='black')
    plt.title("Distribution of final battery charge\n(successful days)")
    plt.xlabel("Battery energy at end of day, Wh")
    plt.ylabel("Number of days")
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()


def plot_soc_trajectories(all_soc_histories, max_trajectories=15):
    if not all_soc_histories:
        print("No SOC trajectories to display")
        return

    plt.figure(figsize=(10, 6))
    hours = np.arange(len(all_soc_histories[0]))

    for i, soc in enumerate(all_soc_histories[:max_trajectories]):
        alpha = 0.8 if i < 5 else 0.35
        plt.plot(hours, soc, lw=1.1, alpha=alpha)

    plt.title(f"Typical state-of-charge (SOC) trajectories — up to {max_trajectories} days")
    plt.xlabel("Hour of the day")
    plt.ylabel("Battery energy, Wh")
    plt.grid(True, alpha=0.3)
    plt.ylim(0, 4100)
    plt.tight_layout()
    plt.show()