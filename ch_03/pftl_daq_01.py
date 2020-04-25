import serial
from time import sleep


class Device:
    def __init__(self, port):
        self.rsc = serial.Serial(port)
        sleep(1)

    def idn(self):
        self.rsc.write(b'IDN\n')
        return self.rsc.readline()

    def get_analog_input(self, channel):
        message = f'IN:CH{channel}\n'
        message = message.encode('ascii')
        self.rsc.write(message)
        return self.rsc.readline()

    def set_analog_output(self, channel, output_value):
        message = f'OUT:CH{channel}:{output_value}\n'
        message = message.encode('ascii')
        self.rsc.write(message)


dev = Device('/dev/ttyACM0') #<---- Remember to change the port
serial_number = dev.idn()
print(f'The device serial number is: {serial_number}')
volts = dev.get_analog_input(0)
print(volts)
dev.set_analog_output(0, 1000)
volts = dev.get_analog_input(0)
print(volts)