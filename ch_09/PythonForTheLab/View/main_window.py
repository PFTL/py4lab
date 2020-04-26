import os

import pyqtgraph as pg
from PyQt5 import uic
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import (QMainWindow,
                             QPushButton,
                             QWidget,
                             QHBoxLayout,
                             QVBoxLayout, )


class MainWindow(QMainWindow):
    def __init__(self, experiment=None):
        super().__init__()
        self.experiment = experiment
        self.setWindowTitle('Scan Window')

        base_dir = os.path.dirname(os.path.abspath(__file__))
        ui_file = os.path.join(base_dir, 'GUI', 'main_window.ui')
        uic.loadUi(ui_file, self)

        self.plot_widget = pg.PlotWidget(title="Plotting I vs V")
        self.plot = self.plot_widget.plot([0], [0])
        layout = self.central_widget.layout()
        layout.addWidget(self.plot_widget)

        self.start_button.clicked.connect(self.start_scan)
        self.stop_button.clicked.connect(self.stop_scan)
        self.actionSave.triggered.connect(self.experiment.save_data)

        self.start_line.setText(self.experiment.config['Scan']['start'])
        self.stop_line.setText(self.experiment.config['Scan']['stop'])
        self.num_steps_line.setText(str(self.experiment.config['Scan']['num_steps']))
        self.delay_line.setText(self.experiment.config['Scan']['delay'])
        self.out_channel_line.setText(str(self.experiment.config['Scan']['channel_out']))
        self.in_channel_line.setText(str(self.experiment.config['Scan']['channel_in']))

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(50)
        self.timer.timeout.connect(self.update_gui)

    def update_plot(self):
        self.plot.setData(self.experiment.scan_range, self.experiment.scan_data)

    def start_scan(self):
        start = self.start_line.text()
        stop = self.stop_line.text()
        num_steps = int(self.num_steps_line.text())
        delay = self.delay_line.text()
        channel_in = int(self.in_channel_line.text())
        channel_out = int(self.out_channel_line.text())

        self.experiment.config['Scan'].update(
            {'start': start,
             'stop': stop,
             'num_steps': num_steps,
             'channel_in': channel_in,
             'channel_out': channel_out,
             'delay': delay,
             }
        )
        self.experiment.start_scan()

    def update_gui(self):
        if self.experiment.is_running:
            self.start_button.setEnabled(False)
            self.stop_button.setEnabled(True)
        else:
            self.start_button.setEnabled(True)
            self.stop_button.setEnabled(False)

    def stop_scan(self):
        self.experiment.stop_scan()
        print('Stopping Scan')