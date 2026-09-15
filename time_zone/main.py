import sys

from PyQt6.QtWidgets import QApplication

from clock1 import DigitalClockV1

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    
    clock1 = DigitalClockV1()
    clock1.setWindowTitle("Digital Clock V1")
    clock1.move(300, 80)
    clock1.show()
   
    sys.exit(app.exec())