# This file must be run with python -i run_experiment.py or the plot won't show
import os
import sys


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from time import sleep
import pyqtgraph as pg
import threading
from PythonForTheLab.Model.experiment import Experiment


experiment = Experiment('experiment.yml')
experiment.load_config()
experiment.load_daq()
t = threading.Thread(target=experiment.do_scan)
t.start()
t2 = threading.Thread(target=experiment.do_scan)
t2.start()

PlotWidget = pg.plot(title="Plotting I vs V")
PlotWidget.setLabel('bottom', f"Channel: {experiment.config['Scan']['channel_out']}", units = "V")
PlotWidget.setLabel('left', f"Channel: {experiment.config['Scan']['channel_in']}", units = "V")

while t.is_alive():
    PlotWidget.plot(experiment.scan_range, experiment.scan_data, clear=True)
    pg.QtGui.QApplication.processEvents()
    sleep(.1)

experiment.finalize()