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

## Goal and Objectives

**Goal**  
Quantitatively evaluate the daily autonomy reliability (probability of blackout-free days) of a small off-grid solar-battery system under random weather conditions and characterize the remaining battery energy at the end of successful days.

**Objectives**
- Model hourly solar generation with realistic daily weather variability
- Simulate a typical 24-hour household load profile with evening peak
- Run Monte Carlo simulation (90 independent days)
- Compute key reliability indicators: % autonomous days, blackout count, final SOC statistics
- Visualize final battery energy distribution and intra-day SOC trajectories
- Analyze system margin and suggest directions for improvement

## System Model

### Components and Parameters

| Component             | Parameter                          | Value / Description                                      |
|-----------------------|------------------------------------|----------------------------------------------------------|
| Photovoltaic System   | Peak power                         | 800 W (midday peak under ideal conditions)               |
|                       | Daily weather factor               | Uniform random ∈ [0.5, 1.0] (50-100% of ideal yield)      |
| Battery Storage       | Nominal capacity                   | 4000 Wh                                                  |
|                       | Charge efficiency                  | 90%                                                      |
|                       | Initial state-of-charge (each day) | 2000 Wh                                                  |
| Residential Load      | Base power                         | 200 W (daytime / night)                                  |
|                       | Evening peak                       | 450 W (17:00-23:00)                                      |
|                       | Off-peak                           | 200 W (other hours)                                      |

### Key Electrical Relations
- Hourly solar generation: P_solar(t) = BASE_PROFILE[t] × weather_factor  
- Net energy to/from battery: ΔE = (P_solar(t) − P_load(t)) × η_charge  
  (η_charge = 0.9)  
- Battery update: E_{t+1} = min( max(E_t + ΔE, 0), BATTERY_CAPACITY )  
- Blackout: occurs when battery reaches ≤ 0 Wh while load remains

### Important Model Limitation
The current implementation **resets battery level to 2000 Wh at the start of each simulated day**.  
This evaluates **independent daily autonomy** under varying weather, but does **not** model multi-day carry-over effects (e.g., surviving sequences of cloudy days).  
A full multi-day version is a recommended future extension.

## Simulation Approach
- Time resolution: 1 hour  
- Simulation duration: 90 independent days (Monte Carlo trials)  
- Weather variation: uniform random factor [0.5, 1.0] applied per day  
- Metrics collected:  
  - Percentage of fully autonomous days (no blackout)  
  - Final battery level (successful days)  
  - Minimum, average and maximum final SOC on successful days  
  - Time-series of battery SOC over the day

## Simulation Results and Visualizations

Typical results from a 90-day run (values vary due to randomness):

- **Autonomous days**: **97-99.5%** (usually 88-90 days without blackout)  
- **Average final battery level** (successful days): **~3200-3500 Wh**  
- **Minimum final battery level** (successful days): **~1500-2200 Wh**  
- **Blackout days**: typically 0-2 out of 90

Visualizations:
- Histogram — distribution of final battery energy levels (successful days only)  
- SOC trajectories — overlaid time-series plots showing battery charge dynamics over 24 hours for multiple days (reveals critical periods, especially evening peak)

These plots demonstrate:
- How deeply the battery is discharged during evening hours
- Typical reserve remaining at midnight
- Spread caused by weather variability

## Analysis and Conclusions
The 800 W PV + 4000 Wh battery configuration provides **excellent single-day autonomy**, even when solar yield is reduced to 50%.  
Blackouts are rare (~0.5-3%) and usually occur only under worst-case weather combined with full evening peak consumption.

**Key findings**:
- The battery almost always ends the day with substantial reserve (>3000 Wh on average)  
- This suggests the system is **considerably oversized** for daily autonomy  
- Evening peak load is the main stress factor — the system is most vulnerable between 17:00-23:00

**Recommendations**:
- Add multi-day battery continuity to assess resilience during extended cloudy periods  
- Introduce correlated weather patterns (e.g. Markov chain or historical data)  
- Perform sensitivity / optimization studies: vary PV size, battery capacity, load profile  
- Explore load shifting or demand-side management as low-cost reliability improvements  
- Consider adding discharge efficiency, depth-of-discharge limits, self-discharge for realism

## Limitations
- Independent daily resets (no multi-day energy carry-over)  
- Uniform and independent weather variation (real weather shows temporal correlation)  
- Hourly resolution (misses intra-hour PV fluctuations)  
- No modeling of depth-of-discharge protection, discharge efficiency, self-discharge  
- Fixed daily profiles (no seasonal or weekly variation)

## Project Structure
- `config.py`            — system parameters  
- `solar_model.py`       — weather-scaled solar generation profile  
- `load_model.py`        — daily household load profile  
- `simulation.py`        — core Monte Carlo simulation logic (returns SOC histories)  
- `analysis.py`          — reliability metrics and statistics  
- `visualization.py`     — histogram of final levels + SOC trajectory plots  
- `main.py`              — entry point: runs simulation, prints results, shows plots  
- `README.md`            — this file

## How to Run
1. Install required libraries:
```bash
pip install numpy matplotlib
```
2. Run the simulation:
python main.py

The program will:

Execute 90-day Monte Carlo simulation
Print reliability metrics (autonomy %, blackouts, final SOC statistics)
Display two plots: final battery distribution + SOC trajectories

Feel free to modify parameters in config.py to test different configurations.

## Possible Extensions

Multi-day battery state continuity
Correlated weather sequences (Markov chain, real weather data)
Seasonal / monthly solar and load profiles
Optimization loop: minimal battery capacity for ≥99.9% autonomy
Depth-of-discharge limits and round-trip efficiency
Time-series blackout visualization / calendar view

## References

- Bukar, A. L., Tan, C. W., Lau, K. Y. (2019). Optimal sizing of an autonomous photovoltaic/wind/battery/diesel generator microgrid using grasshopper optimization algorithm. Solar Energy, 188, 685-696.
- Maleki, A., Askarzadeh, A. (2014). Optimal sizing of a PV/wind/diesel system with battery storage... Sustainable Energy Technologies and Assessments, 7, 147-153. 
- Tina, G. M., et al. (2020). Accurate Sizing of Residential Stand-Alone Photovoltaic Systems Considering System Reliability. Sustainability, 12(3), 1274. 
- Khatib, T., Mohamed, A., Sopian, K. (2013). A review of photovoltaic systems size optimization techniques. Renewable and Sustainable Energy Reviews, 22, 454-465.
- NASA POWER - Solar and Meteorological Data. 