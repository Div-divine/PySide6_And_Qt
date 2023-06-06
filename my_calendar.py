from PySide6.QtWidgets import QApplication, QMainWindow, QCalendarWidget, QLabel
from PySide6.QtUiTools import loadUiType
from PySide6.QtCore import QDate


Ui_MainWindow, QMainWindow = loadUiType('calendar.ui')

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.calendar = self.findChild(QCalendarWidget, 'calendarWidget')
        self.label = self.findChild(QLabel, 'label')

        self.current_date = QDate.currentDate() 

        self.calendar.selectionChanged.connect(self.Date_output)
        self.calendar.setMaximumDate(self.current_date)


    def Date_output(self):

        dateSelected = self.calendar.selectedDate() 

        # we can also use .toPyDate() instead of .toString()

        self.label.setText(f'You are born on {dateSelected.toString()}')



if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = App()

    window.show()
    app.exec()        