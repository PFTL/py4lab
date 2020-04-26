# This file must be run with python -i run_experiment.py or the plot won't show
import os
import sys


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from time import sleep
import threading
from PythonForTheLab.Model.experiment import Experiment


experiment = Experiment('experiment.yml')
experiment.load_config()
experiment.load_daq()
scan1 = threading.Thread(target=experiment.do_scan)
scan1.start()
sleep(2)
experiment.keep_running = False
sleep(.5)
print('Experiment finished')
experiment.start_scan()
while experiment.is_running:
    print('Experiment Running')
    sleep(1)
experiment.finalize()