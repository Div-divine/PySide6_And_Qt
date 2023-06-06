from PySide6.QtWidgets import QApplication, QMessageBox, QWidget, QVBoxLayout
import sys

class Message_box(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Message Box")

        layout = QVBoxLayout()
        self.setLayout(layout)
        message = QMessageBox()
        message.setInformativeText("Hope you like the app ?")
        message.setIcon(QMessageBox.Question)
        message.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        layout.addWidget(message)

   

        

app = QApplication(sys.argv)
widget = Message_box()
widget.show()
app.exec()