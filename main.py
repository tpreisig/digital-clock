import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt, QTime, QTimer
from PyQt6.QtGui import QLinearGradient, QBrush, QPalette

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel("16:40:20", self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setFixedSize(800, 400)
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_label.setStyleSheet("""
            font-size: 120px;
            font-family: 'Avenir';
            color: aliceblue;
            font-weight: 900;
        """)
        # Setting up the linear gradient background
        palette = QPalette()
        gradient = QLinearGradient(0, 0, self.width(), self.height())
        gradient.setColorAt(0.0, Qt.GlobalColor.darkBlue)
        gradient.setColorAt(1.0, Qt.GlobalColor.cyan)
        brush = QBrush(gradient)
        palette.setBrush(QPalette.ColorRole.Window, brush)
        self.setPalette(palette)

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss")
        self.time_label.setText(current_time)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DigitalClock()
    # ex.show() inherits from QWidget
    ex.show()
    sys.exit(app.exec())