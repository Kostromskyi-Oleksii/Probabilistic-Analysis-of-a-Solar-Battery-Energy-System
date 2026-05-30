from config import *
from solar_model import generate_solar_profile
from load_model import generate_load

def run_simulation():
    blackout_days = 0
    final_battery = []
    successful_soc_histories = []

    for _ in range(SIMULATION_DAYS):
        solar = generate_solar_profile()
        load = generate_load()
        battery = BATTERY_INITIAL
        soc_history = [battery]
        blackout = False

        for h in range(HOURS_PER_DAY):
            net = (solar[h] - load[h]) * CHARGE_EFFICIENCY
            battery += net

            if battery <= 0:
                blackout = True
                battery = 0
                soc_history.append(0)
                break

            battery = min(battery, BATTERY_CAPACITY)
            soc_history.append(battery)

        if blackout:
            blackout_days += 1
        else:
            final_battery.append(battery)
            successful_soc_histories.append(soc_history)

    return blackout_days, final_battery, successful_soc_histories