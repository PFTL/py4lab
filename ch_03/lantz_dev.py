from time import sleep

from lantz import Feat, MessageBasedDriver, DictFeat


class MyDevice(MessageBasedDriver):

    DEFAULTS = {'ASRL': {'write_termination': '\n',
                        'read_termination': '\n',
                        'encoding': 'ascii',
                        }}

    _output = [None, None]
    output0 = None

    @Feat()
    def idn(self):
        return self.query('IDN')

    @Feat(limits=(0, 4095, 1))
    def set_output0(self):
        return self.output0

    @set_output0.setter
    def set_output0(self, value):
        command = "OUT:CH0:{}".format(value)
        self.write(command)
        self.output0 = value

    @DictFeat(keys=[0, 1], limits=(0, 4095, 1))
    def output(self, key):
        return self._output[key]

    @output.setter
    def output(self, key, value):
        self.write(f'OUT:CH{key}:{value}')
        self._output[key] = value


dev = MyDevice.via_serial('/dev/ttyACM0')
dev.initialize()
sleep(1)
print(dev.idn)
print(dev.set_output0)
dev.set_output0 = 500
print(dev.set_output0)
dev.output[0] = 500
dev.output[1] = 1000
print(dev.output[0])
print(dev.output[1])