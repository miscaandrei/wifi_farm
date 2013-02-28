#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
from PyQt4 import QtGui, QtCore
import serial # if you have not already done so
ser = serial.Serial('/dev/ttyACM0', 9600)
ser.write('O')


class Example(QtGui.QMainWindow):
    r=0
    g=0
    b=0
    
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
        
    def initUI(self):      

        btn1 = QtGui.QPushButton("Error ~ON~", self)
        btn1.move(50, 50)

        btn2 = QtGui.QPushButton("Error ~OFF~", self)
        btn2.move(150, 50)
        
        btn3 = QtGui.QPushButton("Warn ~ON~", self)
        btn3.move(50, 80)
        
        btn4 = QtGui.QPushButton("Warn ~OFF~", self)
        btn4.move(150, 80)
        
        btn5 = QtGui.QPushButton("LED Red", self)
        btn5.move(50, 110)
        
        btn6 = QtGui.QPushButton("LED Blue", self)
        btn6.move(50, 140)
        
        btn7 = QtGui.QPushButton("LED Green", self)
        btn7.move(50, 170)
        
        self.statusBar().showMessage('Status: OFF')
        ser.write('O')
        
        btn1.clicked.connect(self.buttonClickedOn)            
        btn2.clicked.connect(self.buttonClickedOff)
        btn3.clicked.connect(self.warningOn)
        btn4.clicked.connect(self.warningOff)
        btn5.clicked.connect(self.r)
        btn6.clicked.connect(self.g)
        btn7.clicked.connect(self.b)
        
        
        self.statusBar()
        
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Arduino Controler')
        self.show()
        
    def buttonClickedOn(self):
        self.statusBar().showMessage('Status: ON')
        ser.write('A')
    
    def buttonClickedOff(self):
        self.statusBar().showMessage('Status: OFF')
        ser.write('B')
    
    def warningOn(self):
        self.statusBar().showMessage('Status: ON')
        ser.write('C')
    
    def warningOff(self):
        self.statusBar().showMessage('Status: ON')
        ser.write('D')
    
    def r(self):
        if (self.r==0):
            ser.write('R')
            self.r=1
        else:
            ser.write('Q')
            self.r=0
    
    def g(self):
        if (self.g==0):
            ser.write('T')
            self.g=1
        else:
            ser.write('W')
            self.g=0
    
    def b(self):
        if (self.g==0):
            ser.write('S')
            self.g=1
        else:
            ser.write('V')
            self.g=0
    
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
