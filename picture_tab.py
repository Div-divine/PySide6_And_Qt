

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QStatusBar,
    QTabWidget, QToolBar, QWidget)

from PySide6.QtWidgets import QPushButton

from todo_list2 import Ui_MainWindow, todo_list

class Ui_Picture_tab(object):

    def second_window(self):

        self.window = todo_list()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)

        self.window.show()

    def setupUi(self, Picture_tab):
        if not Picture_tab.objectName():
            Picture_tab.setObjectName(u"Picture_tab")
        Picture_tab.resize(643, 632)
        self.actionOpen = QAction(Picture_tab)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionNew = QAction(Picture_tab)
        self.actionNew.setObjectName(u"actionNew")
        self.actionSave = QAction(Picture_tab)
        self.actionSave.setObjectName(u"actionSave")
        self.actionDelete = QAction(Picture_tab)
        self.actionDelete.setObjectName(u"actionDelete")
        self.actionCut = QAction(Picture_tab)
        self.actionCut.setObjectName(u"actionCut")
        self.actionPaste = QAction(Picture_tab)
        self.actionPaste.setObjectName(u"actionPaste")
        self.actionAbout = QAction(Picture_tab)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionPrint = QAction(Picture_tab)
        self.actionPrint.setObjectName(u"actionPrint")
        icon = QIcon()
        icon.addFile(u"../../../Downloads/printer.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionPrint.setIcon(icon)
        self.actionPrint.setMenuRole(QAction.NoRole)
        self.actionHome = QAction(Picture_tab)
        self.actionHome.setObjectName(u"actionHome")
        icon1 = QIcon()
        icon1.addFile(u"../../../Downloads/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionHome.setIcon(icon1)
        self.actionHome.setMenuRole(QAction.NoRole)
        self.actionCut_2 = QAction(Picture_tab)
        self.actionCut_2.setObjectName(u"actionCut_2")
        icon2 = QIcon()
        icon2.addFile(u"../../../Downloads/scissors.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCut_2.setIcon(icon2)
        self.actionCut_2.setMenuRole(QAction.NoRole)
        self.centralwidget = QWidget(Picture_tab)
        self.centralwidget.setObjectName(u"centralwidget")
        self.second_tab_2 = QTabWidget(self.centralwidget)
        self.second_tab_2.setObjectName(u"second_tab_2")
        self.second_tab_2.setGeometry(QRect(10, 10, 621, 551))
        self.second_tab_2.setTabsClosable(True)
        self.first_tab = QWidget()
        self.first_tab.setObjectName(u"first_tab")
        self.first_label = QLabel(self.first_tab)
        self.first_label.setObjectName(u"first_label")
        self.first_label.setGeometry(QRect(-230, -330, 861, 1024))
        self.first_label.setMinimumSize(QSize(331, 251))
        self.first_label.setPixmap(QPixmap(u"../../../Pictures/.thumbnails/4225.jpg"))
        self.second_tab_2.addTab(self.first_tab, "")
        self.second_tab = QWidget()
        self.second_tab.setObjectName(u"second_tab")
        self.label_2 = QLabel(self.second_tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 30, 591, 451))
        self.label_2.setPixmap(QPixmap(u"../../../Pictures/.thumbnails/4272.jpg"))
        self.lineEdit = QLineEdit(self.second_tab)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(2, 0, 301, 21))
        self.second_tab_2.addTab(self.second_tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.lineEdit_2 = QLineEdit(self.tab_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(22, 30, 211, 21))
        # self.lineEdit_2.setStyleSheet('''
        # color: green;
        # ''')
        self.second_tab_2.addTab(self.tab_2, "")
        self.Third_tab = QWidget()
        self.Third_tab.setObjectName(u"Third_tab")
        self.third_label = QLabel(self.Third_tab)
        self.third_label.setObjectName(u"third_label")
        self.third_label.setGeometry(QRect(120, 0, 751, 481))
        self.third_label.setPixmap(QPixmap(u"../../../Pictures/.thumbnails/6171.jpg"))
        self.second_tab_2.addTab(self.Third_tab, "")
        Picture_tab.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Picture_tab)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 643, 22))
        self.menufile = QMenu(self.menubar)
        self.menufile.setObjectName(u"menufile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        Picture_tab.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Picture_tab)

        self.button = QPushButton("Click Here To open Todo list window", clicked = lambda : self.second_window())
        self.button.setStyleSheet('''
        background-color : green;
        color : white
        ''')
        self.statusbar.addWidget(self.button)
        self.statusbar.setObjectName(u"statusbar")
        Picture_tab.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(Picture_tab)
        self.toolBar.setObjectName(u"toolBar")
        Picture_tab.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menufile.addAction(self.actionOpen)
        self.menufile.addAction(self.actionNew)
        self.menufile.addAction(self.actionSave)
        self.menufile.addAction(self.actionDelete)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionPaste)
        self.menuHelp.addAction(self.actionAbout)
        self.toolBar.addAction(self.actionHome)
        self.toolBar.addAction(self.actionPrint)
        self.toolBar.addAction(self.actionCut_2)

        self.retranslateUi(Picture_tab)

        self.second_tab_2.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Picture_tab)
    # setupUi

    def retranslateUi(self, Picture_tab):
        Picture_tab.setWindowTitle(QCoreApplication.translate("Picture_tab", u"Picture_tab", None))
        self.actionOpen.setText(QCoreApplication.translate("Picture_tab", u"Open", None))
        self.actionNew.setText(QCoreApplication.translate("Picture_tab", u"New", None))
        self.actionSave.setText(QCoreApplication.translate("Picture_tab", u"Save", None))
        self.actionDelete.setText(QCoreApplication.translate("Picture_tab", u"Delete", None))
        self.actionCut.setText(QCoreApplication.translate("Picture_tab", u"Cut", None))
        self.actionPaste.setText(QCoreApplication.translate("Picture_tab", u"Paste", None))
        self.actionAbout.setText(QCoreApplication.translate("Picture_tab", u"About", None))
        self.actionPrint.setText(QCoreApplication.translate("Picture_tab", u"Print", None))
        self.actionHome.setText(QCoreApplication.translate("Picture_tab", u"Home", None))
        self.actionCut_2.setText(QCoreApplication.translate("Picture_tab", u"Cut", None))
        self.first_label.setText("")
        self.second_tab_2.setTabText(self.second_tab_2.indexOf(self.first_tab), QCoreApplication.translate("Picture_tab", u"Me Eating", None))
        self.label_2.setText("")
        self.lineEdit.setText(QCoreApplication.translate("Picture_tab", u"Happy Family", None))
        self.second_tab_2.setTabText(self.second_tab_2.indexOf(self.second_tab), QCoreApplication.translate("Picture_tab", u"My Little Family", None))
        self.lineEdit_2.setText(QCoreApplication.translate("Picture_tab", u"Hello", None))
        self.second_tab_2.setTabText(self.second_tab_2.indexOf(self.tab_2), QCoreApplication.translate("Picture_tab", u"Page", None))
        self.third_label.setText("")
        self.second_tab_2.setTabText(self.second_tab_2.indexOf(self.Third_tab), QCoreApplication.translate("Picture_tab", u"My Lovely Little Princess", None))
        self.menufile.setTitle(QCoreApplication.translate("Picture_tab", u"file", None))
        self.menuEdit.setTitle(QCoreApplication.translate("Picture_tab", u"Edit", None))
        self.menuHelp.setTitle(QCoreApplication.translate("Picture_tab", u"Help", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("Picture_tab", u"toolBar", None))
    # retranslateUi


        tabs = self.second_tab_2
        tabs.tabCloseRequested.connect(lambda index: tabs.removeTab(index))

             

    # def add_second_window(self):
        
class pictures(QMainWindow, Ui_Picture_tab):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == '__main__':
    import sys

    app= QApplication(sys.argv)
    pics = pictures()

    pics.show()
    app.exec()        
        

