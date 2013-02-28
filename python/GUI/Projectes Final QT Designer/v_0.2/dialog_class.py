#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import *
from Dialog_3 import *
from MainWindows_class import *
import sys



class Dialog(QtGui.QDialog,Ui_Dialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)
        self.valors_actuals()
   
    def valors_actuals(self):
       self.temperatura_lcd.display(32.5)
       self.temperatura_set.setValue(32.5)
   
   
    #SLOTS DIALOG#
    def apagar_llum_1(self):
        #deixem per mes tard
        print "Executant commanda: Apagar LLum nº 1 "
        self.estat_llum_1.setText('Apagat')
    
    
    def apagar_llum_2(self):
        #deixem per mes tard
        print "Executant commanda: Apagar LLum nº 2 "
        self.estat_llum_2.setText('Apagat')
    
    
    def apagar_llum_3(self):
        #deixem per mes tard
        print "Executant commanda: Apagar LLum nº 3"
        self.estat_llum_3.setText('Apagat')
    
    
    def encendre_l_1(self):
        #deixem per mes tard
        print "Executant commanda: Encenen LLum nº 1"
        self.estat_llum_1.setText('Ences')
    
    def encendre_l_2(self):
        #deixem per mes tard
        print "Executant commanda: Encenen LLum nº 2"
        self.estat_llum_2.setText('Ences')
    
    def encendre_l_3(self):
        #deixem per mes tard
        print "Executant commanda: Encenen LLum nº 3"
        self.estat_llum_3.setText('Ences')
    
    
    def set_calefacio(self, valor_numeric):
        #deixem per mes tard
        print "Executant commanda: Ajustant Calefaccio a  "+str(valor_numeric)+" º"
        self.temperatura_lcd.display(valor_numeric)
        
        
    def temp_apagar(self):
        self.temperatura_estat_funcionament.setText('Parat')
    
    def temp_encendre(self):
        self.temperatura_estat_funcionament.setText('En Marxa')
    
