from PySide6.QtWidgets import QApplication, QMainWindow, QTreeView, QVBoxLayout, QWidget, QLineEdit, QPushButton
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.tree_view = QTreeView(self)
        self.line_edit1 = QLineEdit(self)
        self.line_edit2 = QLineEdit(self)
        self.line_edit3 = QLineEdit(self)
        self.button = QPushButton("Get Selected Items", self)
        self.button.clicked.connect(self.get_selected_items)
        
        layout = QVBoxLayout()
        layout.addWidget(self.tree_view)
        layout.addWidget(self.line_edit1)
        layout.addWidget(self.line_edit2)
        layout.addWidget(self.line_edit3)
        layout.addWidget(self.button)
        
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
        # Assuming you have set up your QTreeView and populated it with data
        
    def get_selected_items(self):
        selected_indexes = self.tree_view.selectedIndexes()
        if selected_indexes:
            item_data = [index.data(Qt.DisplayRole) for index in selected_indexes]
            if len(item_data) >= 3:
                self.line_edit1.setText(str(item_data[0]))
                self.line_edit2.setText(str(item_data[1]))
                self.line_edit3.setText(str(item_data[2]))

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
