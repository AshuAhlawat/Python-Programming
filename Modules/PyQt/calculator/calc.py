from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(223, 304)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setFixedHeight=304
        self.centralwidget.setFixedWidth=223
        self.centralwidget.setStyleSheet("background-color:black;")
        
        self.display = QtWidgets.QLabel(self.centralwidget)
        self.display.setGeometry(QtCore.QRect(0, 0, 551, 51))
        self.display.setObjectName("display")
        self.display.setStyleSheet("background-color:black;color:white;border:1px solid white;")
    
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(0, 60, 101, 28))
        self.clear.setObjectName("clear")
        self.clear.setShortcut("Esc")
        self.clear.setStyleSheet("background-color:red;color:white;border:1px solid white;")
        self.clear.clicked.connect(self.actionClear)
        
        self.delete_2 = QtWidgets.QPushButton(self.centralwidget)
        self.delete_2.setGeometry(QtCore.QRect(100, 60, 121, 28))
        self.delete_2.setObjectName("delete_2")
        self.delete_2.setShortcut("Backspace")
        self.delete_2.setStyleSheet("background-color:orange;color:white;border:1px solid white;")
        self.delete_2.clicked.connect(self.actionDel)
        
        self.Plus = QtWidgets.QPushButton(self.centralwidget)
        self.Plus.setGeometry(QtCore.QRect(180, 90, 41, 31))
        self.Plus.setObjectName("Plus")
        self.Plus.setShortcut("+")
        self.Plus.setStyleSheet("background-color:black;color:white;border:1px solid white;")
        self.Plus.clicked.connect(self.actionPlus)
        
        self.equal = QtWidgets.QPushButton(self.centralwidget)
        self.equal.setGeometry(QtCore.QRect(0, 250, 221, 28))
        self.equal.setObjectName("equal")
        self.equal.setShortcut("Enter")
        self.equal.setStyleSheet("background-color:green;color:white;border:1px solid white;")
        self.equal.clicked.connect(self.actionEqual)
        
        self.Minus = QtWidgets.QPushButton(self.centralwidget)
        self.Minus.setGeometry(QtCore.QRect(180, 130, 41, 28))
        self.Minus.setObjectName("Minus")
        self.Minus.setShortcut("-")
        self.Minus.setStyleSheet("background-color:black;color:white;border:1px solid white;")
        self.Minus.clicked.connect(self.actionMinus)
        
        self.Multi = QtWidgets.QPushButton(self.centralwidget)
        self.Multi.setGeometry(QtCore.QRect(180, 170, 41, 28))
        self.Multi.setObjectName("Multi")
        self.Multi.setShortcut("*")
        self.Multi.setStyleSheet("background-color:black;color:white;border:1px solid white;")
        self.Multi.clicked.connect(self.actionMulti)
        
        self.Divide = QtWidgets.QPushButton(self.centralwidget)
        self.Divide.setGeometry(QtCore.QRect(182, 210, 41, 28))
        self.Divide.setObjectName("Divide")
        self.Divide.setShortcut("/")
        self.Divide.setStyleSheet("background-color:black;color:white;border:1px solid white;")
        self.Divide.clicked.connect(self.actionDivide)
        
        self.one = QtWidgets.QPushButton(self.centralwidget)
        self.one.setGeometry(QtCore.QRect(0, 90, 41, 28))
        self.one.setObjectName("one")
        self.one.setShortcut("1")
        self.one.setStyleSheet("background-color:black;color:white;border:1px solid white;")
        self.one.clicked.connect(self.action1)
        
        self.two = QtWidgets.QPushButton(self.centralwidget)
        self.two.setGeometry(QtCore.QRect(60, 90, 41, 28))
        self.two.setObjectName("two")
        self.two.setShortcut("2")
        self.two.setStyleSheet("background-color:black;color:white;border:1px solid white;")
        self.two.clicked.connect(self.action2)
        
        self.three = QtWidgets.QPushButton(self.centralwidget)
        self.three.setGeometry(QtCore.QRect(120, 90, 41, 28))
        self.three.setObjectName("three")
        self.three.setShortcut("3")
        self.three.setStyleSheet("background-color:black;color:white;border:1px solid white;")
        self.three.clicked.connect(self.action3)
        
        self.four = QtWidgets.QPushButton(self.centralwidget)
        self.four.setGeometry(QtCore.QRect(0, 130, 41, 28))
        self.four.setObjectName("four")
        self.four.setShortcut("4")
        self.four.setStyleSheet("background-color:black;color:white;border:1px solid white;")
        self.four.clicked.connect(self.action4)
        
        self.five = QtWidgets.QPushButton(self.centralwidget)
        self.five.setGeometry(QtCore.QRect(60, 130, 41, 28))
        self.five.setObjectName("five")
        self.five.setShortcut("5")
        self.five.setStyleSheet("background-color:black;color:white;border:1px solid white;")
        self.five.clicked.connect(self.action5)
        
        self.six = QtWidgets.QPushButton(self.centralwidget)
        self.six.setGeometry(QtCore.QRect(120, 130, 41, 28))
        self.six.setObjectName("six")
        self.six.setShortcut("6")
        self.six.setStyleSheet("background-color:black;color:white;border:1px solid white;")
        self.six.clicked.connect(self.action6)
        
        self.seven = QtWidgets.QPushButton(self.centralwidget)
        self.seven.setGeometry(QtCore.QRect(0, 170, 41, 28))
        self.seven.setObjectName("seven")
        self.seven.setShortcut("7")
        self.seven.setStyleSheet("background-color:black;color:white;border:1px solid white;")
        self.seven.clicked.connect(self.action7)
        
        self.eight = QtWidgets.QPushButton(self.centralwidget)
        self.eight.setGeometry(QtCore.QRect(60, 170, 41, 28))
        self.eight.setObjectName("eight")
        self.eight.setShortcut("8")
        self.eight.setStyleSheet("background-color:black;color:white;border:1px solid white;")
        self.eight.clicked.connect(self.action8)
        
        self.nine = QtWidgets.QPushButton(self.centralwidget)
        self.nine.setGeometry(QtCore.QRect(120, 170, 41, 28))
        self.nine.setObjectName("nine")
        self.nine.setShortcut("9")
        self.nine.setStyleSheet("background-color:black;color:white;border:1px solid white;")
        self.nine.clicked.connect(self.action9)
        
        self.zero = QtWidgets.QPushButton(self.centralwidget)
        self.zero.setGeometry(QtCore.QRect(60, 210, 41, 28))
        self.zero.setObjectName("zero")
        self.zero.setShortcut("0")
        self.zero.setStyleSheet("background-color:black;color:white;border:1px solid white;")
        self.zero.clicked.connect(self.actionZero)
        
        self.point = QtWidgets.QPushButton(self.centralwidget)
        self.point.setGeometry(QtCore.QRect(120, 210, 41, 28))
        self.point.setObjectName("point")
        self.point.setShortcut(".")
        self.point.setStyleSheet("background-color:black;color:white;border:1px solid white;")
        self.point.clicked.connect(self.actionPoint)
        
        self.dblzero = QtWidgets.QPushButton(self.centralwidget)
        self.dblzero.setGeometry(QtCore.QRect(0, 210, 41, 28))
        self.dblzero.setObjectName("dblzero")
        self.dblzero.setStyleSheet("background-color:black;color:white;border:1px solid white;")
        self.dblzero.clicked.connect(self.actionDblzero)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.setStyleSheet("background-color:black;")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Darkalc"))
        self.display.setText(_translate("MainWindow", ""))
        self.clear.setText(_translate("MainWindow", "AC"))
        self.delete_2.setText(_translate("MainWindow", "Del"))
        self.Plus.setText(_translate("MainWindow", "+"))
        self.equal.setText(_translate("MainWindow", "="))
        self.Minus.setText(_translate("MainWindow", "-"))
        self.Multi.setText(_translate("MainWindow", "*"))
        self.Divide.setText(_translate("MainWindow", "/"))
        self.one.setText(_translate("MainWindow", "1"))
        self.two.setText(_translate("MainWindow", "2"))
        self.three.setText(_translate("MainWindow", "3"))
        self.four.setText(_translate("MainWindow", "4"))
        self.five.setText(_translate("MainWindow", "5"))
        self.six.setText(_translate("MainWindow", "6"))
        self.seven.setText(_translate("MainWindow", "7"))
        self.eight.setText(_translate("MainWindow", "8"))
        self.nine.setText(_translate("MainWindow", "9"))
        self.zero.setText(_translate("MainWindow", "0"))
        self.point.setText(_translate("MainWindow", "."))
        self.dblzero.setText(_translate("MainWindow", "00"))
    
    def actionEqual(self):
        eq = self.display.text()
        
        try:
            ans = eval(eq)
            self.display.setText(str(ans))
        except:
            self.display.setText("Input Incorrect")
    
    def actionClear(self):
        self.display.setText("")
    
    def actionDel(self):
        txt = self.display.text()
        self.display.setText(txt[:len(txt)-1])
    
    def actionPlus(self):
        txt = self.display.text()
        self.display.setText(txt+" + ")
        
    def actionMinus(self):
        txt = self.display.text()
        self.display.setText(txt+" - ")
    
    def actionMulti(self):
        txt = self.display.text()
        self.display.setText(txt+" * ")
    
    def actionDivide(self):
        txt = self.display.text()
        self.display.setText(txt+" / ")
    
    def action1(self):
        txt = self.display.text()
        self.display.setText(txt+"1")
    
    def action2(self):
        txt = self.display.text()
        self.display.setText(txt+"2")
    
    def action3(self):
        txt = self.display.text()
        self.display.setText(txt+"3")
    
    def action4(self):
        txt = self.display.text()
        self.display.setText(txt+"4")
    
    def action5(self):
        txt = self.display.text()
        self.display.setText(txt+"5")
    
    def action6(self):
        txt = self.display.text()
        self.display.setText(txt+"6")
    
    def action7(self):
        txt = self.display.text()
        self.display.setText(txt+"7")
    
    def action8(self):
        txt = self.display.text()
        self.display.setText(txt+"8")
    
    def action9(self):
        txt = self.display.text()
        self.display.setText(txt+"9")
        
    def actionZero(self):
        txt = self.display.text()
        self.display.setText(txt+"0")
    
    def actionDblzero(self):
        txt = self.display.text()
        self.display.setText(txt+"00")
    
    def actionPoint(self):
        txt = self.display.text()
        self.display.setText(txt+".")
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
