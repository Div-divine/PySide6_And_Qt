from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QTextEdit, QPushButton, QMenuBar, QMenu, QStatusBar, QFileDialog, QCheckBox, QMdiArea
from PySide6.QtUiTools import loadUiType
from PySide6.QtCore import QTimer
from PySide6.QtGui import QKeySequence
Ui_MainWindow, QMainWindow = loadUiType('textEditor.ui')

current_file_path = ""

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.text_edit = self.findChild(QTextEdit, 'textEdit')

        self.file = self.findChild(QMenu, 'menuFile') 
        self.edit = self.findChild(QMenu, 'menuEdit')
        self.view = self.findChild(QMenu, 'menuView') 

        self.open = self.findChild(QPushButton, 'open_button')
        self.exit = self.findChild(QPushButton, 'exit_button')
        self.save = self.findChild(QPushButton, 'save_button')
        self.newFile = self.findChild(QPushButton, 'newfile_button')
        


        self.black_Editor = self.findChild(QPushButton, 'black_pushButton')
        self.white_Editor = self.findChild(QPushButton, 'white_pushButton')
        self.checkBox = self.findChild(QCheckBox, 'checkBox')
        


        self.ui.actionNew.triggered.connect(self.new_file)  
        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionSave.triggered.connect(self.save_file)
        self.ui.actionSave_As.triggered.connect(self.save_file_as)

        self.ui.actionZoom_in.triggered.connect(self.ZoomIn)
        self.ui.actionZoom_out.triggered.connect(self.ZoomOut)
        self.ui.actionExit.triggered.connect(self.exit_editor)

       

        # self.ui.actionZoom_in.triggered.connect(QKeySequence.zoomIn)
        # self.ui.actionAuto_Save.triggered.connect(self.autoSave)




        # self.statusBar = self.findChild(QStatusBar, 'statusbar')
        # self.statusBar.setStyleSheet('''
        #     background-color : black;
        #     color : white
            
        #     ''')
        
        # button = QPushButton("THIS IS A STATUS BAR")
        # self.statusBar.addWidget(button)

        self.open.clicked.connect(self.open_folder)
        self.exit.clicked.connect(self.exit_editor)
        self.save.clicked.connect(self.save_file)
        self.newFile.clicked.connect(self.new_file)


        self.checkBox.toggled.connect(self.checking)
        self.checkBox.setCheckable(True)

        self.text_edit.setStyleSheet('''
        font-size : 15px;
        ''')

        # self.show_text()



    def ZoomIn(self):
        self.text_edit.setStyleSheet('''
        font-size : 8px;
        ''')

    def ZoomOut(self):
        self.text_edit.setStyleSheet('''
        font-size : 22px;
        ''')       

    def checking(self):
        if self.checkBox.isChecked():

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

            
            


    #     self.timer = QTimer()
    #     self.timer.timeout.connect(lambda : self.autoSave(""))  
    #     self.timer.start(5000) 

    # def autoSave(self, data):
    #     self.text_edit.setText(f'{data}')     
    

    def exit_editor(self):
            
        window.close()   


    def open_folder(self):
            global current_file_path
            file_dialog = QFileDialog(self)
            file_path, _ = file_dialog.getOpenFileName()

            if file_path:
                with open(file_path, "r", encoding='utf-8') as file:
                    self.text_edit.setText(file.read())

                current_file_path = file_path   



    # def autoSave_File(self):
        # global current_file_path
        # file_dialog = QFileDialog(self)
        # file_path, _ = file_dialog.getOpenFileName()
        # text = self.text_edit.toPlainText() 

        # with open(file_path, 'w'):
        #     text.write(text)  

    
        
        

       
                   


                      



    def new_file(self):
            global current_file_path
            self.text_edit.clear()
            current_file_path = ""


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
        global current_file_path
        file_dialog = QFileDialog(window)
        file_path, _ = file_dialog.getOpenFileName()
        if file_path:
            with open(file_path, "r") as file:
                self.text_edit.setText(file.read())
            current_file_path = file_path
   



    def save_file_as(self):
        global current_file_path
        file_dialog = QFileDialog(window)
        file_path, _ = file_dialog.getSaveFileName()
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_edit.toPlainText())

        current_file_path = file_path



    def save_file(self):
        global current_file_path
        if current_file_path:
            with open(current_file_path, "w") as file:
                file.write(self.text_edit.toPlainText())
        else:

            self.save_file_as()


        
    
       
    


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = App()

    window.show()
    app.exec()        