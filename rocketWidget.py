from PySide6.QtWidgets import QPushButton, QWidget, QVBoxLayout, QHBoxLayout



class ButtonLayout(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button Widget")
    

        button1= QPushButton("Button1")
        button2= QPushButton("Button2")

        button_layout = QVBoxLayout()
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)

        self.setLayout(button_layout)
    

        def button1_clicked(self):
            
            print("You clicked Button1")
        
        def button2_clicked(self):
            print("You clicked Button2")


        button1.clicked.connect(button1_clicked)
        button2.clicked.connect(button2_clicked)    

    
       