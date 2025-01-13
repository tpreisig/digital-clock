import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt, QTime, QTimer
from PyQt6.QtGui import QLinearGradient, QBrush, QPalette

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel("06:06:06", self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setFixedSize(800, 400)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # linear gradient background
        palette = QPalette()
        gradient = QLinearGradient(0, 0, self.width(), self.height())
        gradient.setColorAt(0.0, Qt.GlobalColor.darkBlue)
        gradient.setColorAt(1.0, Qt.GlobalColor.cyan)
        brush = QBrush(gradient)
        palette.setBrush(QPalette.ColorRole.Window, brush)
        self.setPalette(palette)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # ex.show() method inherited from QWidget class
    ex = DigitalClock()
    ex.show()
    sys.exit(app.exec())


