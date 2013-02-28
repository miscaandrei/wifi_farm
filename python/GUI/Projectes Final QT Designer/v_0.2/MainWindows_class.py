#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import *
from MainWindow import *
from dialog_class import *
from dialog_2_class import *
import sys


class MainWindow(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)
    
    
    #SLOTS MainWindow#
    def administra_complex_1(self):
        #deixem per mes tard
        print "Executant commanda: administra_complex_1() "
        administra = Dialog(self)
        ok = administra.exec_()
        
    
    def administra_complex_2(self):
        #deixem per mes tard
        print "Executant commanda: administra_complex_2() "
    
    def administra_complex_3(self):
        #deixem per mes tard
        print "Executant commanda: administra_complex_3() "
    
    def finestra_canvia_valors(self):
        #obre el dialog per canvia els valors del programa
        print "Canvia Valors"
