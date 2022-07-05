# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiQt.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import pyqtSignal

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("GUIs are so cool!!!")
        Dialog.resize(900, 650)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        Dialog.setFont(font)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("background-color: rgb(32, 32, 32);")
        self.pbExit = QtWidgets.QPushButton(Dialog)
        self.pbExit.setGeometry(QtCore.QRect(750, 60, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbExit.setFont(font)
        self.pbExit.setStyleSheet('QPushButton {background-color: rgb(183, 155, 255); border-radius: 12px}')
        self.pbExit.setObjectName("pushButton_2")
        self.pbConnect = QtWidgets.QPushButton(Dialog)
        self.pbConnect.setGeometry(QtCore.QRect(650, 158, 91, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pbConnect.setFont(font)
        self.pbConnect.setAutoFillBackground(False)
        self.pbConnect.setStyleSheet('QPushButton {background-color: rgb(144, 255, 144); border-radius: 12px}')
        self.pbConnect.setCheckable(False)
        self.pbConnect.setObjectName("pushButton_3")
        self.pbClear = QtWidgets.QPushButton(Dialog)
        self.pbClear.setGeometry(QtCore.QRect(750, 330, 91, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pbClear.setFont(font)
        self.pbClear.setAutoFillBackground(False)
        self.pbClear.setStyleSheet('QPushButton {background-color: rgb(255, 255, 127); border-radius: 12px}')
        self.pbClear.setCheckable(False)
        self.pbClear.setObjectName("pushButton_4")
        self.pbDisconnect = QtWidgets.QPushButton(Dialog)
        self.pbDisconnect.setGeometry(QtCore.QRect(750, 158, 91, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pbDisconnect.setFont(font)
        self.pbDisconnect.setAutoFillBackground(False)
        self.pbDisconnect.setStyleSheet('QPushButton {background-color: rgb(255, 129, 131); border-radius: 12px}')
        self.pbDisconnect.setCheckable(False)
        self.pbDisconnect.setObjectName("pushButton_5")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(50, 162, 121, 31))
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setStyleSheet("color: rgb(255, 255, 255);")
        self.textBrowser.setFont(QtGui.QFont('Arial', 11))
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_3 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_3.setGeometry(QtCore.QRect(50, 252, 121, 31))
        self.textBrowser_3.setAutoFillBackground(False)
        self.textBrowser_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.textBrowser_3.setFont(QtGui.QFont('Arial', 11))
        self.textBrowser_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(50, 332, 121, 31))
        self.textBrowser_2.setAutoFillBackground(False)
        self.textBrowser_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.textBrowser_2.setFont(QtGui.QFont('Arial', 11))
        self.textBrowser_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.sendCommand = extQLineEdit(self)
        self.sendCommand.setGeometry(190, 330, 448, 32)
        self.sendCommand.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 12px;")
        self.sendCommand.setPlaceholderText('<Command>')
        self.sendCommand.setFont(QtGui.QFont('Arial', 12))
        self.sendCommand.setObjectName("command")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(190, 160, 451, 31))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setFont(QtGui.QFont('Arial', 12))
        self.comboBox.setObjectName("comboBox")
        self.pbStop = QtWidgets.QPushButton(Dialog)
        self.pbStop.setGeometry(QtCore.QRect(540, 400, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pbStop.setFont(font)
        self.pbStop.setAutoFillBackground(False)
        self.pbStop.setStyleSheet('QPushButton {background-color: rgb(255, 129, 131); border-radius: 12px}')
        self.pbStop.setCheckable(False)
        self.pbStop.setObjectName("pushButton_7")
        self.pbStart = QtWidgets.QPushButton(Dialog)
        self.pbStart.setGeometry(QtCore.QRect(280, 400, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pbStart.setFont(font)
        self.pbStart.setAutoFillBackground(False)
        self.pbStart.setStyleSheet('QPushButton {background-color: rgb(144, 255, 144); border-radius: 12px}')
        self.pbStart.setCheckable(False)
        self.pbStart.setObjectName("pushButton_8")
        self.pbInput = QtWidgets.QPushButton(Dialog)
        self.pbInput.setGeometry(QtCore.QRect(650, 330, 91, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pbInput.setFont(font)
        self.pbInput.setAutoFillBackground(False)
        self.pbInput.setStyleSheet('QPushButton {background-color: rgb(144, 255, 144); border-radius: 12px}')
        self.pbInput.setCheckable(False)
        self.pbInput.setObjectName("pushButton_9")
        self.rbBluetooth = QtWidgets.QRadioButton(Dialog)
        self.rbBluetooth.setGeometry(QtCore.QRect(220, 255, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rbBluetooth.setFont(font)
        self.rbBluetooth.setStyleSheet("color: rgb(255, 255, 255);")
        self.rbBluetooth.setObjectName("radioButton")
        self.rbWifi = QtWidgets.QRadioButton(Dialog)
        self.rbWifi.setGeometry(QtCore.QRect(420, 255, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rbWifi.setFont(font)
        self.rbWifi.setStyleSheet("color: rgb(255, 255, 255);")
        self.rbWifi.setObjectName("radioButton_2")
        self.rbCellular = QtWidgets.QRadioButton(Dialog)
        self.rbCellular.setGeometry(QtCore.QRect(580, 255, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rbCellular.setStyleSheet("color: rgb(255, 255, 255);")
        self.rbCellular.setFont(font)
        self.rbCellular.setObjectName("radioButton_3")

        self.ok_icon = QtWidgets.QLabel(Dialog)

        self.pyladies_logo = QtWidgets.QLabel(Dialog)
        self.pyladies_logo.setPixmap(QtGui.QPixmap("images/pyBerlin.png"))
        self.pyladies_logo.resize(100,74)
        self.pyladies_logo.setGeometry(50,20,120,75)
        
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 100, 100, 11))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setText("GUIs are so cool!!!")
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setGeometry(380,70,172,20)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pbExit.setText(_translate("Dialog", "Exit"))
        self.pbConnect.setText(_translate("Dialog", "Connect"))
        self.pbClear.setText(_translate("Dialog", "Clear"))
        self.pbInput.setText(_translate("Dialog", "Input"))
        self.pbDisconnect.setText(_translate("Dialog", "Disconnect"))
        self.textBrowser_2.setText(_translate("Dialog", "Enter Command:"))
        self.textBrowser.setHtml(_translate("Dialog", "Select COM port:"))
        self.textBrowser_3.setHtml(_translate("Dialog", "Select Feature:"))
        self.pbStop.setText(_translate("Dialog", "Stop"))
        self.pbStart.setText(_translate("Dialog", "Start"))
        self.rbBluetooth.setText(_translate("Dialog", "Bluetooth"))
        self.rbWifi.setText(_translate("Dialog", "Wi-Fi"))
        self.rbCellular.setText(_translate("Dialog", "Cellular"))


class extQLineEdit(QLineEdit):
    clicked = pyqtSignal()
    def __init__(self,parent):
        QLineEdit.__init__(self,parent)
    def mousePressEvent(self,QMouseEvent):
        self.clicked.emit()