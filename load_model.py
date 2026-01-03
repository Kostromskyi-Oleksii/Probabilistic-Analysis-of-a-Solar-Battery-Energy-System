import numpy as np
from config import *

def generate_load():
    return np.array([
        EVENING_LOAD if EVENING_START <= h <= EVENING_END else BASE_LOAD
        for h in range(HOURS_PER_DAY)
    ])
