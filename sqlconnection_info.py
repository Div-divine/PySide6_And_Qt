from PySide6.QtWidgets import  QApplication, QVBoxLayout,QMainWindow, QPushButton, QLineEdit, QTreeView, QComboBox, QWidget, QMessageBox, QHeaderView
from PySide6.QtUiTools import loadUiType
from PySide6.QtGui import QStandardItem, QStandardItemModel
import pymysql
from pymysql.cursors import DictCursor
from PySide6.QtCore import QAbstractItemModel, QModelIndex, Qt
from important_info import PASSWORD


database = pymysql.connect(
    host="localhost",
    user="root",
    password=PASSWORD,
    database="testdb"
)

my_cur = database.cursor()

my_cur.execute("""UPDATE testdb.membersinfo SET Member_Id = 76890 AND FirstName= 'Sam' AND LastName= 'Trust'  WHERE ID = 2 """)

database.commit()





Ui_MainWindow , QMainWindow = loadUiType('sqlconnection_info.ui')
class App(QMainWindow):


    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.count = 0

        
        
        self.PoBox = self.findChild(QPushButton, "pobox_button")
        self.PoBox_line = self.findChild(QLineEdit, "pobox_line")
        self.Address = self.findChild(QPushButton, "address_button")
        self.Address_line = self.findChild(QLineEdit, "address_line")
        self.Email = self.findChild(QPushButton, "email_button")
        self.Email_line = self.findChild(QLineEdit, "email_line")
        self.Surname = self.findChild(QPushButton, "surname_button")
        self.Surname_line = self.findChild(QLineEdit, "surname_line")
        self.ID = self.findChild(QPushButton, "memberId_button")
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
    


        self.Treeview = self.findChild(QTreeView, "MembersInfo")

        self.model = QStandardItemModel()
        header_label = ["Member ID", "Firstname", "Lastname", "Gender", "Address", "Email", "Mobile Number", "PO Box", "Membership Type" ,  "ID"]
        self.model.setHorizontalHeaderLabels(header_label)
        
       
        self.Treeview.setModel(self.model)

        self.add_button = self.findChild(QPushButton, "addnew_button")
        self.add_button.clicked.connect(self.addNew)

        self.record_button = self.findChild(QPushButton,"showrecord_button") 
        self.record_button.clicked.connect(self.showRecord)

        self.Exit = self.findChild(QPushButton, "exit_button")
        self.Exit.clicked.connect(self.Exit_func)

        self.Search_line = self.findChild(QLineEdit, "search_line")
        self.Search = self.findChild(QPushButton, "search_button")
        self.Search.clicked.connect(self.search)

        self.Update_button = self.findChild(QPushButton, "update_button")
        self.Update_button.clicked.connect(self.update_line_edit)


        self.line_edit = [self.ID_line, self.FirstName_line, self.Surname_line, self.Gender_combo, self.Address_line, self.Email_line,
                     self.Mobile_line, self.PoBox_line, self.Type_Combo
                     ]
        
        

   

        # Start the event loop
        # sys.exit(app.exec())
        

    def addNew(self):

        self.count+=1

        database = pymysql.connect(
        host="localhost",
        user="root",
        password=PASSWORD,
        database="testdb"
        )

        my_cur = database.cursor()
        sqlFormula = "INSERT INTO membersinfo (Member_Id,FirstName,LastName,Gender,Address,Email,Mobile_Number,PO_Box,Membership_Type ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"



        self.list = [int(self.ID_line.text()), self.FirstName_line.text(), self.Surname_line.text(), self.Gender_combo.currentText(), 
                     self.Address_line.text(), self.Email_line.text(), int(self.Mobile_line.text()), self.PoBox_line.text(), self.Type_Combo.currentText()
                     ]
        
        my_cur.execute(sqlFormula, self.list)

        # self.info = QMessageBox()
        # self.info.setText("Record Entered Successfully!")
        # self.info.setWindowTitle("Your Data has been registered into the database!")
        # self.info.setStandardButtons(QMessageBox.Ok)

       
        database.commit()

        
        

        
        



    def showRecord(self):

        self.model.clear()

        self.model = QStandardItemModel()
        header_label = ["Member ID", "Firstname", "Lastname", "Gender", "Address", "Email", "Mobile Number", "PO Box", "Membership Type" ,  "ID"]
        self.model.setHorizontalHeaderLabels(header_label)

        self.Treeview.setModel(self.model)

        # titles_position = header_label

        # titles_position.setSectionResizeMode(QHeaderView.ResizeToContents)
        # header_label.setSectionResizeMode(0, QHeaderView.Stretch)
        # header_label.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        # header_label.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        

        database = pymysql.connect(
        host="localhost",
        user="root",
        password=PASSWORD,
        database="testdb"
        ) 

        cur = database.cursor()
        cur.execute("""SELECT * FROM testdb.membersinfo""")   

        record = cur.fetchall()

        for row in record:
            item_row = []
            for i, value in enumerate(row):
    
                item = QStandardItem()
                item.setText(str(value))
                item_row.append(item)
            self.model.appendRow(item_row)

            

            database.commit()
        database.close()

        

        

         


    def Exit_func(self) :

        window.close()


    def search(self):

        self.model.clear()

        self.model = QStandardItemModel()
        header_label = ["Member ID", "Firstname", "Lastname", "Gender", "Address", "Email", "Mobile Number", "PO Box", "Membership Type" ,  "ID"]
        self.model.setHorizontalHeaderLabels(header_label)

       
        self.Treeview.setModel(self.model)



        # print(self.list2)
        # pass

        member = self.Search_line.text()

        ##################### Searching for Member Info Using the Member ID ############################################


        database = pymysql.connect(
        host="localhost",
        user="root",
        password=PASSWORD,
        database="testdb"
        )  

        my_cur = database.cursor()
        querie = """SELECT * FROM testdb.membersinfo WHERE Member_Id = %s """
        my_cur.execute(querie, member) 
        record = my_cur.fetchall()


        # print(record)

        for row in record:

            item_row = []
            for i, value in enumerate(row):
    
                item = QStandardItem()
                item.setText(str(value))
                item_row.append(item)
            self.model.appendRow(item_row)

        database.commit()
        database.close() 


        ##################### Searching for Member Info Using Using the Member First Name  ############################################

        database = pymysql.connect(
        host="localhost",
        user="root",
        password=PASSWORD,
        database="testdb"
        )  

        my_cur = database.cursor()
        querie = """SELECT * FROM testdb.membersinfo WHERE FirstName = %s """
        my_cur.execute(querie, member) 
        record = my_cur.fetchall()


        # print(record)

        for row in record:

            item_row = []
            for i, value in enumerate(row):
    
                item = QStandardItem()
                item.setText(str(value))
                item_row.append(item)
            self.model.appendRow(item_row)

        database.commit()
        database.close()

         ##################### Searching for Member Info Using Using the Member Last Name  ############################################

        database = pymysql.connect(
        host="localhost",
        user="root",
        password=PASSWORD,
        database="testdb"
        )  

        my_cur = database.cursor()
        querie = """SELECT * FROM testdb.membersinfo WHERE LastName = %s """
        my_cur.execute(querie, member) 
        record = my_cur.fetchall()


        # print(record)

        for row in record:

            item_row = []
            for i, value in enumerate(row):
    
                item = QStandardItem()
                item.setText(str(value))
                item_row.append(item)
            self.model.appendRow(item_row)

        database.commit()
        database.close()

         ##################### Searching for Member Info Using Using the Member Gender ############################################

        database = pymysql.connect(
        host="localhost",
        user="root",
        password=PASSWORD,
        database="testdb"
        )  

        my_cur = database.cursor()
        querie = """SELECT * FROM testdb.membersinfo WHERE Gender = %s """
        my_cur.execute(querie, member) 
        record = my_cur.fetchall()


        # print(record)

        for row in record:

            item_row = []
            for i, value in enumerate(row):
    
                item = QStandardItem()
                item.setText(str(value))
                item_row.append(item)
            self.model.appendRow(item_row)

        database.commit()
        database.close()

          ##################### Searching for Member Info Using Using the Member Address ############################################

        database = pymysql.connect(
        host="localhost",
        user="root",
        password=PASSWORD,
        database="testdb"
        )  

        my_cur = database.cursor()
        querie = """SELECT * FROM testdb.membersinfo WHERE Address = %s """
        my_cur.execute(querie, member) 
        record = my_cur.fetchall()


        # print(record)

        for row in record:

            item_row = []
            for i, value in enumerate(row):
    
                item = QStandardItem()
                item.setText(str(value))
                item_row.append(item)
            self.model.appendRow(item_row)

        database.commit()
        database.close()

         ##################### Searching for Member Info Using Using the Member Email ############################################

        database = pymysql.connect(
        host="localhost",
        user="root",
        password=PASSWORD,
        database="testdb"
        )  

        my_cur = database.cursor()
        querie = """SELECT * FROM testdb.membersinfo WHERE Email = %s """
        my_cur.execute(querie, member) 
        record = my_cur.fetchall()


        # print(record)

        for row in record:

            item_row = []
            for i, value in enumerate(row):
    
                item = QStandardItem()
                item.setText(str(value))
                item_row.append(item)
            self.model.appendRow(item_row)

        database.commit()
        database.close()

          ##################### Searching for Member Info Using Using the Member Mobile Number  ############################################

        database = pymysql.connect(
        host="localhost",
        user="root",
        password=PASSWORD,
        database="testdb"
        )  

        my_cur = database.cursor()
        querie = """SELECT * FROM testdb.membersinfo WHERE Mobile_Number = %s """
        my_cur.execute(querie, member) 
        record = my_cur.fetchall()


        # print(record)

        for row in record:

            item_row = []
            for i, value in enumerate(row):
    
                item = QStandardItem()
                item.setText(str(value))
                item_row.append(item)
            self.model.appendRow(item_row)

        database.commit()
        database.close()

         ##################### Searching for Member Info Using Using the Member Po Box  ############################################

        database = pymysql.connect(
        host="localhost",
        user="root",
        password=PASSWORD,
        database="testdb"
        )  

        my_cur = database.cursor()
        querie = """SELECT * FROM testdb.membersinfo WHERE PO_Box = %s """
        my_cur.execute(querie, member) 
        record = my_cur.fetchall()


        # print(record)

        for row in record:

            item_row = []
            for i, value in enumerate(row):
    
                item = QStandardItem()
                item.setText(str(value))
                item_row.append(item)
            self.model.appendRow(item_row)

        database.commit()
        database.close()

         ##################### Searching for Member Info Using Using the Member Membership Type  ############################################

        database = pymysql.connect(
        host="localhost",
        user="root",
        password=PASSWORD,
        database="testdb"
        )  

        my_cur = database.cursor()
        querie = """SELECT * FROM testdb.membersinfo WHERE Membership_Type = %s """
        my_cur.execute(querie, member) 
        record = my_cur.fetchall()


        # print(record)

        for row in record:

            item_row = []
            for i, value in enumerate(row):
    
                item = QStandardItem()
                item.setText(str(value))
                item_row.append(item)
            self.model.appendRow(item_row)

        database.commit()
        database.close()

         ##################### Searching for Member Info Using Using the Column ID ############################################

        database = pymysql.connect(
        host="localhost",
        user="root",
        password=PASSWORD,
        database="testdb"
        )  

        my_cur = database.cursor()
        querie = """SELECT * FROM testdb.membersinfo WHERE ID = %s """
        my_cur.execute(querie, member) 
        record = my_cur.fetchall()


        # print(record)

        for row in record:

            item_row = []
            for i, value in enumerate(row):
    
                item = QStandardItem()
                item.setText(str(value))
                item_row.append(item)
            self.model.appendRow(item_row)

        database.commit()
        database.close()






        
        

        # database = pymysql.connect(
        # host="localhost",
        # user="root",
        # password="divineosuuweb@123",
        # database="testdb"
        # )

        # my_cur = database.cursor()
        
    def update_line_edit(self):
        print("Worked")
        

        # Connect to the database
        connection = pymysql.connect(host='localhost', user='root', password='divineosuuweb@123', database='testdb')

        # Create a QTreeView
        tree_view = QTreeView()

        # Create a QStandardItemModel
        model = QStandardItemModel()

        # Set the model on the QTreeView
        tree_view.setModel(model)

        # Create QLineEdit widgets for each item
        line_edits = [QLineEdit() for _ in range(11)]

        # Create a QVBoxLayout and QWidget to display the widgets
        layout = QVBoxLayout()
        layout.addWidget(tree_view)
        for line_edit in line_edits:
            layout.addWidget(line_edit)
        widget = QWidget()
        widget.setLayout(layout)
        widget.show()

        # Function to update the LineEdits with the clicked item's data
        def update_line_edits(index):
            row = index.row()
            for i in range(11):
                data = model.index(row, i).data(Qt.DisplayRole)
                line_edits[i].setText(data)

        # Connect the clicked signal of the QTreeView to the update_line_edits function
        tree_view.clicked.connect(update_line_edits)

        # Retrieve data from the database
        with connection.cursor() as cursor:
            # Execute the SQL query to fetch the data
            query = "SELECT Member_Id, FirstName, LastName, Gender, Address, Email, Mobile_Number, PO_Box, Membership_Type, ID  FROM testdb.membersinfo"
            cursor.execute(query)
            result = cursor.fetchall()

            # Populate the QStandardItemModel with the retrieved data
            for row in result:
                items = [QStandardItem(str(value)) for value in row]
                model.appendRow(items)




if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = App()

    window.show()
    app.exec()





