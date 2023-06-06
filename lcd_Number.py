from PySide6.QtWidgets import QApplication, QMainWindow, QLCDNumber
from PySide6.QtCore import QTimer, QDateTime
import sys



app = QApplication(sys.argv)
window = QMainWindow()

lcdNumber = QLCDNumber()
lcdNumber.setDigitCount(8)

lcdNumber.setStyleSheet('''
background-color: yellow;
''')

def update_time():
    current_time = QDateTime.currentDateTime()
    lcdNumber.display(current_time.toString("hh:mm:ss"))


timer = QTimer()
timer.timeout.connect(update_time)
timer.start(1000)

update_time()

window.setCentralWidget(lcdNumber)
window.show()
app.exec()