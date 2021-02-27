from PyQt5 import QtCore, QtGui, QtWidgets
from random import choices


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(722, 506)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        
        self.RegNoInput = QtWidgets.QLineEdit(self.centralwidget)
        self.RegNoInput.setGeometry(QtCore.QRect(210, 30, 181, 21))
        self.RegNoInput.setObjectName("RegNoInput")
        
        
        self.PassWordInput = QtWidgets.QLineEdit(self.centralwidget)
        self.PassWordInput.setGeometry(QtCore.QRect(210, 60, 181, 22))
        self.PassWordInput.setObjectName("PassWordInput")
        
        
        self.PollComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.PollComboBox.setGeometry(QtCore.QRect(210, 90, 181, 22))
        self.PollComboBox.setEditable(False)
        self.PollComboBox.setObjectName("PollComboBox")
        poll_option=["B","C","RANDOM"]
        self.PollComboBox.addItems(poll_option)
        
        self.RunButton = QtWidgets.QPushButton(self.centralwidget)
        self.RunButton.setGeometry(QtCore.QRect(510, 50, 93, 28))
        self.RunButton.setObjectName("RunButton")
        self.RunButton.clicked.connect(self.trigger)
        
        self.RegNo = QtWidgets.QLabel(self.centralwidget)
        self.RegNo.setGeometry(QtCore.QRect(30, 30, 161, 21))
        self.RegNo.setObjectName("RegNo")
        
        self.PassWord = QtWidgets.QLabel(self.centralwidget)
        self.PassWord.setGeometry(QtCore.QRect(30, 60, 171, 21))
        self.PassWord.setObjectName("PassWord")
        
        self.PollOptionLabel = QtWidgets.QLabel(self.centralwidget)
        self.PollOptionLabel.setGeometry(QtCore.QRect(30, 90, 171, 21))
        self.PollOptionLabel.setObjectName("PollOptionLabel")
        
        
        
        self.ScriptStatusLabel = QtWidgets.QLabel(self.centralwidget)
        self.ScriptStatusLabel.setGeometry(QtCore.QRect(40, 160, 671, 291))
        self.ScriptStatusLabel.setObjectName("ScriptStatusLabel")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 722, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CLASS SCRIPT"))
        self.RunButton.setText(_translate("MainWindow", "Attendance++"))
        self.RegNo.setText(_translate("MainWindow", "Registration Number For Lpu : "))
        self.PassWord.setText(_translate("MainWindow", "Password For Myclass: "))
        self.PollOptionLabel.setText(_translate("MainWindow", "Select Polling Options: "))
        self.ScriptStatusLabel.setText(_translate("MainWindow", "STATUS TEXT"))
        
        
    
    def trigger(self):
        # Your id below
        id_ = str(self.RegNoInput.text())
# your password below
        pass_ = str(self.PassWordInput.text())

        method = "Microphone"
        
        
        if self.PollComboBox.currentText=="RANDOM":
            options=["A","B","C","D"]
            probabity=[0.25,0.25,0.25,0.25]
            x = choices(options,probabity)
            poll=str(x)
        else:
            poll = str(self.PollComboBox.currentText())

        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions
        from selenium.webdriver.common.by import By
        from selenium.webdriver.chrome.options import Options

#setting permissions to the browser
        opt = Options()
        opt.add_argument("start-maximized")
        opt.add_experimental_option("prefs", { \
        "profile.default_content_setting_values.media_stream_mic":1,
    })

#locating the webdriver
        driver = webdriver.Chrome(options=opt,  executable_path="C:\Programdata\chromedriver.exe")

#the class joining function
        def onlineclassscript():
            def labelprint(message):
                return self.ScriptStatusLabel.setText(message)
    
            #connecting to login page
            driver.get("https://myclass.lpu.in")
            print(driver.title)

    #logging in
            username = driver.find_element_by_name("i")
            username.send_keys(id_)
            password = driver.find_element_by_name("p")
            password.send_keys(pass_)
            password.send_keys(Keys.ENTER)

    #finding and clicking on Classes/Meetings
            match_search = WebDriverWait(driver,20).until(
                expected_conditions.presence_of_element_located(
                    (By.LINK_TEXT, "View Classes/Meetings")
                )
            )

            search = driver.find_element_by_link_text("View Classes/Meetings")
            search.click()
    
    #finding any running classes
            match_search = WebDriverWait(driver,20).until(
                expected_conditions.presence_of_element_located(
                    (By.CLASS_NAME, "fc-content")
            )
            )
    #joining the running classes
            import time
            while True:
                try:
                    
                    search = driver.find_element_by_css_selector('a[style*="color: white; background: green;"]')
                    search.click()
                    break
                except Exception as e:
                    time.sleep(120)
                    labelprint("no class now")
                    onlineclassscript()
                    
    
            match_search = WebDriverWait(driver,20).until(
                expected_conditions.presence_of_element_located(
                    (By.CSS_SELECTOR, 'a[role="button"]')
                )
            )
            search = driver.find_element_by_css_selector('a[role="button"]')
            search.click()
    
    #switching to the audio choice frame
            match_search = WebDriverWait(driver,400).until(
                expected_conditions.presence_of_element_located(
                    (By.ID, 'frame')
                )
            )
            iframe = driver.find_element_by_id('frame')
            driver.switch_to.frame(iframe)
    
    #choosing microphone method
            match_search = WebDriverWait(driver,20).until(
                expected_conditions.presence_of_element_located(
                    (By.CSS_SELECTOR, 'button[aria-label="' + method +'"]')
            )
            )
            search = driver.find_element_by_css_selector('button[aria-label="' + method +'"]')
            search.click()
    
    #doing echo test
            match_search = WebDriverWait(driver,20).until(
                expected_conditions.presence_of_element_located(
                    (By.CSS_SELECTOR, 'button[aria-label="Echo is audible"]')
            )
            )
            search = driver.find_element_by_css_selector('button[aria-label="Echo is audible"]')
            search.click()
    
    #waiting for class end
            while True:
                try:
                    match_search = WebDriverWait(driver,3).until(
                        expected_conditions.presence_of_element_located(
                            (By.CSS_SELECTOR, 'button[aria-label="OK"]')
                        )
                    )
            #joining any next class if any 
                    onlineclassscript()
                except Exception as e:
                    
                    try:
                        match_search = WebDriverWait(driver,117).until(
                            expected_conditions.presence_of_element_located(
                                (By.CSS_SELECTOR, 'div[class*="pollingContainer"]')
                            )
                        )
                        time.sleep(4000)
                        try:
                            search = driver.find_element_by_css_selector('button   [aria-label="'+poll+'"]')
                            search.click()
                            labelprint("poll attended!!!")
                        except Exception as e:
                            search = driver.find_element_by_css_selector('button[aria-label="Yes"]')
                            search.click()
                            labelprint("poll attended!!!")
                    except Exception as e:
                        labelprint("class running!")
            

        onlineclassscript()
    print("running")
    
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
