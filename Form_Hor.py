from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QFormLayout, QLabel, QLineEdit, QMessageBox
import sys



class Logging_Form(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("This is a User Logging Form")

        

        layout = QFormLayout()

        label = QLabel("Logging Form")
        label.setStyleSheet('''
        font-size : 10px;
        ''')
        layout.addRow(label)

        First = QLineEdit()
        First.setText("")
        First.setStyleSheet('''
        font-size : 10px
        ''')
        layout.addRow('First Name', First)


        last = QLineEdit()
        last.setStyleSheet('''
        font-size : 10px
        ''')
        layout.addRow('Last Name', last)

        email = QLineEdit()
        email.setStyleSheet('''
        font-size : 10px
        ''')
        layout.addRow('Email', email)

        self.button = QPushButton("Loggin")
        self.button.setStyleSheet('''
        color: white;
        background-color: green;
        font-size : 12px;
        ''')

        layout.addWidget(self.button)

        def button_clicked(self):
            label.setText(f'You are welcom {First.text()}')


        self.button.clicked.connect(button_clicked) 

        self.msg_button = QPushButton("Message")
        self.msg_button.setStyleSheet('''
        color: white;
        background-color: red;
        font-size : 12px;
        ''')

        layout.addWidget(self.msg_button)
        # message = QMessageBox()
        # message.setText("Are you happy with the Form ?")
        # message.setInformativeText("This form is still goinb through production!")
        # message.setStandardButtons(QMessageBox.Save | QMessageBox.Discard)
        # layout.addRow(message)
        
        self.setLayout(layout)

          

        def button_clicked_msg(self): 
            message = QMessageBox()
            message.setInformativeText("Hope you like the app ?")
            message.setText("Hello!")
            message.setIcon(QMessageBox.Critical)
            message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            


            layout.addWidget(message)    
   
    
    
        self.msg_button.clicked.connect(button_clicked_msg)  
    

    




    
        



app = QApplication(sys.argv)
widget = Logging_Form()

widget.show()
app.exec()