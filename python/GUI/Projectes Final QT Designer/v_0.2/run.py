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

def inicialitzar_valors(finestra):
    lista = llegeix_arxiu()
    for element in lista:
        print element
    finestra.complex_1_temperatura.display(lista[0])
    finestra.complex_1_humitat.display(lista[1])
    finestra.complex_1_lluminositat.display(lista[2])
    
    finestra.complex_2_temperatura.display(lista[3])
    finestra.complex_2_humitat.display(lista[4])
    finestra.complex_2_lluminositat.display(lista[5])
    
    finestra.complex_3_temperaura.display(lista[6])
    finestra.complex_3_humitat.display(lista[7])
    finestra.complex_3_luminositat.display(lista[8])
    
    finestra.aus_adults_lcd.display(lista[9])
    finestra.aus_creixent_lcd.display(lista[10])
    finestra.aus_totals.display(lista[9]+lista[10])
    
    finestra.altre_total.display(lista[11]+lista[12])
    finestra.altre_adults_lcd.display(lista[11])
    finestra.altre_creixent_lcd.display(lista[12])

    finestra.aus_adults_progress_bar.setValue(lista[9]*100/(lista[9]+lista[10]))
    finestra.aus_creixent_progress_bar.setValue(lista[10]*100/(lista[9]+lista[10]))
    
    
    finestra.altre_adults_progress_bar.setValue(lista[11]*100/(lista[11]+lista[12]))
    finestra.altre_creixent_progress_bar.setValue(lista[12]*100/(lista[11]+lista[12]))



def llegeix_arxiu():
    print 'Llegint arxiu'
    lista=[21,18,76,21,25,95,23,23,5,300,200,200,150]
    return lista



if __name__ == "__main__":
    global app
    app = QtGui.QApplication(sys.argv)
    finestra = MainWindow()
    finestra.show()
    
    inicialitzar_valors(finestra)

    
    sys.exit(app.exec_())



