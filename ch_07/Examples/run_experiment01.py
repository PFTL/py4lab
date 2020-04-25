# This file must be run with python -i run_experiment.py or the plot won't show
import os
import pyqtgraph as pg
import sys


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from PythonForTheLab.Model.experiment import Experiment

experiment = Experiment('experiment.yml')
experiment.load_config()
print(experiment.config)
experiment.load_daq()
print(experiment.daq)
experiment.config['Scan']['num_steps'] = 5
experiment.do_scan()
experiment.save_data()
experiment.config['Scan']['num_steps'] = 10
experiment.do_scan()
experiment.save_data()
PlotWidget = pg.plot(title="Plotting I vs V")
PlotWidget.setLabel('bottom', f"Channel: {experiment.config['Scan']['channel_out']}", units = "V")
PlotWidget.setLabel('left', f"Channel: {experiment.config['Scan']['channel_in']}", units = "V")
PlotWidget.plot(experiment.scan_range, experiment.scan_data)
experiment.finalize()