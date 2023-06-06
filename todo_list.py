

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

import sqlite3



db = sqlite3.connect('my_list_sql.db')

c = db.cursor()

c.execute("""CREATE TABLE if not exists list_table(
     list_item text

)""")

db.commit()
db.close()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(324, 285)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 10, 322, 253))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.add_item_line_edit = QLineEdit(self.widget)
        self.add_item_line_edit.setObjectName(u"add_item_line_edit")

        self.verticalLayout.addWidget(self.add_item_line_edit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.view_item = QPushButton(self.widget, clicked = lambda : self.save())
        self.view_item.setText("Save")
        self.view_item.setObjectName(u"view_item")

        self.horizontalLayout.addWidget(self.view_item)

        self.add_item = QPushButton(self.widget, clicked = lambda : self.add())
        self.add_item.setObjectName(u"add_item")

        self.horizontalLayout.addWidget(self.add_item)

        self.delete_item = QPushButton(self.widget, clicked = lambda : self.delete())
        self.delete_item.setObjectName(u"delete_item")

        self.horizontalLayout.addWidget(self.delete_item)

        self.clear_item = QPushButton(self.widget, clicked = lambda : self.clear())
        self.clear_item.setObjectName(u"clear_item")

        self.horizontalLayout.addWidget(self.clear_item)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.listWidget = QListWidget(self.widget)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 324, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def delete(self):
        self.listWidget.takeItem(self.listWidget.currentRow())    

    def add(self):

        if self.add_item_line_edit.text() == "" :
            pass

        else:
            # add_it = self.add_item_line_edit
            self.listWidget.addItem(f'{self.add_item_line_edit.text()}')

            self.add_item_line_edit.setText("")

    def clear(self):
        
        self.listWidget.clear()

    def save(self):

        db = sqlite3.connect('my_list_sql.db')

        c = db.cursor()

        c.execute("DELETE FROM list_table ;",)

        
        item = []

        for index in range(self.listWidget.count()):
            item.append(self.listWidget.item(index))

        for list in item:
            # print(list.text())    
            c.execute("INSERT INTO list_table VALUES(:item)",
                      {
                       'item': list.text()   
                      })
    
        db.commit()
        db.close()



            
    # setupUi
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"todo_list", None))
        self.view_item.setText(QCoreApplication.translate("MainWindow", u"View Item", None))
        self.add_item.setText(QCoreApplication.translate("MainWindow", u"Add Item", None))
        self.delete_item.setText(QCoreApplication.translate("MainWindow", u"Delete Item", None))
        self.clear_item.setText(QCoreApplication.translate("MainWindow", u"Clear Item", None))
    # retranslateUi

        self.take_all_item()
    def take_all_item(self):
        db = sqlite3.connect('my_list_sql.db')

        c = db.cursor()

        c.execute("SELECT * FROM list_table")
        
        results = c.fetchall()
        db.commit()
        db.close()

        for result in results:
            self.listWidget.addItem(str(result[0]))


            

class todo_list(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)



if __name__ == '__main__':
    import sys

    app= QApplication(sys.argv)
    todo = todo_list()

    todo.show()
    app.exec()        