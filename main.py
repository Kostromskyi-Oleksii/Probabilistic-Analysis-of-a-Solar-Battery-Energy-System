from simulation import run_simulation
from analysis import analyze
from visualization import plot_battery_distribution

blackouts, battery_levels = run_simulation()
results = analyze(blackouts, battery_levels)

for k, v in results.items():
    print(f"{k}: {v}")

plot_battery_distribution(battery_levels)
