import sys
import healthApplicationMainWindowGUI
from healthApplicationMainWindowGUI import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import data as d
import writtenToExcel as written


class HealthApp(Ui_MainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        # self.setWindowTitle("Health App")
        # self.resize(957, 610)
        self.setupUi(self)
        self.run()
      
    def run(self):
        self.nursePushButton.clicked.connect(self.nurseButtonPressed)   
        self.doctorPushButton.clicked.connect(self.doctorPushButtonPressed)
        
    def nurseButtonPressed(self): # move to the next page when the nurse button is pushed
        print("Hello")
        # self.stackedWidget.setCurrentIndex(1)
        
        
    def doctorPushButtonPressed(self): # move to the next page when the doctor button is pushed
        print("Hello I am Doctor")    
    # self.stackedWidget.setCurrentIndex(1)
        
    def acceptInfoButtonPresses(self): # move to the next page after collecting the information
        first_name = self.firstNameInput.getText()
        middle_name = self.middleNameInput.getText()
        last_name = self.lastNameInput.getText()
        phone_number = self.phoneNumberInput.getText()
        email = self.emailInput.getText()
        # input variables into the excel sheet
        self.stackedWidget.setCurrentIndex(2)

    
if __name__ == "__main__":
    d.func()
    written.create_excel()
    app = QtWidgets.QApplication(sys.argv)
    win = Ui_MainWindow()
    win.show()
    sys.exit(app.exec())





