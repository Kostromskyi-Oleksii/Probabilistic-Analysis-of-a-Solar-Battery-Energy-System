# Probabilistic Analysis of a Solar-Battery Energy System

## Overview
This project presents a probabilistic model of an off-grid solar energy system consisting of photovoltaic generation, battery storage, and residential electrical load.  
The primary objective is to perform a Monte Carlo-based assessment of system reliability under stochastic weather conditions.

The project is designed as a pre-university Electrical Engineering study, emphasizing renewable energy systems analysis, energy balance, and statistical reliability evaluation.

## Motivation
Solar power generation is highly variable due to weather conditions. Designing off-grid systems based solely on average solar yield can lead to frequent energy shortages.  
This simulation investigates how daily weather fluctuations affect:
- Single-day energy autonomy
- Battery state-of-charge dynamics
- Risk of blackout (load not fully supplied)

Such probabilistic analysis is critical for proper sizing of PV panels and batteries, ensuring high reliability in real-world autonomous solar installations.

## System Model

### Components and Parameters

| Component             | Parameter                          | Value / Description                                      |
|-----------------------|------------------------------------|----------------------------------------------------------|
| Photovoltaic System   | Peak power                         | 800 W (midday peak under ideal conditions)               |
|                       | Daily weather factor               | Uniform random ∈ [0.5, 1.0] (50–100% of ideal yield)      |
| Battery Storage       | Nominal capacity                   | 4000 Wh                                                  |
|                       | Charge efficiency                  | 90%                                                      |
|                       | Initial state-of-charge (each day) | 2000 Wh                                                  |
| Residential Load      | Base power                         | 200 W (daytime)                                          |
|                       | Evening peak                       | 450 W (17:00–23:00)                                       |
|                       | Off-peak                           | 200 W (other hours)                                      |

### Key Electrical Relations
- Generated energy per hour: P_solar(t) × weather_factor  
- Energy charged to battery: ΔE × η_charge (η = 0.9)  
- Energy balance: E_generated + E_from_battery ≥ E_load  
- Blackout occurs if battery depletes before load is fully supplied

### Important Model Limitation
The current implementation **resets battery level to 2000 Wh at the start of each simulated day**.  
This evaluates **independent daily autonomy** under varying weather, but does **not** model multi-day carry-over effects (e.g., surviving sequences of cloudy days).  
A full multi-day autonomy version is a recommended future extension.

## Simulation Approach
- Time resolution: 1 hour  
- Simulation duration: 90 independent days (Monte Carlo trials)  
- Weather variation: uniform random factor between 0.5 and 1.0 applied daily  
- Metrics collected:  
  - Percentage of fully autonomous days (no blackout)  
  - Final battery level on successful days  

## Key Results
Example output from a typical 90-day simulation (results vary slightly due to randomness):

- **Autonomous days**: **98.89%** (89 out of 90 days fully supplied)  
- **Average final battery level** (on successful days): **3421 Wh**  
- **Minimum final battery level** (successful days): **~1800 Wh**  

Interpretation:  
Under the modeled conditions, the system achieves near-perfect daily reliability (~99%).  
The battery typically ends the day with substantial reserve, indicating possible over-sizing for single-day autonomy.

A histogram of final battery states (successful days) is generated to visualize the distribution.

## Analysis and Conclusions
- The 800 W PV + 4000 Wh battery configuration provides excellent single-day autonomy even at 50% solar yield.  
- Blackouts are rare (~1%) and occur only on extremely poor weather days combined with full evening peak usage.  
- Significant battery energy remains unused at day's end, suggesting potential for smaller battery or larger load.  
- Recommendations:  
  - Implement battery state carry-over to evaluate resilience during prolonged cloudy periods.  
  - Test sensitivity to lower PV power or higher evening loads.  
  - Explore optimal battery sizing for target reliability (e.g., 99.9%).

## Limitations
- Independent daily resets (no multi-day energy accumulation/depletion).  
- Uniform weather distribution (real weather often has correlated cloudy periods).  
- Hourly resolution (misses short-term PV fluctuations).  
- No depth-of-discharge limits, discharge efficiency, or self-discharge modeling.  
- Fixed daily load and solar profiles (no seasonal variation).

## Project Structure
- `config.py`            - System parameters (PV power, battery capacity, load profile, etc.)  
- `solar_model.py`       - Weather-scaled hourly solar generation profile  
- `load_model.py`        - Daily residential load profile  
- `simulation.py`        - Core Monte Carlo daily simulation logic  
- `analysis.py`          - Calculation of reliability metrics  
- `visualization.py`     - Histogram of final battery levels  
- `main.py`              - Entry point (runs simulation, prints results, shows plot)  
- `README.md`            - This file

## How to Run
1. Install required libraries:
```bash
pip install numpy matplotlib
python main.py
```
The program will:

Run 90-day Monte Carlo simulation
Print percentage of autonomous days and average final battery level
Display a histogram of ending battery states (successful days)

Feel free to modify parameters in config.py to explore different system configurations!
Possible Extensions

Multi-day battery state continuity
Correlated weather sequences (e.g., Markov chain for cloudy days)
Seasonal solar irradiance profiles
Optimization loop: find minimal battery capacity for ≥99% autonomy
Add depth-of-discharge protection and round-trip efficiency
Time-series plots and blackout calendar visualization