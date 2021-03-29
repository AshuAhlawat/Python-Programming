from PyQt5 import QtCore, QtGui, QtWidgets
import math

class Ui_darkalcpro(object):
    def setupUi(self, darkalcpro):
        darkalcpro.setObjectName("darkalcpro")
        darkalcpro.resize(582, 475)
        darkalcpro.setMaximumSize(QtCore.QSize(582, 624))
        darkalcpro.setStyleSheet("background-color:black")
        self.centralwidget = QtWidgets.QWidget(darkalcpro)
        self.centralwidget.setObjectName("centralwidget")
        self.display = QtWidgets.QLineEdit(self.centralwidget)
        self.display.setGeometry(QtCore.QRect(0, 0, 581, 121))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Arabic")
        font.setPointSize(14)
        self.display.setFont(font)
        self.display.setStyleSheet("background-color:rgb(85,88,92) ;border: 3px solid white;color:white;")
        self.display.setObjectName("display")
        
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(350, 240, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.clear.setFont(font)
        self.clear.setAutoFillBackground(False)
        self.clear.setStyleSheet("background-color:rgb(57,58,59);color:rgb(230,234,240);border:2px solid white;")
        self.clear.setObjectName("clear")
        self.clear.clicked.connect(self.actionClear)
        
        self.delete_2 = QtWidgets.QPushButton(self.centralwidget)
        self.delete_2.setGeometry(QtCore.QRect(470, 240, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.delete_2.setFont(font)
        self.delete_2.setStyleSheet("background-color:rgb(57,58,59);color:rgb(230,234,240);border:2px solid white;")
        self.delete_2.setObjectName("delete_2")
        self.delete_2.clicked.connect(self.actionDel)
        
        self.dblzero = QtWidgets.QPushButton(self.centralwidget)
        self.dblzero.setGeometry(QtCore.QRect(0, 420, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.dblzero.setFont(font)
        self.dblzero.setStyleSheet("background-color:rgb(57,58,59);color:rgb(230,234,240);border:2px solid white;")
        self.dblzero.setObjectName("dblzero")
        self.dblzero.clicked.connect(self.actionDblzero)
        
        self.zero = QtWidgets.QPushButton(self.centralwidget)
        self.zero.setGeometry(QtCore.QRect(110, 420, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.zero.setFont(font)
        self.zero.setStyleSheet("background-color:rgb(57,58,59);color:rgb(230,234,240);border:2px solid white;")
        self.zero.setObjectName("zero")
        self.zero.clicked.connect(self.action0)
        
        self.point = QtWidgets.QPushButton(self.centralwidget)
        self.point.setGeometry(QtCore.QRect(220, 420, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.point.setFont(font)
        self.point.setStyleSheet("background-color:rgb(57,58,59);color:rgb(230,234,240);border:2px solid white;")
        self.point.setObjectName("point")
        self.point.clicked.connect(self.actionPoint)
    
        
        self.equal = QtWidgets.QPushButton(self.centralwidget)
        self.equal.setGeometry(QtCore.QRect(350, 420, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.equal.setFont(font)
        self.equal.setStyleSheet("background-color:rgb(57,58,59);color:rgb(230,234,240);border:2px solid white;")
        self.equal.setObjectName("equal")
        self.equal.clicked.connect(self.actionEqual)
        
        self.plus = QtWidgets.QPushButton(self.centralwidget)
        self.plus.setGeometry(QtCore.QRect(470, 420, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.plus.setFont(font)
        self.plus.setStyleSheet("background-color:rgb(57,58,59);color:rgb(230,234,240);border:2px solid white;")
        self.plus.setObjectName("plus")
        self.plus.clicked.connect(self.actionPlus)
        
        self.one = QtWidgets.QPushButton(self.centralwidget)
        self.one.setGeometry(QtCore.QRect(0, 360, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.one.setFont(font)
        self.one.setStyleSheet("background-color:rgb(57,58,59);color:rgb(230,234,240);border:2px solid white;")
        self.one.setObjectName("one")
        self.one.clicked.connect(self.action1)
        
        self.two = QtWidgets.QPushButton(self.centralwidget)
        self.two.setGeometry(QtCore.QRect(110, 360, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.two.setFont(font)
        self.two.setStyleSheet("background-color:rgb(57,58,59);color:rgb(230,234,240);border:2px solid white;")
        self.two.setObjectName("two")
        self.two.clicked.connect(self.action2)
        
        self.three = QtWidgets.QPushButton(self.centralwidget)
        self.three.setGeometry(QtCore.QRect(220, 360, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.three.setFont(font)
        self.three.setStyleSheet("background-color:rgb(57,58,59);color:rgb(230,234,240);border:2px solid white;")
        self.three.setObjectName("three")
        self.three.clicked.connect(self.action3)
        
        self.remainder = QtWidgets.QPushButton(self.centralwidget)
        self.remainder.setGeometry(QtCore.QRect(350, 360, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.remainder.setFont(font)
        self.remainder.setStyleSheet("background-color:rgb(57,58,59);color:rgb(230,234,240);border:2px solid white;")
        self.remainder.setObjectName("remainder")
        self.remainder.clicked.connect(self.actionRem)
        
        self.minus = QtWidgets.QPushButton(self.centralwidget)
        self.minus.setGeometry(QtCore.QRect(470, 360, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.minus.setFont(font)
        self.minus.setStyleSheet("background-color:rgb(57,58,59);color:rgb(230,234,240);border:2px solid white;")
        self.minus.setObjectName("minus")
        self.minus.clicked.connect(self.actionMinus)
        
        self.four = QtWidgets.QPushButton(self.centralwidget)
        self.four.setGeometry(QtCore.QRect(0, 300, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.four.setFont(font)
        self.four.setStyleSheet("background-color:rgb(57,58,59);color:rgb(230,234,240);border:2px solid white;")
        self.four.setObjectName("four")
        self.four.clicked.connect(self.action4)
        
        self.five = QtWidgets.QPushButton(self.centralwidget)
        self.five.setGeometry(QtCore.QRect(110, 300, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.five.setFont(font)
        self.five.setStyleSheet("background-color:rgb(57,58,59);color:rgb(230,234,240);border:2px solid white;")
        self.five.setObjectName("five")
        self.five.clicked.connect(self.action5)
        
        self.six = QtWidgets.QPushButton(self.centralwidget)
        self.six.setGeometry(QtCore.QRect(220, 300, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.six.setFont(font)
        self.six.setStyleSheet("background-color:rgb(57,58,59);color:rgb(230,234,240);border:2px solid white;")
        self.six.setObjectName("six")
        self.six.clicked.connect(self.action6)
        
        self.divide = QtWidgets.QPushButton(self.centralwidget)
        self.divide.setGeometry(QtCore.QRect(350, 300, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.divide.setFont(font)
        self.divide.setStyleSheet("background-color:rgb(57,58,59);color:rgb(230,234,240);border:2px solid white;")
        self.divide.setObjectName("divide")
        self.divide.clicked.connect(self.actionDivide)
        
        self.Multi = QtWidgets.QPushButton(self.centralwidget)
        self.Multi.setGeometry(QtCore.QRect(470, 300, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Multi.setFont(font)
        self.Multi.setStyleSheet("background-color:rgb(57,58,59);color:rgb(230,234,240);border:2px solid white;")
        self.Multi.setObjectName("Multi")
        self.Multi.clicked.connect(self.actionMulti)
        
        self.seven = QtWidgets.QPushButton(self.centralwidget)
        self.seven.setGeometry(QtCore.QRect(0, 240, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.seven.setFont(font)
        self.seven.setStyleSheet("background-color:rgb(57,58,59);color:rgb(230,234,240);border:2px solid white;")
        self.seven.setObjectName("seven")
        self.seven.clicked.connect(self.action7)
        
        self.eight = QtWidgets.QPushButton(self.centralwidget)
        self.eight.setGeometry(QtCore.QRect(110, 240, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.eight.setFont(font)
        self.eight.setStyleSheet("background-color:rgb(57,58,59);color:rgb(230,234,240);border:2px solid white;")
        self.eight.setObjectName("eight")
        self.eight.clicked.connect(self.action8)
        
        self.nine = QtWidgets.QPushButton(self.centralwidget)
        self.nine.setGeometry(QtCore.QRect(220, 240, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.nine.setFont(font)
        self.nine.setStyleSheet("background-color:rgb(57,58,59);color:rgb(230,234,240);border:2px solid white;")
        self.nine.setObjectName("nine")
        self.nine.clicked.connect(self.action9)
        
        self.brcOn = QtWidgets.QPushButton(self.centralwidget)
        self.brcOn.setGeometry(QtCore.QRect(0, 130, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.brcOn.setFont(font)
        self.brcOn.setStyleSheet("background-color:rgb(57,58,59);color:rgb(230,234,240);border:2px solid white;")
        self.brcOn.setObjectName("brcOn")
        self.brcOn.clicked.connect(self.actionBrcOn)
        
        self.brcOff = QtWidgets.QPushButton(self.centralwidget)
        self.brcOff.setGeometry(QtCore.QRect(120, 130, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.brcOff.setFont(font)
        self.brcOff.setStyleSheet("background-color:rgb(57,58,59);color:rgb(230,234,240);border:2px solid white;")
        self.brcOff.setObjectName("brcOff")
        self.brcOff.clicked.connect(self.actionBrcOff)
        
        self.pow = QtWidgets.QPushButton(self.centralwidget)
        self.pow.setGeometry(QtCore.QRect(240, 180, 91, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        self.pow.setFont(font)
        self.pow.setStyleSheet("background-color:rgb(57,58,59);color:rgb(230,234,240);border:2px solid white;")
        self.pow.setObjectName("pow")
        self.pow.clicked.connect(self.actionPow)
        
        self.exp = QtWidgets.QPushButton(self.centralwidget)
        self.exp.setGeometry(QtCore.QRect(240, 130, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.exp.setFont(font)
        self.exp.setStyleSheet("background-color:rgb(57,58,59);color:rgb(230,234,240);border:2px solid white;")
        self.exp.setObjectName("exp")
        self.exp.clicked.connect(self.actionExp)
        
        self.square = QtWidgets.QPushButton(self.centralwidget)
        self.square.setGeometry(QtCore.QRect(360, 130, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.square.setFont(font)
        self.square.setStyleSheet("background-color:rgb(57,58,59);color:rgb(230,234,240);border:2px solid white;")
        self.square.setObjectName("square")
        self.square.clicked.connect(self.actionSquare)
        
        self.logx = QtWidgets.QPushButton(self.centralwidget)
        self.logx.setGeometry(QtCore.QRect(480, 130, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.logx.setFont(font)
        self.logx.setStyleSheet("background-color:rgb(57,58,59);color:rgb(230,234,240);border:2px solid white;")
        self.logx.setObjectName("logx")
        self.logx.clicked.connect(self.actionLogx)
        
        self.perm = QtWidgets.QPushButton(self.centralwidget)
        self.perm.setGeometry(QtCore.QRect(0, 180, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.perm.setFont(font)
        self.perm.setStyleSheet("background-color:rgb(57,58,59);color:rgb(230,234,240);border:2px solid white;")
        self.perm.setObjectName("perm")
        self.perm.clicked.connect(self.actionPerm)
        
        self.comb = QtWidgets.QPushButton(self.centralwidget)
        self.comb.setGeometry(QtCore.QRect(120, 180, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.comb.setFont(font)
        self.comb.setStyleSheet("background-color:rgb(57,58,59);color:rgb(230,234,240);border:2px solid white;")
        self.comb.setObjectName("comb")
        self.comb.clicked.connect(self.actionComb)
        
        self.logb2 = QtWidgets.QPushButton(self.centralwidget)
        self.logb2.setGeometry(QtCore.QRect(360, 180, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.logb2.setFont(font)
        self.logb2.setStyleSheet("background-color:rgb(57,58,59);color:rgb(230,234,240);border:2px solid white;")
        self.logb2.setObjectName("logb2")
        self.logb2.clicked.connect(self.actionLog2)
        
        self.logb10 = QtWidgets.QPushButton(self.centralwidget)
        self.logb10.setGeometry(QtCore.QRect(480, 180, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.logb10.setFont(font)
        self.logb10.setStyleSheet("background-color:rgb(57,58,59);color:rgb(230,234,240);border:2px solid white;")
        self.logb10.setObjectName("logb10")
        self.logb10.clicked.connect(self.actionLog10)
        
        darkalcpro.setCentralWidget(self.centralwidget)
        self.retranslateUi(darkalcpro)
        QtCore.QMetaObject.connectSlotsByName(darkalcpro)

    def retranslateUi(self, darkalcpro):
        _translate = QtCore.QCoreApplication.translate
        darkalcpro.setWindowTitle(_translate("darkalcpro", "MainWindow"))
        self.display.setText(_translate("darkalcpro", ""))
        self.clear.setText(_translate("darkalcpro", "AC"))
        self.clear.setShortcut(_translate("darkalcpro", "Esc"))
        self.delete_2.setText(_translate("darkalcpro", "Del"))
        self.delete_2.setShortcut(_translate("darkalcpro", "Backspace"))
        self.dblzero.setText(_translate("darkalcpro", "00"))
        self.zero.setText(_translate("darkalcpro", "0"))
        self.zero.setShortcut(_translate("darkalcpro", "0"))
        self.point.setText(_translate("darkalcpro", "."))
        self.point.setShortcut(_translate("darkalcpro", "."))
        self.equal.setText(_translate("darkalcpro", "="))
        self.equal.setShortcut(_translate("darkalcpro", "="))
        self.plus.setText(_translate("darkalcpro", "+"))
        self.plus.setShortcut(_translate("darkalcpro", "+"))
        self.one.setText(_translate("darkalcpro", "1"))
        self.one.setShortcut(_translate("darkalcpro", "1"))
        self.two.setText(_translate("darkalcpro", "2"))
        self.two.setShortcut(_translate("darkalcpro", "2"))
        self.three.setText(_translate("darkalcpro", "3"))
        self.three.setShortcut(_translate("darkalcpro", "3"))
        self.remainder.setText(_translate("darkalcpro", "REM"))
        self.minus.setText(_translate("darkalcpro", "-"))
        self.minus.setShortcut(_translate("darkalcpro", "-"))
        self.four.setText(_translate("darkalcpro", "4"))
        self.five.setText(_translate("darkalcpro", "5"))
        self.five.setShortcut(_translate("darkalcpro", "5"))
        self.six.setText(_translate("darkalcpro", "6"))
        self.six.setShortcut(_translate("darkalcpro", "6"))
        self.divide.setText(_translate("darkalcpro", "/"))
        self.Multi.setText(_translate("darkalcpro", "*"))
        self.seven.setText(_translate("darkalcpro", "7"))
        self.seven.setShortcut(_translate("darkalcpro", "7"))
        self.eight.setText(_translate("darkalcpro", "8"))
        self.eight.setShortcut(_translate("darkalcpro", "8"))
        self.nine.setText(_translate("darkalcpro", "9"))
        self.nine.setShortcut(_translate("darkalcpro", "9"))
        self.brcOn.setText(_translate("darkalcpro", "("))
        self.brcOn.setShortcut(_translate("darkalcpro", "("))
        self.brcOff.setText(_translate("darkalcpro", ")"))
        self.brcOff.setShortcut(_translate("darkalcpro", ")"))
        self.pow.setText(_translate("darkalcpro", "X^N"))
        self.exp.setText(_translate("darkalcpro", "Exp"))
        self.square.setText(_translate("darkalcpro", "2^X"))
        self.logx.setText(_translate("darkalcpro", "lnx"))
        self.perm.setText(_translate("darkalcpro", "nPr"))
        self.comb.setText(_translate("darkalcpro", "nCr"))
        self.logb2.setText(_translate("darkalcpro", "log2"))
        self.logb10.setText(_translate("darkalcpro", "log10"))
    
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
        
    def action0(self):
        txt = self.display.text()
        self.display.setText(txt+"0")
    
    def actionDblzero(self):
        txt = self.display.text()
        self.display.setText(txt+"00")
    
    def actionPoint(self):
        txt = self.display.text()
        self.display.setText(txt+".")
        
    def actionEqual(self):
        eq = self.display.text()
        
        try:
            ans = eval(eq)
            self.display.setText(str(ans))
        except:
            self.display.setText("Input Incorrect")
    
    def actionRem(self):
        txt = self.display.text()
        self.display.setText(txt+"%")
    
    def actionBrcOn(self):
        txt = self.display.text()
        self.display.setText(txt+"(")
    
    def actionBrcOff(self):
        txt = self.display.text()
        self.display.setText(txt+")")
    
    def actionPow(self):
        txt = self.display.text()
        self.display.setText(txt+"pow(")
    
    def actionExp(self):
        txt = self.display.text()
        self.display.setText(txt+"exp(")
    
    def actionSquare(self):
        txt = self.display.text()
        self.display.setText(txt+"pow(2,")
    
    def actionLogx(self):
        txt = self.display.text()
        self.display.setText(txt+"math.log(math.pi,")
    
    def actionPerm(self):
        txt = self.display.text()
        self.display.setText(txt+"math.perm(")
    
    def actionComb(self):
        txt = self.display.text()
        self.display.setText(txt+"math.comb(")

    def actionLog2(self):
        txt = self.display.text()
        self.display.setText(txt+"math.log2(")
    
    def actionLog10(self):
        txt = self.display.text()
        self.display.setText(txt+"math.log10(")    
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    darkalcpro = QtWidgets.QMainWindow()
    ui = Ui_darkalcpro()
    ui.setupUi(darkalcpro)
    darkalcpro.show()
    sys.exit(app.exec_())
