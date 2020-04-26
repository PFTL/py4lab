import os
import sys


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from PyQt5.QtWidgets import QApplication, QPushButton
from PythonForTheLab.View.main_window import MainWindow
from PythonForTheLab.Model.experiment import Experiment

experiment = Experiment('experiment.yml')
experiment.load_config()
experiment.load_daq()

app = QApplication([])
window = MainWindow(experiment)
window.show()
app.exec()

experiment.finalize()