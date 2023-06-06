from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, QTabWidget, QWidget, QCheckBox, QTextEdit, QInputDialog
from PySide6.QtUiTools import loadUiType


Ui_MainWindow, QMainWindow = loadUiType('Text_Edit.ui')


current_path = ""

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        # self.button = self.findChild(QPushButton, 'pushButton')
        # self.label = self.findChild(QLabel, 'label')
        self.Text_edit1 = self.findChild(QTextEdit, 'tab1_textEdit')
        self.Text_edit2 = self.findChild(QTextEdit, 'tab2_textEdit_2')
        self.TabWidget = self.findChild(QTabWidget, 'tabWidget')
        self.Tab1 = self.findChild(QWidget, 'tab1')
        self.Tab2 = self.findChild(QWidget, 'tab2')
        self.Plus_button = self.findChild(QPushButton, 'pushButton')
        self.CheckBox = self.findChild(QCheckBox, 'checkBox')


        self.TabWidget.removeTab(1)


        # self.Plus_button.clicked.connect(self.create_new_tab)

        

        # self.ui.actionOpen.triggered.connect(self.open_File)
        # self.ui.actionSave.triggered.connect(self.save_File)
        # self.ui.actionSava_As.triggered.connect(self.save_As)
        # self.ui.actionNew.triggered.connect(self.new_File)
        self.CheckBox.setCheckable(True)
        self.CheckBox.toggled.connect(self.checking)
        self.ui.actionExit.triggered.connect(self.exit_File)

        self.ui.actionNew.triggered.connect(self.new_file)  
        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionSave.triggered.connect(self.save_file)
        self.ui.actionSava_As.triggered.connect(self.save_file_as)
        

        self.ui.actionZoom_Out.triggered.connect(self.ZoomOut)
        self.ui.actionZoom_In.triggered.connect(self.ZoomIn)
        self.ui.actionDefault_Size.triggered.connect(self.default_Size)

        # self.ui.actionAuto_Save.triggered.connect()

    # def exit_File(self):

    #     window.close()    

        

        
    # def new_file(self):
    #     global current_path

    #     self.Text_edit1.setText("")
    #     current_path = ""
        

    # def open_file(self):
    #     global current_path
    #     file = QFileDialog(window)
    #     file_path, _ = file.getOpenFileName(self,"My File")

    #     if file_path:
    #         with open(file_path, "r") as F:
    #             self.Text_edit1.setText(F.read())

    #         current_path = file_path 


    # def save_file_as(self):
    #     global current_path
    #     File = QFileDialog(window)
    #     file_path, _ = File.getOpenFileName()

    #     if file_path:
    #         with open(file_path, 'w') as W:
    #             W.write(self.Text_edit1.toPlainText())  

    #     current_path = file_path


    # def save_file(self):    
    #     global current_path
    #     if current_path:
    #         with open(current_path, "w") as WS:
    #             WS.write(self.Text_edit1.toPlainText())

    #     else:
    #         self.save_file_as()                       

        self.Text_edit1.setStyleSheet('''
        font-size : 15px;
        ''') 

        # self.create_new_tab()


    # def create_new_tab(self):

    #     title, ok = QInputDialog.getText(self, "Enter Title", "Tab Title:")
    #     if ok and title:
    #         tab_index = self.TabWidget.addTab(self.Text_edit1, title)
    #         self.TabWidget.setCurrentIndex(tab_index) 


        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)
        self.tab_widget.setTabsClosable(True)

        self.new_button = QPushButton("New")
        self.new_button.clicked.connect(self.create_new_tab)

        self.toolbar = self.addToolBar("Toolbar")
        self.toolbar.addWidget(self.new_button)

        # self.create_new_tab()

        self.text_edit = QTextEdit()

    def create_new_tab(self):

        title, ok = QInputDialog.getText(self, "Enter Title", "Tab Title:")
        if ok and title:
            tab_index = self.tab_widget.addTab(self.text_edit, title)
            self.tab_widget.setCurrentIndex(tab_index)

               

    def default_Size(self):
        self.text_edit.setStyleSheet('''
        font-size : 15px;
        ''')     

    def ZoomIn(self):
        self.text_edit.setStyleSheet('''
        font-size : 8px;
        ''')

    def ZoomOut(self):
        self.text_edit.setStyleSheet('''
        font-size : 22px;
        ''')       

    def checking(self):
        if self.CheckBox.isChecked():

            self.text_edit.setStyleSheet('''
            background-color : black;
            color : white;
            font-size : 15px;
            ''')

            
            
        else:
            self.text_edit.setStyleSheet('''
            background-color : white;
            color : black;
            font-size: 15px;
            ''')
       




    def exit_File(self):
            
        window.close()   


    def open_folder(self):
            global current_path
            file_dialog = QFileDialog(self)
            file_path, _ = file_dialog.getOpenFileName()

            if file_path:
                with open(file_path, "r", encoding='utf-8') as file:
                    self.text_edit.setText(file.read())

                current_path = file_path   



    # def autoSave_File(self):
        # global current_file_path
        # file_dialog = QFileDialog(self)
        # file_path, _ = file_dialog.getOpenFileName()
        # text = self.text_edit.toPlainText() 

        # with open(file_path, 'w'):
        #     text.write(text)  

    
        
        

       
                   


                      



    def new_file(self):
            global current_path
            self.text_edit.clear()
            current_path = ""


    # def open_file(self):
    #         global current_file_path
    #         file_path = QFileDialog.getOpenFileName(self, "My file", "", "All Files (*)")
        #    def save_file(self):
        # global current_file_path
        # if current_file_path:
        #     with open(current_file_path, "w") as file:
        #         file.write(self.text_edit.toPlainText())
        # else:
        #     save_file_as()


    def open_file(self):
        global current_path
        file_dialog = QFileDialog(window)
        file_path, _ = file_dialog.getOpenFileName()
        if file_path:
            with open(file_path, "r") as file:
                self.text_edit.setText(file.read())
            current_path = file_path
   



    def save_file_as(self):
        global current_path
        file_dialog = QFileDialog(window)
        file_path, _ = file_dialog.getSaveFileName()
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_edit.toPlainText())

        current_path = file_path



    def save_file(self):
        global current_path
        if current_path:
            with open(current_path, "w") as file:
                file.write(self.text_edit.toPlainText())
        else:

            self.save_file_as()


        
    
       
    


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = App()

    window.show()
    
    app.exec()        