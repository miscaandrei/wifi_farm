#!/usr/bin/python
# -*- coding: utf-8 -*-
 
from PyQt4 import *
from MainWindows_class import *
import sys
 
global app

'''
class Dialog(QtGui.QDialog,Ui_Dialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)
   
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
        
    def temp_apagar(self):
        self.temperatura_estat_funcionament.setText('Parat')
    
    def temp_encendre(self):
        self.temperatura_estat_funcionament.setText('En Marxa')
    


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

'''


if __name__ == "__main__":
    global app
    app = QtGui.QApplication(sys.argv)
    finestra = MainWindow()
    finestra.show()

    
    sys.exit(app.exec_())
