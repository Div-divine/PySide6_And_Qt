from PySide6.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QPushButton, QToolBar, QTextEdit, QInputDialog, QTabWidget, QFileDialog



current_path = ""

class App(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.count = 0

       
        self.TabWidget = QTabWidget(self)
        self.setCentralWidget(self.TabWidget)

        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)
        
        

        self.addButton = QPushButton("New")
        self.addButton.clicked.connect(self.new_Tab)
        self.toolBar = QToolBar()
        self.toolBar.addWidget(self.addButton)

        self.addToolBar(self.toolBar)
        

        


        self.file = QMenu("File")
        self.Open = self.file.addAction("Open")
        self.Save_as = self.file.addAction("Save As")
        self.Save = self.file.addAction("Save")
        self.New = self.file.addAction("New")
        self.Exit = self.file.addAction("Exit")

        self.edit = QMenu("Edit")
        self.Find = self.edit.addAction("Find")

        self.view = QMenu("View")
        self.ZoomOut = self.view.addAction("Zoom Out")
        self.ZoomIn = self.view.addAction("Zoom In")
        self.Default = self.view.addAction("Default Size")


        self.advanced = QMenu("Advanced")
        self.Auto_Save = self.advanced.addAction("Auto Save")

        self.TextEdit = QTextEdit()


        


        self.menuBar.addMenu(self.file)
        self.menuBar.addMenu(self.edit)
        self.menuBar.addMenu(self.view)
        self.menuBar.addMenu(self.advanced)


        self.New.triggered.connect(self.new_Tab)
        self.Open.triggered.connect(self.open_file)
        self.Save_as.triggered.connect(self.save_file_as)
        self.Save.triggered.connect(self.save_file)

    

        # self.menuBar.addAction("File")
        # self.menuBar.addAction("View")
        # self.addToolBar(self.toolBar)

        self.new_Tab

    def new_Tab(self):
        global current_path
        # self.TextEdit = QTextEdit()

        title, ok = QInputDialog.getText(self, "New Tab", "Tab Name:")    
        if title and ok:
            text_index = self.TabWidget.addTab(self.TextEdit, title)
            self.TabWidget.setCurrentIndex(text_index)

            self.TextEdit.clear()
            current_path = ""   
   


    # def open_Folder(self):
    #     # self.count +=1
    #     # print(self.count)
    #     global current_path

    #     self.TextEdit = QTextEdit()

    #     file = QFileDialog(self)
    #     file_path,_= file.getOpenFileName()
    #     if file_path:
    #         with open(file_path, "r") as F:
    #             self.TextEdit.setText(F.read())

    #         current_path = file_path 
   
        # if file_path:
        #     text_index = self.TabWidget.addTab(self.TextEdit, file_path)
        #     self.TabWidget.setCurrentIndex(text_index) 
        
        # current_path = file_path


    # def save_file_As(self):
    #     global current_path

    #     self.TextEdit = QTextEdit()

    #     file = QFileDialog(self)
    #     file_path,_ = file.getOpenFileName()
    #     if file_path:
    #         with open(file_path, "w") as w:
    #             w.write(self.TextEdit.toPlainText())

    #         current_path = file_path 


    # def save_File(self):
    #     global current_path
    #     self.TextEdit = QTextEdit()
    #     if current_path:
    #         with open(current_path, "w") as w:
    #             w.write(self.TextEdit.toPlainText())  

    #     else:
    #         self.save_file_As()              



    def open_file(self):
        global current_path
        file_dialog = QFileDialog(window)
        file_path, _ = file_dialog.getOpenFileName()
        if file_path:
            with open(file_path, "r") as file:
                self.TextEdit.setText(file.read())
            current_path = file_path

        if file_path:
            text_index = self.TabWidget.addTab(self.TextEdit, file_path)
            self.TabWidget.setCurrentIndex(text_index) 
        
        current_path = file_path 


         
   



    def save_file_as(self):
        global current_path
        file_dialog = QFileDialog(window)
        file_path, _ = file_dialog.getSaveFileName()
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.TextEdit.toPlainText())

        current_path = file_path


        if file_path:
            text_index = self.TabWidget.addTab(self.TextEdit, file_path)
            self.TabWidget.setCurrentIndex(text_index)  



    def save_file(self):
        global current_path
        if current_path:
            with open(current_path, "w") as file:
                file.write(self.TextEdit.toPlainText())


        if current_path:
            text_index = self.TabWidget.addTab(self.TextEdit, current_path)
            self.TabWidget.setCurrentIndex(text_index) 

        else:

            self.save_file_as()

        










if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = App()
    window.setGeometry(100, 100, 800, 600)

    window.show()
    app.exec()
