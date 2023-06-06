

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

from todo_list2 import Ui_MainWindow, todo_list



import sys

class Ui_LogginForm(object):

    def input_to_todo_list(self):
        self.window = todo_list()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    



        if self.enter_button.isChecked :

            self.ui.listWidget.addItem(f'User {self.firstname_label.text()} is :  {self.firstname_line.text()}')
            self.ui.listWidget.addItem(f'User {self.lastname_label.text()} is  : {self.lastname_line.text()}')
            self.ui.listWidget.addItem(f'User {self.email_label.text()} is {self.email_line.text()}')




            
            

    def setupUi(self, LogginForm):
        if not LogginForm.objectName():
            LogginForm.setObjectName(u"LogginForm")
        LogginForm.resize(460, 270)
        self.centralwidget = QWidget(LogginForm)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout_2 = QFormLayout(self.centralwidget)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.firstname_line = QLineEdit(self.centralwidget)
        self.firstname_line.setObjectName(u"firstname_line")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.firstname_line)

        self.lastname_label = QLabel(self.centralwidget)
        self.lastname_label.setObjectName(u"lastname_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lastname_label)

        self.lastname_line = QLineEdit(self.centralwidget)
        self.lastname_line.setObjectName(u"lastname_line")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lastname_line)

        self.email_label = QLabel(self.centralwidget)
        self.email_label.setObjectName(u"email_label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.email_label)

        self.email_line = QLineEdit(self.centralwidget)
        self.email_line.setObjectName(u"email_line")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.email_line)

        self.password_label = QLabel(self.centralwidget)
        self.password_label.setObjectName(u"password_label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.password_label)

        self.password_line = QLineEdit(self.centralwidget)
        self.password_line.setObjectName(u"password_line")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.password_line)

        self.enter_button = QPushButton(self.centralwidget, clicked = lambda: self.input_to_todo_list())
        self.enter_button.setObjectName(u"enter_button")
        self.enter_button.setMaximumSize(QSize(100, 40))
        font = QFont()
        font.setFamilies([u"Arial"])
        self.enter_button.setFont(font)
        self.enter_button.setStyleSheet('''
        background-color : blue;
        color: white;
        ''')

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.enter_button)

        self.firstname_label = QLabel(self.centralwidget)
        self.firstname_label.setObjectName(u"firstname_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.firstname_label)


        self.formLayout_2.setLayout(0, QFormLayout.SpanningRole, self.formLayout)

        LogginForm.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(LogginForm)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 460, 22))
        LogginForm.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(LogginForm)
        self.statusbar.setObjectName(u"statusbar")
        LogginForm.setStatusBar(self.statusbar)

        self.retranslateUi(LogginForm)

        QMetaObject.connectSlotsByName(LogginForm)
    # setupUi

    def retranslateUi(self, LogginForm):
        LogginForm.setWindowTitle(QCoreApplication.translate("LogginForm", u"MainWindow", None))
        self.lastname_label.setText(QCoreApplication.translate("LogginForm", u"Last Name ", None))
        self.email_label.setText(QCoreApplication.translate("LogginForm", u"Email ", None))
        self.password_label.setText(QCoreApplication.translate("LogginForm", u"Password ", None))
        self.enter_button.setText(QCoreApplication.translate("LogginForm", u"Enter", None))
        self.firstname_label.setText(QCoreApplication.translate("LogginForm", u"First Name ", None))
    # retranslateUi



class show_form(QMainWindow, Ui_LogginForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    form = show_form()

    form.show()
    app.exec()


           
