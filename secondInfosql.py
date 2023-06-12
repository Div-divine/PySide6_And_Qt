from PySide6.QtWidgets import  QApplication, QVBoxLayout,QMainWindow, QPushButton, QLineEdit, QTreeView, QComboBox, QWidget, QMessageBox, QHeaderView
from PySide6.QtUiTools import loadUiType
from PySide6.QtGui import QStandardItem, QStandardItemModel
import pymysql
from pymysql.cursors import DictCursor
from PySide6.QtCore import QAbstractItemModel, QModelIndex, Qt
from important_info import PASSWORD




# my_cur = database.cursor()

# my_cur.execute("""UPDATE testdb.membersinfo SET Member_Id = 76890 AND FirstName= 'Sam' AND LastName= 'Trust'  WHERE ID = 2 """)

# database.commit()





Ui_MainWindow , QMainWindow = loadUiType('secondInfosql.ui')
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
        self.ID_line = self.findChild(QLineEdit, "memberId_line")
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
        header_label = ["Member ID", "Firstname", "Lastname", "Address", "Email", "PO_Box", "Gender", "Mobile_Number", "Membership Type" ,  "ID"]
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
        self.Update_button.clicked.connect(self.update)


        self.Save_update = self.findChild(QPushButton, "save_button")
        self.Save_update.clicked.connect(self.save_update)

        self.Num_list = self.findChild(QPushButton, "number_button")
        self.Num_line = self.findChild(QPushButton, "number_line")


        self.deleteButton = self.findChild(QPushButton, "delete_button")
        self.deleteButton.clicked.connect(self.delete_column_items)

        



        self.line_edit = [self.ID_line, self.FirstName_line, self.Surname_line, self.Gender_combo, self.Address_line, self.Email_line,
                     self.Mobile_line, self.PoBox_line, self.Type_Combo, self.Num_line
                     ]
        
        

   

        # Start the event loop
        # sys.exit(app.exec())


    # def reset_id_sequence(self):
    #     database = pymysql.connect(
    #         host="localhost",
    #         user="root",
    #         password="divineosuuweb@123",
    #         database="testdb"
    #     )
    
    #     cursor = database.cursor()
    
    #     # Execute an SQL query to reset the auto-increment sequence of the ID column
    #     sql = "ALTER TABLE testdb.membersinfo AUTO_INCREMENT= 1"
    #     cursor.execute(sql)
    
    #     database.commit()
    #     database.close()    
        

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


        msg = QMessageBox()
        msg.setWindowTitle("Saved")
        msg.setText("Your Information has been saved succesfully!")
        msg.setIcon(QMessageBox.Information)

        msg_exec = msg.exec()

        # self.reset_id_sequence()
        self.showRecord()

        
     

        
        

        
        



    def showRecord(self):

        self.model.clear()

        self.model = QStandardItemModel()
        header_label = ["Member ID", "Firstname", "Lastname", "Address", "Email", "PO_Box", "Gender", "Mobile_Number", "Membership Type" ,  "ID"]
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

                


        
    def update(self):
        selection_model = self.Treeview.selectionModel()
        selected_indexes = selection_model.selectedIndexes()
        if selected_indexes:
            item_data = [index.data(Qt.DisplayRole) for index in selected_indexes]
            if len(item_data) >= 10:
                self.ID_line.setText(str(item_data[0]))
                self.FirstName_line.setText(str(item_data[1]))
                self.Surname_line.setText(str(item_data[2]))
                self.Address_line.setText(str(item_data[3]))
                self.Email_line.setText(str(item_data[4]))
                self.PoBox_line.setText(str(item_data[5]))
                self.Gender_combo.setCurrentText(str(item_data[6]))
                self.Mobile_line.setText(str(item_data[7]))
                self.Type_Combo.setCurrentText(str(item_data[8]))
                self.Num_line.setText(str(item_data[9]))




                

        

        

         


    def Exit_func(self) :

        window.close()


    def search(self):

        self.model.clear()

        self.model = QStandardItemModel()
        header_label = ["Member ID", "Firstname", "Lastname", "Address", "Email", "PO_Box", "Gender", "Mobile_Number", "Membership Type" ,  "ID"]
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

        # self.update()





        
        

        # database = pymysql.connect(
        # host="localhost",
        # user="root",
        # password="divineosuuweb@123",
        # database="testdb"
        # )

        # my_cur = database.cursor()
        
    def save_update(self):
        database = pymysql.connect(
        host="localhost",
        user="root",
        password=PASSWORD,
        database="testdb"
        )

        self.list = [
        int(self.ID_line.text()),
        self.FirstName_line.text(),
        self.Surname_line.text(),
        self.Address_line.text(),
        self.Email_line.text(),
        self.PoBox_line.text(),
        self.Gender_combo.currentText(),
        int(self.Mobile_line.text()),
        self.Type_Combo.currentText(),
        int(self.Num_line.text())
        ]

        with database.cursor() as cursor:
            sql = "UPDATE testdb.membersinfo SET Member_Id = %s, FirstName = %s, LastName = %s, Address = %s, Email = %s, " \
              "PO_Box = %s, Gender = %s, Mobile_Number = %s, Membership_Type = %s WHERE ID = %s"
            cursor.execute(sql, self.list)
            database.commit()

        msg = QMessageBox()
        msg.setWindowTitle("Saved")
        msg.setText("Your Information has been updated!")
        msg.setIcon(QMessageBox.Information)
        msg_exec = msg.exec()

        database.close()

        self.showRecord()




    def delete_column_items(self):
        selection_model = self.Treeview.selectionModel()
        column_index = selection_model.currentIndex().column()  # Get the selected column index

        # Iterate over the rows of the selected column in reverse order
        for row in range(self.Treeview.model().rowCount() - 1, -1, -1):
            index = self.Treeview.model().index(row, column_index)
            item_data = index.data()

            # Delete the corresponding item from the database using pymysql
            self.delete_from_database(item_data)

            # Remove the row from the TreeView model
            self.Treeview.model().removeRow(row, index.parent())


             # Delete the corresponding item from the database using pymysql
            item_data = index.data()

            self.showRecord()
            self.delete_from_database(item_data)



        

    def delete_from_database(self, item_data):

        # item_data = [
        # int(self.ID_line.text()),
        # self.FirstName_line.text(),
        # self.Surname_line.text(),
        # self.Address_line.text(),
        # self.Email_line.text(),
        # self.PoBox_line.text(),
        # self.Gender_combo.currentText(),
        # int(self.Mobile_line.text()),
        # self.Type_Combo.currentText(),
        # int(self.Num_line.text())
        # ]

        database = pymysql.connect(
        host="localhost",
        user="root",
        password=PASSWORD,
        database="testdb"
        )
         # Connect to the database
        cursor = database.cursor()

        # Write your SQL query to delete the item from the database
        sql = "DELETE FROM testdb.membersinfo  WHERE FirstName = %s"

        # Execute the query with the item_data
        cursor.execute(sql, (item_data))

    # Commit the changes and close the database connection
        database.commit()
        database.close()

        self.showRecord()

# Connect the deleteButton's clicked signal to the delete_column_items function/slot

    
   


        




if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = App()

    window.show()
    app.exec()





