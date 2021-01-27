from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(180, 0, 511, 451))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap(r"D:\Coding\Python Programming\Modules\PyQt\download1.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.prev = QtWidgets.QPushButton(self.centralwidget)
        self.prev.setGeometry(QtCore.QRect(80, 480, 131, 61))
        self.prev.setObjectName("prev")
        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(500, 480, 171, 61))
        self.next.setObjectName("next")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.prev.clicked.connect(self.show_prev)
        self.next.clicked.connect(self.show_next)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.prev.setText(_translate("MainWindow", "Prev"))
        self.next.setText(_translate("MainWindow", "Next"))

    def show_prev(self):
        self.photo.setPixmap(QtGui.QPixmap(r"D:\Coding\Python Programming\Modules\PyQt\download.png"))
    def show_next(self):
        self.photo.setPixmap(QtGui.QPixmap(r"D:\Coding\Python Programming\Modules\PyQt\download1.jpg"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())