from PythonForTheLab.Controller.pftl_daq import Device
from PythonForTheLab import ur


class AnalogDaq:
    def __init__(self, port):
        self.port = port
        self.driver = Device(self.port)

    def initialize(self):
        self.driver.initialize()
        self.set_voltage(0, ur('0V'))
        self.set_voltage(1, ur('0V'))

    def finalize(self):
        self.set_voltage(0, ur('0V'))
        self.set_voltage(1, ur('0V'))
        self.driver.finalize()

    def set_voltage(self, channel, volts):
        value_volts = volts.m_as('V')
        value_int = round(value_volts / 3.3 * 4095)
        self.driver.set_analog_output(channel, value_int)

    def get_voltage(self, channel):
        voltage_bits = self.driver.get_analog_input(channel)
        voltage = voltage_bits * ur('3.3V')/1023
        return voltage

    def __str__(self):
        return "Analog Daq"

if __name__ == "__main__":
    daq = AnalogDaq('/dev/ttyACM0')
    daq.initialize()
    voltage = ur('3000mV')
    daq.set_voltage(0, voltage)
    input_volts = daq.get_voltage(0)
    print(input_volts)
    daq.finalize()