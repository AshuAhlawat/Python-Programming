from PyQt5 import QtCore, QtGui, QtWidgets,QtPrintSupport
from PyQt5.QtWidgets import QApplication,QFileDialog, QFontDialog, QListWidget, QScrollArea, QScrollBar,QWidget
from PyQt5.QtCore import Qt
import os
import sys



class Ui_DarkPad(object):
    def setupUi(self, DarkPad):
        '''creating a method that takes the resolution of the screen and use it in darkpad'''
        
        self.desktop=QApplication.desktop()
        self.screenRect=self.desktop.screenGeometry()
        h=self.screenRect.height()
        w=self.screenRect.width()
        self.path=None
        
        
        DarkPad.setObjectName("DarkPad")
        self.centralwidget = QtWidgets.QWidget(DarkPad)
        self.centralwidget.setObjectName("centralwidget")
        self.editor = QtWidgets.QTextEdit(self.centralwidget)
        self.editor.setGeometry(QtCore.QRect(0, 0, w, h))
        self.editor.setMouseTracking(True)
        self.editor.setObjectName("plainTextEdit")
        DarkPad.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DarkPad)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 689, 26))
        self.menubar.setObjectName("menubar")
        DarkPad.setGeometry(QtCore.QRect(0,0,w/2,h/2))

        #fixing the font
        fixedfont=QtGui.QFontDatabase.systemFont(QtGui.QFontDatabase.FixedFont)
        fixedfont.setPointSize(18)
        self.editor.setFont(fixedfont)
        
        #creating a horizontal scroll bar
        
        
        #file tab details
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        
        #edit tab details
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        
        #Format tab Details
        self.menuFormat = QtWidgets.QMenu(self.menubar)
        self.menuFormat.setObjectName("menuFormat")
        
        #Utility tab Details
        self.menuWeb=QtWidgets.QMenu(self.menubar)
        self.menuWeb.setObjectName("menuWeb")
        
        DarkPad.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DarkPad)
        self.statusbar.setObjectName("statusbar")
        DarkPad.setStatusBar(self.statusbar)
        
        #file->New
        self.actionNew = QtWidgets.QAction(DarkPad)
        self.actionNew.setObjectName("actionNew")
        
        #file->Open
        self.actionOpen = QtWidgets.QAction(DarkPad)
        self.actionOpen.setObjectName("actionOpen")
        
        #file->Save
        self.actionSave = QtWidgets.QAction(DarkPad)
        self.actionSave.setObjectName("actionSave")
        #edit->Undo
        self.actionUndo = QtWidgets.QAction(DarkPad)
        self.actionUndo.setObjectName("actionUndo")
        
        #edit->Copy
        self.actionCopy = QtWidgets.QAction(DarkPad)
        self.actionCopy.setObjectName("actionCopy")
        
        #edit->Paste
        self.actionPaste = QtWidgets.QAction(DarkPad)
        self.actionPaste.setObjectName("actionPaste")
        
        self.actionSaveas=QtWidgets.QAction(DarkPad)
        self.actionSaveas.setObjectName("actionSaveas")
        
        #edit->Select All
        self.actionSelect_All = QtWidgets.QAction(DarkPad)
        self.actionSelect_All.setObjectName("actionSelect_All")
        
        #format->Word Wrap
        self.actionWord_Wrap = QtWidgets.QAction(DarkPad)
        self.actionWord_Wrap.setObjectName("actionWord_Wrap")
        self.actionWord_Wrap.setCheckable(True)
        self.actionWord_Wrap.setChecked(True)
        self.actionWord_Wrap.triggered.connect(self.word_wrap)
        
        #edit-> Font Box
        self.actionFont=QtWidgets.QAction(DarkPad)
        self.actionFont.setObjectName("actionFont")
        
        #Web-> Login
        self.actionLogin=QtWidgets.QAction(DarkPad)
        self.actionLogin.setObjectName("actionLogin")
        
        
        #adding action to the above options
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveas)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionFont)
        self.menuEdit.addAction(self.actionSelect_All)
        self.menuFormat.addAction(self.actionWord_Wrap)
        self.menuWeb.addAction(self.actionLogin)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuFormat.menuAction())
        self.menubar.addAction(self.menuWeb.menuAction())
        

        self.retranslateUi(DarkPad)
        QtCore.QMetaObject.connectSlotsByName(DarkPad)
        

    def retranslateUi(self, DarkPad):
        
        #detailing the above file,edit,format and their subs
        _translate = QtCore.QCoreApplication.translate
        DarkPad.setWindowTitle(_translate("DarkPad", "DarkPad"))
        self.menuFile.setTitle(_translate("DarkPad", "File"))
        self.menuEdit.setTitle(_translate("DarkPad", "Edit"))
        self.menuFormat.setTitle(_translate("DarkPad", "Format"))
        self.menuWeb.setTitle(_translate("DarkPad","Utility"))
        self.actionNew.setText(_translate("DarkPad", "New"))
        self.actionNew.setStatusTip(_translate("DarkPad", "Create a new file"))
        
        self.actionNew.setShortcut(_translate("DarkPad", "Ctrl+N"))
        self.actionOpen.setText(_translate("DarkPad", "Open"))
        self.actionOpen.setStatusTip(_translate("DarkPad", "Open a file"))
        self.actionOpen.setShortcut(_translate("DarkPad", "Ctrl+O"))
        self.actionSave.setText(_translate("DarkPad", "Save"))
        self.actionSave.setStatusTip(_translate("DarkPad", "Save the file"))
        self.actionSave.setShortcut(_translate("DarkPad", "Ctrl+S"))
        self.actionUndo.setText(_translate("DarkPad", "Undo"))
        self.actionUndo.setStatusTip(_translate("DarkPad", "Undo a action"))
        self.actionUndo.setShortcut(_translate("DarkPad", "Ctrl+Z"))
        self.actionCopy.setText(_translate("DarkPad", "Copy"))
        self.actionCopy.setStatusTip(_translate("DarkPad", "Copy a file"))
        self.actionCopy.setShortcut(_translate("DarkPad", "Ctrl+C"))
        self.actionPaste.setText(_translate("DarkPad", "Paste"))
        self.actionPaste.setStatusTip(_translate("DarkPad", "Paste a file"))
        self.actionPaste.setShortcut(_translate("DarkPad", "Ctrl+V"))
        self.actionSelect_All.setText(_translate("DarkPad", "Select All"))
        self.actionSelect_All.setStatusTip(_translate("DarkPad", "Select all"))
        self.actionSelect_All.setShortcut(_translate("DarkPad", "Ctrl+A"))
        self.actionWord_Wrap.setText(_translate("DarkPad", "Word Wrap"))
        self.actionSaveas.setText(_translate("Darkpad","Save As"))
        self.actionSaveas.setStatusTip(_translate("DarkPad","Save the current file"))
        self.actionSaveas.setShortcut(_translate("DarkPad","Ctrl+Alt+S"))
        self.actionFont.setText(_translate("DarkPad","select Font"))
        self.actionFont.setStatusTip(_translate("Darkpad","Select Font And Size"))
        
        self.actionLogin.setText(_translate("DarkPad","Darkalc"))
        self.actionLogin.setStatusTip(_translate("DarkPad","Click to Use Darkalc for basic calculation "))
        
        self.actionCopy.triggered.connect(self.editor.copy)
        self.actionPaste.triggered.connect(self.editor.paste)
        self.actionUndo.triggered.connect(self.editor.undo)
        self.actionSaveas.triggered.connect(self.saveas_file)
        self.actionSave.triggered.connect(self.save_file)
        self.actionOpen.triggered.connect(self.open_file)
        self.actionFont.triggered.connect(self.font_box)
        self.actionLogin.triggered.connect(self.Login)
    
    def open_file(self):
        path,_=QtWidgets.QFileDialog.getOpenFileName(None,'OpenTextFile','/')
        if path: 
            # try opening path 
            try: 
                with open(path, 'r') as f: 
                    text = f.read()  
            except :
                print(Exception) 
            else: 
                self.path = path  
                self.editor.setPlainText(text) 
    
    def saveas_file(self):
        s_file=QtWidgets.QFileDialog.getSaveFileName(None,'SaveTextFile','',"Text Files (*.txt);;All files(*)")
        text=self.editor.toPlainText()
        
        if s_file[0]:
            with open(s_file[0],'w') as f:
                f.write(text)
        
    def save_file(self):
        if self.path is None:
            return self.saveas_file()
        else:
            self.save_to_path(self.path)
        
    def save_to_path(self,path):
        t=self.editor.toPlainText()
        
        try:
            with open(path,'w') as f:
                f.write(t)
        except:
            print(Exception)
        else:
            self.path=path

            
    
    def word_wrap(self):
        self.editor.setLineWrapMode(1 if self.editor.lineWrapMode()== 0 else 0)
    
    def font_box(self):
        font,ok=QFontDialog.getFont()
        if ok:
            self.editor.setFont(font)
            print("Display Fonts",font)
    
    def Login(self):
        import os 
        os.system('python darkalcpro.py')
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    palette = QtGui.QPalette()
    palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53,53,53))
    palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Base, QtGui.QColor(15,15,15))
    palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53,53,53))
    palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53,53,53))
    palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
         
    palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(200,150,0).lighter())
    palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
    app.setPalette(palette)
    DarkPad = QtWidgets.QMainWindow()
    ui = Ui_DarkPad()
    ui.setupUi(DarkPad)
    DarkPad.show()
    sys.exit(app.exec_())