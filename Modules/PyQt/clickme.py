from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class myWindow(QMainWindow):
    def __init__(self):
        super(myWindow, self).__init__()
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("Click Me!")
        self.initUI()
        self.inc = 0

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("0")
        self.label.move(150, 150)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click Me!!!")
        self.b1.clicked.connect(self.clicked)
        self.b1.move(100, 100)

    def clicked(self):
        self.inc = self.inc+1
        self.label.setText(str(self.inc))


def window():
    app = QApplication(sys.argv)
    win = myWindow()
    win.show()
    sys.exit(app.exec_())


window()
