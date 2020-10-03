# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Medical_helper_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(958, 613)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(10, 20, 941, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.nursePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.nursePushButton.setGeometry(QtCore.QRect(260, 160, 461, 131))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.nursePushButton.setFont(font)
        self.nursePushButton.setObjectName("nursePushButton")
        self.doctorPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.doctorPushButton.setGeometry(QtCore.QRect(260, 330, 461, 131))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.doctorPushButton.setFont(font)
        self.doctorPushButton.setObjectName("doctorPushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 958, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titleLabel.setText(_translate("MainWindow", "Medical Appointment Helper"))
        self.nursePushButton.setText(_translate("MainWindow", "Nurse Consult"))
        self.doctorPushButton.setText(_translate("MainWindow", "Doctor Consult"))
        self.nursePushButton.clicked.connect(self.nurseButtonPush)
        self.doctorPushButton.clicked.connect(self.doctorButtonPush)
        
    def nurseButtonPush(self):
        print("Hello I am a nurse")
        
    def doctorButtonPush(self):
        print("Hello I am a Doctor")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

