import numpy as np
from config import SIMULATION_DAYS

def analyze(blackout_days, final_battery):
    return {
        "autonomous_days_percent":
            (SIMULATION_DAYS - blackout_days) / SIMULATION_DAYS * 100,
        "average_final_battery":
            np.mean(final_battery)
    }
