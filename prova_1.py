#!/usr/bin/python
# -*- coding: utf-8 -*-

import serial # if you have not already done so
ser = serial.Serial('/dev/ttyACM0', 9600)
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
    
