from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QComboBox, QListWidget
from PySide6.QtUiTools import loadUiType
import pymysql
from PySide6.QtGui import QStandardItemModel, QStandardItem


Ui_MainWindow, QMainWindow = loadUiType('myInfosql.ui')

# database = pymysql.Connect(host='localhost', user= 'root', password= 'divineosuuweb@123', database='memberinfo')

# cursur = database.cursor()
# sql = "ALTER memberinfo.memberinfo ADD COLUMN ID PRIMARY KEY AUTOINCREAMENT"

# cursur.execute(sql)

# database.connect()
# database.close()

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.PoBox = self.findChild(QPushButton, "pobox_button")
        self.PoBox_line = self.findChild(QLineEdit, "pobox_line")
        self.Address = self.findChild(QPushButton, "address_button")
        self.Address_line = self.findChild(QLineEdit, "address_line")
        self.Email = self.findChild(QPushButton, "email_button")
        self.Email_line = self.findChild(QLineEdit, "email_line")
        self.Surname = self.findChild(QPushButton, "surname_button")
        self.Surname_line = self.findChild(QLineEdit, "surname_line")
        self.ID = self.findChild(QPushButton, "membid_button")
        self.ID_line = self.findChild(QLineEdit, "id_line")
        # self.list2 = [self.ID_line.text()]

        self.FirstName = self.findChild(QPushButton, "firstname_button")
        self.FirstName_line = self.findChild(QLineEdit, "firstname_line")
        self.Mobile = self.findChild(QPushButton, "mobile_button")
        self.Mobile_line = self.findChild(QLineEdit, "mobile_line")

        self.Gender = self.findChild(QPushButton, "gender_button")
        self.Gender_combo = self.findChild(QComboBox, "gender_combobox") 

        self.Type = self.findChild(QPushButton, "type_button")
        self.Type_Combo = self.findChild(QComboBox, "type_combobox")
    


        self.add_button = self.findChild(QPushButton, "addnew_button")
        # self.add_button.clicked.connect(self.addNew)

        self.record_button = self.findChild(QPushButton,"showrecord_button") 
        # self.record_button.clicked.connect(self.showRecord)

        self.Exit = self.findChild(QPushButton, "exit_button")
        self.Exit.clicked.connect(self.Exit_func)

        self.Search_line = self.findChild(QLineEdit, "search_line")
        self.Search = self.findChild(QPushButton, "search_button")
        # self.Search.clicked.connect(self.search)

        self.Update_button = self.findChild(QPushButton, "update_button")
        # self.Update_button.clicked.connect(self.update_line_edit)

        self.listWidget = self.findChild(QListWidget, "listWidget")


        # self.model = QStandardItemModel()
        # header_label = ["Member ID", "Firstname", "Lastname", "Gender", "Address", "Email", "Mobile Number", "PO Box", "Membership Type" ,  "ID"]
        # self.model.setHorizontalHeaderLabels(header_label)

       
        # self.listWidget.setModel(self.model)



    def Exit_func(self):
        window.close()    



if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()        