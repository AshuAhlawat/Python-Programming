from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class myWindow(QMainWindow):
    def __init__(self):
        super(myWindow, self).__init__()
        self.setGeometry(300,300,300,300)
        self.setWindowTitle("Lets Switch to Linux")
        self.initUI()
        
    def initUI(self):
        self.label=QtWidgets.QLabel(self)
        self.label.setText("Click it and switch it!")
        self.label.move(50,50)
        self.update()
    
        self.b1=QtWidgets.QPushButton(self)
        self.b1.setText("Click me!")
        self.b1.clicked.connect(self.clicked)
    
    def clicked(self):
        self.label.setText("Wallah! you are a step ahead")
        self.update()
    def update(self):
        self.label.adjustSize()
                       


def window():
    app=QApplication(sys.argv)
    win=myWindow()
   
    win.show()
    sys.exit(app.exec_())
    
window()