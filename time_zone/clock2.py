from PyQt6.QtCore import Qt, QTime, QTimer
from PyQt6.QtGui import QBrush, QLinearGradient, QPalette
from PyQt6.QtWidgets import QLabel, QVBoxLayout, QWidget


class DigitalClockV2(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel("16:40:20", self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        # self.setGeometry(300, 400, 800, 400)
        self.resize(800, 400)


        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_label.setStyleSheet("font-size: 140px;"
                                      "font-family: 'Arial';"
                                      "color: aliceblue;")

        # setting up the gradient background
        palette = QPalette()
        gradient = QLinearGradient(0, 0, 800, 400)
        gradient.setColorAt(0, Qt.GlobalColor.darkCyan)
        gradient.setColorAt(1, Qt.GlobalColor.darkYellow)
        brush = QBrush(gradient)
        palette.setBrush(QPalette.ColorRole.Window, brush)
        self.setPalette(palette)

        self.timer.timeout.connect(self.update_time)
        # self.timer.start(1000)
        self.timer.start(1000)  # next tick on the second

        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss")
        self.time_label.setText(current_time)
