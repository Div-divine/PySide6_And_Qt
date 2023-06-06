from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog
from PySide6.QtUiTools import loadUiType


Ui_MainWindow, QMainWindow = loadUiType('Dialogue.ui')

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        self.button = self.findChild(QPushButton, 'pushButton')
        self.label = self.findChild(QLabel, 'label')


        self.button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        
          
        file_name = QFileDialog.getOpenFileName(self,"Open File", "\OneDrive\Pictures\Picture_File", "All Files (*);; Python Files (*.py);; Image Files (*.jpg *.png);; Text Files (*.txt)")

        if file_name:
            self.label.setText(str(file_name))
        

       

        
    

   
    
if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = App()

    window.show()
    
    app.exec()        