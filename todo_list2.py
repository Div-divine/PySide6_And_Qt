
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

from PySide6.QtWidgets import QMessageBox

import sqlite3

conn = sqlite3.connect('todo_list.db')

c = conn.cursor()

c.execute("""CREATE TABLE if not exists my_list(
    list_item  text)
    """)

conn.commit()
conn.close()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(406, 313)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 10, 403, 253))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.add_item_line_edit = QLineEdit(self.layoutWidget)
        self.add_item_line_edit.setObjectName(u"add_item_line_edit")

        self.verticalLayout.addWidget(self.add_item_line_edit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.view_item = QPushButton(self.layoutWidget, clicked = lambda : self.view())
        self.view_item.setObjectName(u"view_item")

        self.horizontalLayout.addWidget(self.view_item)

        self.add_item = QPushButton(self.layoutWidget, clicked = lambda: self.add())
        self.add_item.setObjectName(u"add_item")

        self.horizontalLayout.addWidget(self.add_item)

        self.delete_item = QPushButton(self.layoutWidget, clicked = lambda : self.delete())
        self.delete_item.setObjectName(u"delete_item")

        self.horizontalLayout.addWidget(self.delete_item)

        self.clear_item = QPushButton(self.layoutWidget, clicked = lambda: self.clear())
        self.clear_item.setObjectName(u"clear_item")

        self.horizontalLayout.addWidget(self.clear_item)

        self.save_item = QPushButton(self.layoutWidget, clicked = lambda: self.save())
        self.save_item.setObjectName(u"save_item")
        self.save_item.setStyleSheet('''
        background-color: blue;
        color: white
        ''')

        self.horizontalLayout.addWidget(self.save_item)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.listWidget = QListWidget(self.layoutWidget)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 406, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.showMessage("Copywrite: divineosuuweb@gmail.com")
        self.statusbar.setStyleSheet('''
        color: red;
        ''')
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def add(self):

        if self.add_item_line_edit.text() == "":
            pass

        else:
            self.listWidget.addItem(f'{self.add_item_line_edit.text()}')

            self.add_item_line_edit.setText("")


    def delete(self):
        self.listWidget.takeItem(self.listWidget.currentRow()) 
        


    def clear(self):
        self.listWidget.clear() 


    def view(self):

        self.listWidget.show()   


    def save(self):

        conn = sqlite3.connect('todo_list.db')

        c = conn.cursor()
        c.execute('DELETE FROM my_list;',)


        items = []

        for index in range(self.listWidget.count()):
            items.append(self.listWidget.item(index))



        for item in items:

            # print(item.text())  

           c.execute("INSERT INTO my_list VALUES (:item)",
                     {
                         'item': item.text()
                     })

        conn.commit()
        conn.close()

        msg = QMessageBox()
        msg.setWindowTitle("Saved")
        msg.setText("Your changes has been saved succesfully!")
        msg.setIcon(QMessageBox.Information)

        msg_exec = msg.exec()
     

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"todo_list", None))
        self.view_item.setText(QCoreApplication.translate("MainWindow", u"View Item", None))
        self.add_item.setText(QCoreApplication.translate("MainWindow", u"Add Item", None))
        self.delete_item.setText(QCoreApplication.translate("MainWindow", u"Delete Item", None))
        self.clear_item.setText(QCoreApplication.translate("MainWindow", u"Clear Item", None))
        self.save_item.setText(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi

        self.grab_items()

    def grab_items(self):

        conn = sqlite3.connect('todo_list.db')

        c = conn.cursor()

        c.execute("SELECT * FROM my_list")

        records = c.fetchall()

        conn.commit()
        conn.close()


        for record in records:
            self.listWidget.addItem(str(record[0]))


            



class todo_list(QMainWindow, Ui_MainWindow)  :
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    todo = todo_list()

    todo.show()
    app.exec()          

