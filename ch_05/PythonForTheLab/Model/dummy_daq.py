from random import random
from PythonForTheLab.Model.base_daq import DAQBase


class DummyDaq(DAQBase):
     def get_voltage(self, channel):
         return random()


if __name__ == "__main__":
    daq = DummyDaq('/dev/ttyACM0')
    daq.initialize()
    voltage = 3
    daq.set_voltage(0, voltage)
    input_volts = daq.get_voltage(0)
    print(input_volts)
    daq.finalize()