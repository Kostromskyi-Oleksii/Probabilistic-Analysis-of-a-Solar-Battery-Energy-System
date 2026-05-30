import numpy as np
from config import SIMULATION_DAYS

def analyze(blackout_days, final_battery):
    successful_days = SIMULATION_DAYS - blackout_days
    
    if successful_days == 0:
        return {
            "autonomous_days_percent": 0.0,
            "blackout_days": blackout_days,
            "average_final_battery_Wh": 0.0,
            "min_final_battery_Wh": 0.0,
            "max_final_battery_Wh": 0.0,
            "successful_days": 0
        }

    return {
        "autonomous_days_percent": (successful_days / SIMULATION_DAYS) * 100,
        "blackout_days": blackout_days,
        "average_final_battery_Wh": np.mean(final_battery),
        "min_final_battery_Wh": np.min(final_battery),
        "max_final_battery_Wh": np.max(final_battery),
        "successful_days": successful_days
    }