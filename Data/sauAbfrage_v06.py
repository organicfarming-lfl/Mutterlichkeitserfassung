#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 18:02:56 2020

title           :SauAbfrage_v05.py
description     :Einlesen der Sau Abfrage UIs
author          :Jonas Müller
e-mail          :Mueller.M.Jonas@gmx.de
date            :13.04.2021
version         :00.05
usage           :python pyscript.py
notes           :
python_version  :3.7.3
"""
# Libs
#import sys
#import os
#GuI Libs
#import PyQt5.QtCore
#import PyQt5.QtWidgets as widgets
# from PyQt5 import QtGui
# from PyQt5 import uic
# from PyQt5 import QtWidgets
from PyQt5 import QtCore

#from PyQt5 import uic

from functools import partial

class SauAbfrage: 
    def __init__(self, Sau_UI):
        self.Sau_UI=Sau_UI
        self.SauBoolean = False
        self.Saunummer= [self.Sau_UI.lineEdit_SauNr, 
                         self.Sau_UI.lineEdit_SauRasse,
                         self.Sau_UI.lineDate_Geburtsdatum,self.Sau_UI.lineEdit_NummerMutterSau,
                         self.Sau_UI.lineEdit_NummerVaterSau,self.Sau_UI.lineEdit_NameVaterSau,
                         self.Sau_UI.lineEdit_Abstammungsnummer]
#        self.Sau_UI.pushButton_PushSau.clicked.connect(partial(
#                self.Sau_Button))
#        return(self.SauBoolean)
        #date display format
        self.Date_format ="dd.MM.yy"        

        self.Sau_UI.lineDate_Geburtsdatum.setDisplayFormat(self.Date_format)
        
        
        self.Sau_UI.pushButton_WerteLoeschen.clicked.connect(self.Werte_Loeschen)

        # Sau_UI.lineDate_Geburtsdatums.setDisplayFormat('yyyy.MM.dd hh:mm:ss')
        pass
    def Werte_Loeschen(self):
        # print ("Löschen")
        for xx in range(len(self.Saunummer)):
            if xx == 2:
                self.Saunummer[xx].setDate(QtCore.QDate.fromString("01.01.00", self.Date_format))      
                self.Saunummer[xx].setEnabled(True)
                self.Saunummer[xx].setStyleSheet("background-color: white")
            else:
                self.Saunummer[xx].setText("")
                self.Saunummer[xx].setEnabled(True)
                self.Saunummer[xx].setStyleSheet("background-color: white")
            
        
        pass
    def Sau_Button(self, Files):
        """
        nur erlaubt wenn
        Saunummer, Sau Rasse, Geburtsdatum ausgefüllt sind, 
        wenn das wahr ist dann werden die felder ausgegraut damit sie nicht mehr verändert werden können.
        der Rückgabe wert ist ein Boolen das die Felder ausgefüllt sind
        Die Ausgelesenen Datein in einer Liste
        eine Errormeldung für die Statusleiste wenn diese nicht ausgefüllt sind
        """
        self.SauBoolean = False
        erforderlich= [self.Sau_UI.lineEdit_SauNr,self.Sau_UI.lineEdit_SauRasse, self.Sau_UI.lineDate_Geburtsdatum ]
        if (self.Sau_UI.lineEdit_SauNr.text() == "" or self.Sau_UI.lineEdit_SauRasse.text() =="" 
        or self.Sau_UI.lineDate_Geburtsdatum.text() =="01.01.00" or self.Sau_UI.lineDate_Geburtsdatum.text() =="01.01.2000"):
            for yy in range(len(erforderlich)):
                erforderlich[yy].setStyleSheet("background-color: yellow; border: 1px solid black;")

            self.SauBoolean = False
            error = "Bitte füllen Sie die markierten Zeilen aus"
            return (self.SauBoolean, self.Sau_Return(Files), error)
        else:
# =============================================================================
#             return standart color
# =============================================================================
            for yy in range(len(erforderlich)):
                erforderlich[yy].setStyleSheet("background-color: white")
                erforderlich[yy].setEnabled(False)
                
            self.SauBoolean = True
            error = None
            return (self.SauBoolean, self.Sau_Return(Files),error)
            
    def Sau_Return(self, Files):
        '''
        Gibt den Saufile zurück, dieser besteht aus
        Saunummer = ["Saunummer" =self.Sau_UI.lineEdit_Saunummer.text(), 
                     "Sau Rasse"= self.Sau_UI.lineEdit_SauRasse.text(), 
                     "Geburtsdatum"= self.Sau_UI.lineDate_Geburtsdatum.setDate(),
                     "Nummer Mutter Sau"= self.Sau_UI.lineEdit_NummerMutterSau.text(),
                     "Nummer Vater Sau"= self.Sau_UI.lineEdit_NummerVaterSau.text(),
                     "Name Vater Sau"= self.Sau_UI.lineEdit_NameVaterSau.text(),
                     "Abstammungsnummer"= self.Sau_UI.lineEdit_Abstammungsnummer.text()]
        '''

        for xx in range (0,len(self.Saunummer)):
            if xx ==2: #lese datum richtig aus
                Files[xx] = self.Sau_UI.lineDate_Geburtsdatum.date().toString(self.Date_format)
            else:
                Files[xx] = self.Saunummer[xx].text()
                
#            print(self.Saunummer[xx].text())
        # print(self.Sau_UI.lineDate_Geburtsdatum.date().toString(self.Date_format))
        # for xx in range (0,len(self.Saunummer)):
        #     Files[xx] = self.Saunummer[xx].text()
        return(Files)
        pass
    
    def Sau_Load(self, Files):
        '''
        Lädt die Files in die Leinedits
        set Saunummer.set(File[xx])
        '''
#        Date_edits = [0,2]
        
        for xx in range(0, len(self.Saunummer)):
#             set datum 
            if xx ==2: 
                self.Saunummer[xx].setDate(QtCore.QDate.fromString(Files[xx], self.Date_format))   
                self.Saunummer[xx].setEnabled(False)
            else:
                self.Saunummer[xx].setText(Files[xx])
                self.Saunummer[xx].setEnabled(False)
#        error = "das einlesen der Daten Funktioniert noch nicht"
#        return (error)
        
        pass
    def SaudropDown(self, Load):
        
        if Load == []:
            #erzeuge einen Boolean ob ein Eintrag existiert.
#            self.saudorpdown_eintragexistiert = True
            # es sind keine Sauen Bisher angelegt. 
            self.Sau_UI.comboBox_VorhandeneSau.setEnabled(False)
            self.Sau_UI.comboBox_VorhandeneSau.addItem("Keine Sau Angelegt")

        elif Load!= []:
            # es sind bereits sauen angelegt,
            #erzeuge ein neue Liste
            Load_Sau = []
            Vergleich = None
            #erzeugeden ersten eintrag
            self.Sau_UI.comboBox_VorhandeneSau.addItem("Bitte eine Sau auswählen")
            #wähle die Sau aus 
            for kk in range(len(Load)):
                einlesedata = Load[kk]
                if Vergleich == einlesedata[0]:
#                if einlesedata in Load_Sau:
                    pass
                else: 
                    Load_Sau.append(einlesedata)
                    self.Sau_UI.comboBox_VorhandeneSau.addItem("Saunummer= %s, Sau Rass = %s, Geburtsdatum =%s" %(einlesedata[0], einlesedata[1],einlesedata[2]))
                    self.Sau_UI.comboBox_VorhandeneSau.currentIndexChanged.connect(partial(self.ImportCombo, Load_Sau))
                    Vergleich = einlesedata[0]
#                    self.Sau_UI.comboBox_VorhandeneSau.activated(partial(self.Sau_Load, Load_Sau[0]))
        pass
    def ImportCombo(self, Load_Sau, integer):
        """
        lädt die ausgewählten daten aus der Combobox in die Sauabfrage
        der index startet aber bei 1-xxxx daher muss man minus 1 abziehen
        """
        self.Sau_Load(Load_Sau[integer-1])
#        print("Hello", nteger, Load_Sau[integer])