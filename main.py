from simulation import run_simulation
from analysis import analyze
from visualization import plot_battery_distribution, plot_soc_trajectories

blackouts, battery_levels, soc_trajectories = run_simulation()
results = analyze(blackouts, battery_levels)

print("\n" + "="*65)
print("SIMULATION RESULTS".center(65))
print("="*65)
for k, v in results.items():
    if "percent" in k:
        print(f"{k:32} : {v:8.2f} %")
    else:
        print(f"{k:32} : {v}")
print("="*65)

print("\nPlot generation...")
plot_battery_distribution(battery_levels)
plot_soc_trajectories(soc_trajectories)