from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog
from PySide6.QtUiTools import loadUiType
from PySide6.QtGui import QPixmap




Ui_MainWindow, QMainWindow = loadUiType('image_select.ui')


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.button = self.findChild(QPushButton, 'pushButton')
        self.label = self.findChild(QLabel, 'label')

        self.button.clicked.connect(self.File_Dialog)


    def File_Dialog(self):
        get_into_files = QFileDialog.getOpenFileName(self, "Open File", "", "ALL FILES (*)")

        self.pixmap = QPixmap(get_into_files[0])

        self.label.setPixmap(self.pixmap)
if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = App()

    window.show()
    app.exec()        