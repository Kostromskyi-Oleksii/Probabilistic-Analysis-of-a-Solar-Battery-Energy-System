from config import *
from solar_model import generate_solar_profile
from load_model import generate_load

def run_simulation():
    blackout_days = 0
    final_battery = []

    for _ in range(SIMULATION_DAYS):
        solar = generate_solar_profile()
        load = generate_load()
        battery = BATTERY_INITIAL
        blackout = False

        for h in range(HOURS_PER_DAY):
            net = (solar[h] - load[h]) * CHARGE_EFFICIENCY
            battery += net

            if battery <= 0:
                blackout = True
                break

            battery = min(battery, BATTERY_CAPACITY)

        if blackout:
            blackout_days += 1

        final_battery.append(battery)

    return blackout_days, final_battery
