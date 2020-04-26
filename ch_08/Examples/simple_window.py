from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

def button_clicked():
    print('Button Clicked')

app = QApplication([])
win = QMainWindow()
win.setWindowTitle('My First Window')
button = QPushButton('Press Me')
button.clicked.connect(button_clicked)
win.setCentralWidget(button)
win.show()
app.exec()