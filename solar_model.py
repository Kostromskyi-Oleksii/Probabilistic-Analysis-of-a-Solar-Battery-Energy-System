import numpy as np
from config import BASE_SOLAR_PROFILE

def generate_solar_profile():
    weather_factor = np.random.uniform(0.5, 1.0)
    return np.array(BASE_SOLAR_PROFILE) * weather_factor
