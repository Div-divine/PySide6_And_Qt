from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QFileDialog
from PySide6.QtGui import QIcon
import sys

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("My Notepad")
window.setGeometry(100, 100, 800, 600)

text_edit = QTextEdit(window)
window.setCentralWidget(text_edit)

current_file_path = ""

def new_file():
    global current_file_path
    text_edit.clear()
    current_file_path = ""

def open_file():
    global current_file_path
    file_dialog = QFileDialog(window)
    file_path, _ = file_dialog.getOpenFileName()
    if file_path:
        with open(file_path, "r") as file:
            text_edit.setText(file.read())
        current_file_path = file_path

def save_file():
    global current_file_path
    if current_file_path:
        with open(current_file_path, "w") as file:
            file.write(text_edit.toPlainText())
    else:
        save_file_as()

def save_file_as():
    global current_file_path
    file_dialog = QFileDialog(window)
    file_path, _ = file_dialog.getSaveFileName()
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_edit.toPlainText())
        current_file_path = file_path

menu_bar = window.menuBar()
file_menu = menu_bar.addMenu("File")

new_action = file_menu.addAction("New")
new_action.triggered.connect(new_file)

open_action = file_menu.addAction("Open")
open_action.triggered.connect(open_file)

save_action = file_menu.addAction("Save")
save_action.triggered.connect(save_file)

save_as_action = file_menu.addAction("Save As")
save_as_action.triggered.connect(save_file_as)

window.show()
sys.exit(app.exec())
