
from PySide6.QtWidgets import QMainWindow, QMessageBox, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent,*args,**kwargs)
        
        #configs
        self.central_widget = QWidget()
        self.vLayout = QVBoxLayout()
        self.central_widget.setLayout(self.vLayout)    
        self.setCentralWidget(self.central_widget)
        
        #title
        self.setWindowTitle('Calculator')
        
        
        
    def adjustFixedSize(self):
        #the last thing to do
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
        
    def addTooVLayout(self,widget: QWidget):
        self.vLayout.addWidget(widget)
        
    def makeMsgBox(self):
        return QMessageBox(self)