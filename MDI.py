from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget, QTextEdit, QPushButton, QVBoxLayout, QWidget, QInputDialog, QMenuBar,QMenu
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)
        
    

        self.new_button = QPushButton("New")
        self.new_button.clicked.connect(self.create_new_tab)

        self.toolbar = self.addToolBar("Toolbar")
        self.toolbar.addWidget(self.new_button)

        self.create_new_tab()

    def create_new_tab(self):
        text_edit = QTextEdit()

        title, ok = QInputDialog.getText(self, "Enter Title", "Tab Title:")
        if ok and title:
            tab_index = self.tab_widget.addTab(text_edit, title)
            self.tab_widget.setCurrentIndex(tab_index)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
