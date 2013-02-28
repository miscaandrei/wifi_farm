#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
from PyQt4 import QtGui, QtCore
import serial # if you have not already done so
ser = serial.Serial('/dev/ttyACM0', 9600)
ser.write('O')


class Example(QtGui.QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
        
    def initUI(self):      

        btn1 = QtGui.QPushButton("Button 1", self)
        btn1.move(30, 50)

        btn2 = QtGui.QPushButton("Button 2", self)
        btn2.move(150, 50)
        
        
        self.statusBar().showMessage('Status: OFF')
        ser.write('O')
        
        btn1.clicked.connect(self.buttonClickedOn)            
        btn2.clicked.connect(self.buttonClickedOff)
        
        self.statusBar()
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()
        
    def buttonClickedOn(self):
        self.statusBar().showMessage('Status: ON')
        ser.write('I')
    
    def buttonClickedOff(self):
        self.statusBar().showMessage('Status: OFF')
        ser.write('O')
    
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    


if __name__ == '__main__':
    main()
    


    
'''
missatge=''
estat_led='Apagat'
print ser.readline()
while (missatge!='Exit'):
    print '+-----------------+'
    missatge=raw_input("| ON per encendre |\n| OFF per apagar  |\n| Exit per sortir | \n+-----------------+ \n Opcio: ")
    print '\n+------------------+'
    if (missatge=='ON'):
        print '| Estat LED: Ences |'
        ser.write('I')
        print ser.readline()
        
    elif (missatge=='OFF'):
        ser.write('O')
        print '| Estat LED: Apagat |'
        print ser.readline()
    elif (missatge=='Exit'):
        print ' ##~~ Good Bye ~~##'
    else:
        print 'Opcio No disponible'
    print '+------------------+\n\n'
    
'''
