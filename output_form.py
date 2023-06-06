from PySide6.QtWidgets import QMainWindow, QApplication
import sys
from form_QtDesigner import Ui_LogginForm

from todo_list2 import Ui_MainWindow, todo_list





app = QApplication(sys.argv)
main_window = QMainWindow()

widget = Ui_LogginForm()

widget.setupUi(main_window)


# Customize the UI or connect signals and slots as needed
# ...

# Show the main window
main_window.show()




app.exec()