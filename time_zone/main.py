import sys

from PyQt6.QtWidgets import QApplication

from clock1 import DigitalClockV1
from clock2 import DigitalClockV2
from clock3 import DigitalClockV3

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    
    clock1 = DigitalClockV1()
    clock2 = DigitalClockV2()
    clock3 = DigitalClockV3()

    clock1.setWindowTitle("Digital Clock V1")
    clock2.setWindowTitle("Digital Clock V2")
    clock3.setWindowTitle("Digital Clock V3")

    clock1.move(300, 80)
    clock2.move(300, 120)
    clock3.move(300, 160)
    
    clock1.show()
    clock2.show()
    clock3.show()
   
    sys.exit(app.exec())