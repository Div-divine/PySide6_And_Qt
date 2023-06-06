from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QTabWidget, QLabel, QLineEdit, QMenuBar, QMenu, QStatusBar
from PySide6.QtUiTools import loadUiType
import sys



Ui_MainWindow, QMainWindow = loadUiType('My_picture_tab.ui')

class convert_ui_to_python(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.ui.last_button.setStyleSheet('''
        background-color: green ;
        color : white
        ''')

    #     if self.ui.last_button.isChecked :
    #         self.ui.last_button.clicked.connect(self.change_text())

    # def change_text(self):
    #     self.ui.lineEdit_2.setText(f'We are happy Together!')  

              

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = convert_ui_to_python()

    window.show()
    app.exec()        