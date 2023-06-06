from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QSpinBox, QDoubleSpinBox, QTextEdit

import sys
from PySide6.QtCore import Qt

class MainWindow(QWidget):

    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First Window")
        

        layout = QVBoxLayout()
        label1 = QLabel("Fullname")
        label1.setStyleSheet('''
        color: black;
        font-size : 18px;
        '''
        )

        layout.addWidget(label1)

        line_edit1 = QLineEdit()
        line_edit1.setObjectName("fullname_field")
        line_edit1.setText("")
        layout.addWidget(line_edit1)



        button1 = QPushButton("Register")
        button1.setStyleSheet('''
               background-color: green;
               color : white;
        ''')
        layout.addWidget(button1)

        self.setLayout(layout)

        def button_clicked():
           label1.setText(f'Hello {line_edit1.text()}!')
           print("User Name is : ",line_edit1.text())

           line_edit1.setText("")

        
        button1.clicked.connect(button_clicked)

        label2 = QLabel("Pick something from the list")
        label2.setStyleSheet('''
        color: black;
        font-size: 18px;
        ''')


        layout.addWidget(label2)
        box_combo = QComboBox()
        box_combo.InsertPolicy.InsertAtBottom
        
        box_combo.addItem("Burger", 3)
        box_combo.addItem("Cheese", 6) 
        box_combo.addItem("Patatos", 5)
        box_combo.addItem("Rice", 2)
        box_combo.setEditable(True)
       

        layout.addWidget(box_combo)

        button2 = QPushButton("Add Item")
        button2.setStyleSheet('''
        background-color: blue;
        color : white;
        ''')

        layout.addWidget(button2)

        def second_button_clicked(self):
            label2.setText(f'You picked {box_combo.currentIndex()}{box_combo.currentText()}')
            print("User picked", box_combo.currentIndex(), box_combo.currentText())
            

        button2.clicked.connect(second_button_clicked)

        # button3 = QPushButton("Save Item")
        # button3.setStyleSheet('''
        # color: black;
        # background-color : yellow
        # ''')
        # layout.addWidget(button3)

        # def save_box(self,list_box):
        #     for l in box_combo:
        #         list_box = self.list_box.append(box_combo)
        #         print("The list_box is" , self.list_box )
            

        # button3.clicked.connect(save_box)
        label3 = QLabel("Place your order")
        label3.setStyleSheet('''
        color : black;
        font-size : 18px;
        ''')
        layout.addWidget(label3)
        
        spin_box = QSpinBox()
        spin_box.setValue(10)
        spin_box.setMaximum(20)
        spin_box.setMinimum(6)
        spin_box.setSingleStep(2)
        spin_box.setPrefix('How many order would you like to make?        ')
        layout.addWidget(spin_box)
        double_spin = QDoubleSpinBox()
        double_spin.setValue(10)
        double_spin.setSuffix('    Orders')
        layout.addWidget(double_spin)

        button3 = QPushButton("Save Item")
        button3.setStyleSheet('''
        color: black;
        background-color : yellow;
        ''')
        layout.addWidget(button3)
        
        def button3_save(self):
            label3.setText(f"You've made {spin_box.value()} Orders !")

        button3.clicked.connect(button3_save) 
        
        # label4 = QLabel("Input Text")
        # label4.setStyleSheet('''
        # font-size : 18px
        # ''')
        # layout.addWidget(label4)
        
        text_box = QTextEdit()
        text_box.acceptRichText()
        # text_box.setHtml("<h1> <em>Hello There</em></h1>")
        text_box.setLineWrapColumnOrWidth(50)

        text_box.setStyleSheet('''
        font-size : 12px;

        ''')
        text_box.setPlaceholderText('Type in your Text')

        layout.addWidget(text_box)


        
        

app = QApplication(sys.argv) 
widget = MainWindow()

widget.show()
app.exec()

