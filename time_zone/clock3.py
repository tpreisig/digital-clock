from PyQt6.QtCore import Qt, QTime, QTimer
from PyQt6.QtGui import QColor, QFont, QLinearGradient, QPainter
from PyQt6.QtWidgets import QLabel, QVBoxLayout, QWidget


class DigitalClockV3(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel()
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock V3")
        self.resize(800, 400)

        layout = QVBoxLayout(self)
        layout.addWidget(self.time_label)

        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont("Arial")
        font.setPixelSize(140)
        self.time_label.setFont(font)
        self.time_label.setStyleSheet("color: aliceblue;")

        self.timer.timeout.connect(self.update_time)
        self.update_time()

    def update_time(self):
        now = QTime.currentTime()
        self.time_label.setText(now.toString("hh:mm:ss"))
        self.timer.start(1000 - now.msec())  # next tick on the second

    def paintEvent(self, event):
        painter = QPainter(self)
        gradient = QLinearGradient(0, 0, self.width(), self.height())
        gradient.setColorAt(0, QColor(Qt.GlobalColor.darkCyan))
        gradient.setColorAt(1, QColor(Qt.GlobalColor.darkBlue))
        painter.fillRect(self.rect(), gradient)
