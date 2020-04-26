import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

import numpy as np

from PythonForTheLab.Model.analog_daq import AnalogDaq
from PythonForTheLab import ur

V = ur('V')

daq = AnalogDaq('/dev/ttyACM0') # <-- Remember to change the port
daq.initialize()
# 11 Values with units in a numpy array... 0, 0.3, 0.6, etc.
volt_range = np.linspace(0, 3, 11) * V
currents = [] # Empty list to store the values

for volt in volt_range:
    daq.set_voltage(0, volt)
    measured_voltage = daq.get_voltage(0)
    current = measured_voltage/ur('100ohm')
    currents.append(current)

print(currents)