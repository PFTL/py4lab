import os
import sys


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

from PythonForTheLab.Model.experiment import Experiment

experiment = Experiment('experiment.yml')
experiment.load_config()
experiment.load_daq()

app = QApplication([])
win = QMainWindow()
win.setWindowTitle('My First Window')
button = QPushButton('Start Scan')

button.clicked.connect(experiment.start_scan)

win.setCentralWidget(button)
win.show()
app.exec()

experiment.finalize()