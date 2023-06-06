from PySide6.QtWidgets import QMainWindow, QPushButton

# class ButtonHolder(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Button App")
#         button = QPushButton("Click Here")
#         self.setCentralWidget(button)
        
def button_clicked(data):
    print("you've clicked the button, checked : ", data)

# def button_unclicked():
#     print("We've finish clicking")         