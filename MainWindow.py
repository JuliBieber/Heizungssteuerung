from PyQt6.QtWidgets import QMainWindow
from RadiatorControl import ControlPanel

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)


        tab_widget = ControlPanel(parent)


        self.setCentralWidget(tab_widget)

        self.setWindowTitle("Heizungssteuerung")



