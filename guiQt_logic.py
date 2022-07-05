import serial
import sys, time
import serial.tools.list_ports
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication
from guiQt import Ui_Dialog

comESP = 'Silicon' 

class windowSerial(QtWidgets.QMainWindow,Ui_Dialog):

    def __init__(self):
        super(windowSerial, self).__init__()
        
        ########################################## Main #############################################
        
        # Start the program
        print('')
        print('************************************************************************')
        print('*                              Hema (C) 2022                           *')
        print('*            Python programmer for pyLadies-Berlin June Talk           *')
        print('*                       Version 0.0.1; 2022-06-20                      *')
        print('************************************************************************')
        print('')
        
        self.setupUi(self)
        self.pbClear.clicked.connect(self.clear)
        self.pbStop.clicked.connect(self.stop)
        self.pbStart.clicked.connect(self.start)
        self.pbExit.clicked.connect(self.exit)
        self.pbConnect.clicked.connect(self.conn)
        self.pbInput.clicked.connect(self.input)
        self.pbDisconnect.clicked.connect(self.disconn)
        self.rbBluetooth.toggled.connect(self.bluetooth)
        self.rbWifi.toggled.connect(self.wifi)
        self.rbCellular.toggled.connect(self.cellular)
        
        self.findComPort() 

    ########################################### Functions ############################################

    def findComPort(self):

        ports = serial.tools.list_ports.comports()

        for port, desc, hwid in sorted(ports):
            #if (desc[0:7] == comESP):
            self.comboBox.addItem(desc)
        
    def bluetooth(self):
        print('\nActivating Bluetooth connection...')

    def wifi(self):
        print('\nActivating Wi-Fi connection...')

    def cellular(self):
        print('\nActivating Cellular connection...')

    def start(self):
        print('Progressing.............0%')
        time.sleep(2)
        print('\nProgressing.............25%')
        time.sleep(2)
        print('\nProgressing.............50%')
        time.sleep(2)
        print('\nProgressing.............75%')
        time.sleep(2)
        print('\nProgressing.............100%')
        time.sleep(2)
        print('\nExecution successful!')
        self.ok_icon.setPixmap(QtGui.QPixmap("images/tick.png"))
        self.ok_icon.resize(100,74)
        self.ok_icon.setGeometry(380,470,300,150)
    
    def stop(self):
        print('\nExecution aborted!')

    def input(self):
        print('\nCommand received: '+ self.sendCommand.text())

    def clear(self):
        self.sendCommand.clear()
        print('\nCommand cleared!')

    def conn(self):
        print('\nConnected to COM port!')

    def disconn(self):
        print('\nDisconnected from COM port!')

    def exit(self):
        sys.exit()

if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = windowSerial()
    window.show()
    sys.exit(App.exec_()) 