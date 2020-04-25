import sys
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from PythonForTheLab.Model.experiment import Experiment

experiment = Experiment('experiment.yml')
experiment.load_config()
print(experiment.config)
experiment.load_daq()
print(experiment.daq)
experiment.do_scan()
print(experiment.scan_range)
print(experiment.scan_data)
experiment.save_data()
experiment.finalize()