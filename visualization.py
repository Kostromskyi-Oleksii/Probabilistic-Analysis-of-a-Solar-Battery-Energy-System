import matplotlib.pyplot as plt

def plot_battery_distribution(final_battery):
    plt.figure()
    plt.hist(final_battery, bins=15)
    plt.title("Final Battery Energy Distribution")
    plt.xlabel("Wh")
    plt.grid()
    plt.show()
