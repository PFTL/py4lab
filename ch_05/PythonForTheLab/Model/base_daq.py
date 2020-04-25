class DAQBase:
    def __init__(self, port):
        self.port = port

    def initialize(self):
        pass

    def get_voltage(self, channel):
        pass

    def set_voltage(self, channel, volts):
        pass

    def finalize(self):
        pass