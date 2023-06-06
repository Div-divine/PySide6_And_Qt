from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QFileDialog
from PySide6.QtCore import QTimer
import sys

class NotepadWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Notepad")
        self.setGeometry(100, 100, 800, 600)

        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.autosave_timer = QTimer(self)
        self.autosave_timer.timeout.connect(self.save_contents)
        self.autosave_timer.start(5000)

        # Set the default autosave file path
        self.autosave_file_path = "autosave.txt"


    def save_contents(self):
        text = self.text_edit.toPlainText()

        # Save the text to the default autosave file path
        with open(self.autosave_file_path, "w") as file:
            file.write(text)

    def open_autosave(self):
        # Open a file dialog to choose a new autosave file path
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Autosave File")
        
        if file_path:
            self.autosave_file_path = file_path

app = QApplication(sys.argv)
window = NotepadWindow()
window.show()
sys.exit(app.exec())
