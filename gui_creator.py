import timetable_extractor
from PyQt5.QtWidgets import *


class GUI(QApplication):
    def __init__(self):
        super(GUI, self).__init__([])
        self.setStyle('Fusion')
        self.window = QWidget()
        self.layout = QVBoxLayout()
        self.layout.addWidget(QPushButton('Top'))
        self.window.setLayout(self.layout)


if __name__ == '__main__':
    gui = GUI()
    gui.window.show()
    gui.exec()
