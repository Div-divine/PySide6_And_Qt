
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

import sys

class Ui_Calculator(object):
    def setupUi(self, Calculator):
        if not Calculator.objectName():
            Calculator.setObjectName(u"Calculator")
        Calculator.resize(202, 302)
        Calculator.setWindowOpacity(1.000000000000000)
        self.actionQuit = QAction(Calculator)
        self.actionQuit.setObjectName(u"actionQuit")
        self.centralwidget = QWidget(Calculator)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.result = QLineEdit(self.centralwidget)
        self.result.setObjectName(u"result")
        self.result.setMinimumSize(QSize(0, 51))
        self.result.setMaximumSize(QSize(16777215, 51))
        self.result.setStyleSheet('''
        background-color : blue;
        color : white;
        ''')


        self.verticalLayout.addWidget(self.result)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn2 = QPushButton(self.centralwidget, clicked= lambda : self.press_button("2"))
        self.btn2.setObjectName(u"btn2")
        self.btn2.setMinimumSize(QSize(41, 41))
        self.btn2.setMaximumSize(QSize(41, 41))
        self.btn2.setText(u"2")

        self.gridLayout.addWidget(self.btn2, 0, 1, 1, 1)

        self.btn6 = QPushButton(self.centralwidget, clicked= lambda : self.press_button("6"))
        self.btn6.setObjectName(u"btn6")
        self.btn6.setMinimumSize(QSize(41, 41))
        self.btn6.setMaximumSize(QSize(41, 41))
        self.btn6.setText(u"6")

        self.gridLayout.addWidget(self.btn6, 1, 2, 1, 1)

        self.btn4 = QPushButton(self.centralwidget, clicked= lambda : self.press_button("4"))
        self.btn4.setObjectName(u"btn4")
        self.btn4.setMinimumSize(QSize(41, 41))
        self.btn4.setMaximumSize(QSize(41, 41))
        self.btn4.setText(u"4")

        self.gridLayout.addWidget(self.btn4, 1, 0, 1, 1)

        self.btn3 = QPushButton(self.centralwidget, clicked= lambda : self.press_button("3"))
        self.btn3.setObjectName(u"btn3")
        self.btn3.setMinimumSize(QSize(41, 41))
        self.btn3.setMaximumSize(QSize(41, 41))
        self.btn3.setText(u"3")

        self.gridLayout.addWidget(self.btn3, 0, 2, 1, 1)

        self.btn7 = QPushButton(self.centralwidget, clicked= lambda : self.press_button("7"))
        self.btn7.setObjectName(u"btn7")
        self.btn7.setMinimumSize(QSize(41, 41))
        self.btn7.setMaximumSize(QSize(41, 41))
        self.btn7.setText(u"7")

        self.gridLayout.addWidget(self.btn7, 2, 0, 1, 1)

        self.btn_times = QPushButton(self.centralwidget, clicked= lambda : self.press_button("x"))
        self.btn_times.setObjectName(u"btn_times")
        self.btn_times.setMinimumSize(QSize(41, 41))
        self.btn_times.setMaximumSize(QSize(41, 41))
        self.btn_times.setText(u"*")

        self.gridLayout.addWidget(self.btn_times, 2, 3, 1, 1)

        self.btn9 = QPushButton(self.centralwidget, clicked= lambda : self.press_button("9"))
        self.btn9.setObjectName(u"btn9")
        self.btn9.setMinimumSize(QSize(41, 41))
        self.btn9.setMaximumSize(QSize(41, 41))
        self.btn9.setText(u"9")

        self.gridLayout.addWidget(self.btn9, 2, 2, 1, 1)

        self.btn5 = QPushButton(self.centralwidget, clicked= lambda : self.press_button("5"))
        self.btn5.setObjectName(u"btn5")
        self.btn5.setMinimumSize(QSize(41, 41))
        self.btn5.setMaximumSize(QSize(41, 41))
        self.btn5.setText(u"5")

        self.gridLayout.addWidget(self.btn5, 1, 1, 1, 1)

        self.btn1 = QPushButton(self.centralwidget, clicked= lambda : self.press_button("1"))
        self.btn1.setObjectName(u"btn1")
        self.btn1.setMinimumSize(QSize(41, 41))
        self.btn1.setMaximumSize(QSize(41, 41))
        self.btn1.setText(u"1")

        self.gridLayout.addWidget(self.btn1, 0, 0, 1, 1)

        self.btn_divide = QPushButton(self.centralwidget, clicked= lambda : self.press_button("/"))
        self.btn_divide.setObjectName(u"btn_divide")
        self.btn_divide.setMinimumSize(QSize(41, 41))
        self.btn_divide.setMaximumSize(QSize(41, 41))
        self.btn_divide.setText(u"/")

        self.gridLayout.addWidget(self.btn_divide, 1, 3, 1, 1)

        self.btn8 = QPushButton(self.centralwidget, clicked= lambda : self.press_button("8"))
        self.btn8.setObjectName(u"btn8")
        self.btn8.setMinimumSize(QSize(41, 41))
        self.btn8.setMaximumSize(QSize(41, 41))
        self.btn8.setText(u"8")

        self.gridLayout.addWidget(self.btn8, 2, 1, 1, 1)

        self.btn_minus = QPushButton(self.centralwidget, clicked= lambda : self.press_button("-"))
        self.btn_minus.setObjectName(u"btn_minus")
        self.btn_minus.setMinimumSize(QSize(41, 41))
        self.btn_minus.setMaximumSize(QSize(41, 41))
        self.btn_minus.setText(u"-")

        self.gridLayout.addWidget(self.btn_minus, 0, 3, 1, 1)

        self.btn_equal = QPushButton(self.centralwidget, clicked= lambda : self.press_button("="))
        self.btn_equal.setObjectName(u"btn_equal")
        self.btn_equal.setMinimumSize(QSize(41, 41))
        self.btn_equal.setMaximumSize(QSize(41, 41))
        self.btn_equal.setText(u"=")

        self.gridLayout.addWidget(self.btn_equal, 3, 3, 1, 1)

        self.btn_plus = QPushButton(self.centralwidget, clicked= lambda : self.press_button("+"))
        self.btn_plus.setObjectName(u"btn_plus")
        self.btn_plus.setMinimumSize(QSize(41, 41))
        self.btn_plus.setMaximumSize(QSize(41, 41))
        self.btn_plus.setText(u"+")

        self.gridLayout.addWidget(self.btn_plus, 3, 2, 1, 1)

        self.btn0 = QPushButton(self.centralwidget, clicked= lambda : self.press_button("0"))
        self.btn0.setObjectName(u"btn0")
        self.btn0.setMinimumSize(QSize(41, 41))
        self.btn0.setMaximumSize(QSize(41, 41))
        self.btn0.setText(u"0")

        self.gridLayout.addWidget(self.btn0, 3, 1, 1, 1)

        self.btn_clear = QPushButton(self.centralwidget, clicked= lambda : self.press_button("C"))
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setMinimumSize(QSize(41, 41))
        self.btn_clear.setMaximumSize(QSize(41, 41))
        self.btn_clear.setText(u"c")

        self.gridLayout.addWidget(self.btn_clear, 3, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        Calculator.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Calculator)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 202, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        Calculator.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Calculator)
        self.statusbar.setObjectName(u"statusbar")
        Calculator.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionQuit)

        self.retranslateUi(Calculator)

        QMetaObject.connectSlotsByName(Calculator)
    # setupUi

    def retranslateUi(self, Calculator):
        Calculator.setWindowTitle(QCoreApplication.translate("Calculator", u"Simple Calculator", None))
        self.actionQuit.setText(QCoreApplication.translate("Calculator", u"Quit", None))
#if QT_CONFIG(shortcut)
        self.actionQuit.setShortcut(QCoreApplication.translate("Calculator", u"Shift+Q", None))
#endif // QT_CONFIG(shortcut)
        self.menuFile.setTitle(QCoreApplication.translate("Calculator", u"File", None))
    # retranslateUi


    def press_button(self, value):
        if value == "C":
            self.result.setText("0")
        elif self.result.text() == "0":
            self.result.setText("")
            self.result.setText(f'{self.result.text()}{value}')
                
        else:    
            self.result.setText(f'{self.result.text()}{value}')


class Calculator(QMainWindow, Ui_Calculator):
    def __init__(self):
       super().__init__()

       self.setupUi(self)


if __name__ == '__main__':

    app = QApplication(sys.argv)

    widget = Calculator()
    
    widget.show()
    app.exec()

            



