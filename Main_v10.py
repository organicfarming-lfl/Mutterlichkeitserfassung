#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 11:03:58 2020
title           :Main_10.py
description     :Bestimmung des Mütterlichkeitsindex von Sauen
author          :Jonas Müller
e-mail          :Mueller.M.Jonas@gmx.de
date            :13.04.2021
version         :00.10
usage           :python pyscript.py
notes           :
python_version  :3.7.3
"""


# Libs
import sys
import os
#GuI Libs
from PyQt5 import QtCore
from PyQt5 import QtWidgets
# from PyQt5 import QtGui
from PyQt5 import uic
#from PyQt5.QtWidgets import *
#from PyQt5.QtCore import QObject
from functools import partial
from PyQt5.QtGui import QIcon
# import pandas as pd #für date in save


# =============================================================================
# # programm path
# =============================================================================
current_dir = os.path.dirname(os.path.abspath(__file__))
save_dir = current_dir+"/Save/"
program_dir = current_dir+"/Data/"
sys.path.insert(1,program_dir)
# =============================================================================
# # Own modules 
# =============================================================================
#Programm_path = os.getcwd()
import Abfrage_v05 as abfrage
import Muetterlichkeitsindex_v06 as MI
import sauAbfrage_v06 as SauAbf
import Ausgabe_v07 as Ausgabe
import Save_v07 as Save

#import Test as Test



# =============================================================================
# Lade die Ui pfade
# =============================================================================
UI_dir = current_dir+"/UI/"
Main_window_UI = UI_dir+"MainWindow_05.ui"

# =============================================================================
# load all related ui´s
# =============================================================================
Sau_UI = UI_dir + "Sau_07.ui"

Abfrage_UI = UI_dir+"Abfrage_widget_10.ui"

Ausgabe_UI = UI_dir + "Ausgabe_04.ui"
 
#Test_ausgabe_UI = UI_dir+"Test_ausgabe_1.ui"

#erzeuge den save folder

if not os.path.exists(save_dir):
    os.makedirs(save_dir)
#else:
 #   print("Folder already exist")




class widget(QtWidgets.QWidget):
    '''
    generiert ein Widget in das Ui´s eingeladen werden können.
    '''
    def __init__(self, UI = None, parent = None):
            super(widget,self).__init__(parent)
            UI =uic.loadUi(UI, self)
#            self.ui.setupUi(self)
            UI.show()
            
class MainWindow(QtWidgets.QMainWindow):
    '''
    init das Main Window
    '''
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # init all uis
        self.Main_Window = uic.loadUi(Main_window_UI, self)
#        self.Ausgabe_widget = widget(Test_ausgabe_UI)
#        self.Abfrage_UI_widget = widget(Abfrage_UI)                     # lege eine neue seite an mit der UI
        #set Icon
        self.Main_Window.setWindowIcon(QIcon(current_dir+'/Images/walk-2672654_640_Skaliert.ico'))
        # string value 
        title = "Mütterlichkeitsindex für Sauen"
        # set the title 
        self.setWindowTitle(title) 
        
        self.count_AddWidget = 0        # nur ein Widget erlaubt bis dieses Gespeichert ist.
        self.Tab_count = 0              # Zählt die geöffneten Tabs
# =============================================================================
#         load files und erzeuge buttons
# =============================================================================
        self.Load_files()
        
        # init Save 
        self.save_init = Save.save()
        
        # init empty_files
        self.empty_init = Save.File()
        
        # init load
        
        # self.load_init=Save.load()          # init
        
# =============================================================================
#         pushbutton für einen Neue Abfrage
# =============================================================================
        self.Main_Window.pushButton_Neue_Abfrage.clicked.connect(partial(
                self.Add_Abfrage))
        self.Main_Window.actionNeu.triggered.connect(partial(
                self.Add_Abfrage))
        pass
    def Load_files(self):
        """
        Liest die Files ein und erzeugt ein Tablet widget mit diesen Files
        """
        Load=[]
        self.load_init=Save.load()          # init
        #lade die Files in ein Arry
        Load= self.load_init.find_files(save_dir)
        
# =============================================================================
        ##### lade das Bearbeiten Fenster
        if len(Load)!=0:
             self.ErfassteWuerfe_Widget(Load)
# =============================================================================
# =============================================================================
#         starte das Auswerte Programm
             self.UebersichtWuerfe(Load)
             self.UebersichtSauen(Load)

        
             
# =============================================================================
            
        pass
    def UebersichtWuerfe(self, Load):
        '''
        bestimmt die "Saunummer", "Wurfnummer", "Wurfdatum", "Eber Nummer", "Anzahl lebend geborener Ferkel",
                        "Anzahl erdrückter Ferkel", "Anzahl aufgezogener Ferkel", "Aufzuchtrate", "Anomalien (ja/nein)",
                        "Geburt", "Wurfqualität", "Gesundheitszustand"//Fitness, "Abliegeverhalten",
                        "Umgänglichkeit", "Mütterlichkeitsindex"
        und trägt diese in ein Widget ein wenn ein Mütterlichkeitsindex bestimmt wurde
        '''
        
        Header_UebersichtWuerfe = ["Sau-\nnummer","Wurf-\nnummer", "Wurfdatum", "Eber Nummer", "Lebend \n geb. Ferkel",
                        "Erdrückte \n Ferkel", "Aufgezogene \n Ferkel", "Aufzuchtrate \n in %", "Anomalien \n (ja/nein)", 
                        "Leistung","Geburt", "Wurfqualität", "Gesundheits- \nzustand", 
                        "Abliege-\nverhalten","Umgänglich-\nkeit", "Mütt. \nIndex"]
# =============================================================================
#         Sauen
# =============================================================================
                #Layout
        UebersichtWuerfe_layout = self.Main_Window.verticalLayout_UebersichtWuerfe

                # Schaue ob schon ein Widget angelegt wurde
        if UebersichtWuerfe_layout.count() == 1:
            #es wurde noch keins angelegt #erzeuge ein widget #erzeuge ein Table Widget
            self.UebersichtWuerfe_tableWidget = QtWidgets.QTableWidget()
        if UebersichtWuerfe_layout.count() != 1:
#            es wurde schon ein widget angelegt. lösche dieses
            UebersichtWuerfe_layout.removeWidget(self.UebersichtWuerfe_tableWidget)
            
        UebersichtWuerfe_layout.addWidget(self.UebersichtWuerfe_tableWidget)
        #erzeuge eine AusgabeList
        ausgabe = []
        for ee in range(len(Load)):
            einlesen = Load[ee]
            #checke ob ein Muetterlichkeitsindex bestimmt wurde

            for aa in (12,15,16, 17,18,64,76):
                if einlesen[aa] =="":
                    einlesen[aa] = 0
            
            if einlesen[76] != "": #noch kein Mütterlichkeitsindex bestimmt, setze die noch unbestimmten Variablen auf null
                if einlesen[64] == None or einlesen[64] =="":
                    einlesen[64] = 0
                if int(einlesen[17])!=0:
                    Aufzucht = str(round((int(einlesen[17])/
                                          (int(einlesen[12])+int(einlesen[16])-int(einlesen[15]))*100),1))
                    # Aufzucht = str(round(float(einlesen[64])/float(einlesen[17])*100,2))
                else:
                    Aufzucht = "0"
                Data = [einlesen[0],  #Saunummer
                        einlesen[8],  #Wurfnummer
                        einlesen[7],  #Wurfdatum
                        einlesen[9],  #Ebernummer
                        einlesen[12],  #Anzahl lebend geborener Ferkel
                        einlesen[18], #Anzahl erdrückter Ferkel 
                        einlesen[17], #Anzahle aufgezogener Ferkel
                        Aufzucht,                        
#                        str(round(float(einlesen[63])/float(einlesen[16])*100,2)),
#                        einlesen[63], #Aufzuchrate = Leistung/ #Anzahle aufgezogener Ferkel
                        einlesen[23], # Anomalien Ja  
                        einlesen[64], #Leistung
                        einlesen[65], #Geburt
                        einlesen[66], # Wurf
                        einlesen[67], #Fitness
                        einlesen[68], #Abliegeverhalten
                        einlesen[69], #umgaenglichkeit
                        einlesen[76]] #Muetterid
                ausgabe.append(Data)
                
        self.UebersichtWuerfe_tableWidget.setRowCount(len(ausgabe))                      # number of rows
        self.UebersichtWuerfe_tableWidget.setColumnCount(len(Header_UebersichtWuerfe))          # number of colums
        #setze die Einträge der Liste
        for kk in range(len(ausgabe)):
            UebersichtWuerfe_list = ausgabe[kk]
            for rr in range(len(UebersichtWuerfe_list)):
                #nun müssen wir Unterscheiden ob Zahlen oder die Ampel in die Tabelle soll 
                if rr == 8:
                    #anomalie umschreiben in Ja Nein
                    if UebersichtWuerfe_list[rr] == "True":
                        UebersichtWuerfe_list[rr] ="Ja"
                    elif UebersichtWuerfe_list[rr] == "False":
                        UebersichtWuerfe_list[rr] = "Nein"
                if rr in range(9,15):
                    #für die Ampel ab Geburt bis umgänglichkeit
                    Min = 3.3       #siehe Geburtsverhalten 3.3333
                    Max = 6.7       # siehe geburtsverhalten 6.66666
                    #check if a number is given
                    if UebersichtWuerfe_list[rr] =="":
                        UebersichtWuerfe_list[rr] = 0
                    else: 
                        UebersichtWuerfe_list[rr] = float(UebersichtWuerfe_list[rr])
                    #teile den werten die Farben zu
                    if UebersichtWuerfe_list[rr] >= Min:
                        if UebersichtWuerfe_list[rr] > Max: #green
                            Color = 'green'
                        if UebersichtWuerfe_list[rr] <=Max:   #yellow
                            Color = 'yellow'
                    else: #red
                        Color ='red'                    
                    LED = Ausgabe.LED(Color, 40,5,20) #set size
#                    LED = Ausgabe.LED(Color, size)
                    self.UebersichtWuerfe_tableWidget.setCellWidget(kk,rr, LED)


                else:
                    self.UebersichtWuerfe_tableWidget.setItem(kk,rr, QtWidgets.QTableWidgetItem(UebersichtWuerfe_list[rr]))
        
#        Füge Header ein und lasse das Table zeigen
        self.UebersichtWuerfe_tableWidget.setHorizontalHeaderLabels(Header_UebersichtWuerfe)
        self.UebersichtWuerfe_tableWidget.setSortingEnabled(True) #erlaubt das Sortieren der Tabelle
        self.UebersichtWuerfe_tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) #tabelle nicht editierbar
        # Alternierende Zeilen Fraben
        self.UebersichtWuerfe_tableWidget.setAlternatingRowColors(True)

        self.UebersichtWuerfe_tableWidget.show()
    
    def UebersichtSauen(self, Load):
        '''
        bestimmt die "Saunummer", "Anzahl erfasster Würfe", 
                       "Mittlere Anzahl lebend geborener Ferkel", 
                       "Mittlere anzahl erdrückter Ferkel", "Mittlere Anzahl aufgezogener Ferkel", 
                       "Mittlere Aufzuchtrate", "Mittlerer Mütterlichkeitsindex"
        asu den eingabe Datein und trägt diese in ein Widget ein wenn ein Mütterlichkeitsindex bestimmt wurde
        '''
        Header_UebersichtSauen = ["Saunummer", 
                                  "Anzahl \nerfasster Würfe", 
                                  "Mittl. Anzahl \nlebend geb.", 
                                  "Mittl. Anzahl \nerdrückter", 
                                  "Mittl. Anzahl \naufgezogener", 
                                  "Mittl. \nAufzuchtrate \nin %", 
                                  "Mittl. \nMütt. Index"]

# =============================================================================
#         Herde
# =============================================================================
        #Layout
        UebersichtSauen_layout = self.Main_Window.verticalLayout_UebersichtSauen
        # Schaue ob schon ein Widget angelegt wurde
        if UebersichtSauen_layout.count() == 1:
            #es wurde noch keins angelegt erzeuge ein widget erzeuge ein Table Widget
            self.UebersichtSauen_tableWidget = QtWidgets.QTableWidget()
            # self.UebersichtSauen_tableWidget = QtWidgets.QTableWidgetItem()
        if UebersichtSauen_layout.count() != 1:
#            es wurde schon ein widget angelegt.lösche dieses
            UebersichtSauen_layout.removeWidget(self.UebersichtSauen_tableWidget)
        
        
        UebersichtSauen_layout.addWidget(self.UebersichtSauen_tableWidget)
#        erzeuge eine Herden List
        UebersichtSauen_List = []
        #anzahl der Würfe
        Wurf_anzahl = 0 # wird aufsummiert muss null sein damit wir die daten in der For schlife initieren könne
        #Anzahl der lebend geborenen Ferkel
        leb_Ferkel = 0 # [12]
        #anzahl der erdrückten Ferkel 
        erd_Ferkel = 0 #[18]
        #anzahl der Aufgezogenen Ferkel 
        auf_ferkel = 0 #[17]
        #aufzuchtrate
        Aufzuchtrate = 0     
        #muetterlichketisindex
        Muetterlichkeitsindex = 0
        #wie viele komma stellen sollen ausgegeben werden
        rounddigit = 1
        Vergleich =None
        for kk in range(len(Load)):
            einlesedata = Load[kk]
            #checke das die Daten einen eintrag haben und setze leere strings auf null

            for aa in (12,15,16,17,18,64,76):
                if einlesedata[aa] =="":
                    einlesedata[aa] = 0
                #Sauen ob es einen Mütterlichktsindex gibt
            if einlesedata[76] != 0  and einlesedata[76]!= "":
                if Vergleich == None:
                # es wurden noch keine wurf erfasst
                #erfasse ersten wurf
                    
                    Wurf_anzahl = 1
                    leb_Ferkel = int(einlesedata[12])
                    erd_Ferkel = int(einlesedata[18])
                    auf_ferkel = int(einlesedata[17])
                    # if auf_ferkel !=0:
                    if int(einlesedata[17])!=0:
                        # Aufzuchtrate = int(einlesedata[64])/auf_ferkel
                        Aufzuchtrate = (int(einlesedata[17]))/(int(einlesedata[12])+int(einlesedata[16])-int(einlesedata[15]))
                    else: 
                        Aufzuchtrate = 0
                    Muetterlichkeitsindex = float(einlesedata[76])
                    Vergleich = einlesedata[0]

                    pass

        #Sau wurde bereits "erfasst" neue Daten zur Sau Hinzufügen
                elif Vergleich == einlesedata[0]:

#                Anzahl der Würfe
                    Wurf_anzahl +=1
# =============================================================================
                      
# =============================================================================
                    leb_Ferkel += int(einlesedata[12])
                    erd_Ferkel += int(einlesedata[18])
                    auf_ferkel += int(einlesedata[17])
                    # if auf_ferkel !=0:
                    if int(einlesedata[17])!=0:
                        # Mittel_Auf = int(int(einlesedata[64])/auf_ferkel)
                        Mittel_Auf = (int(einlesedata[17]))/(int(einlesedata[12])+int(einlesedata[16])-int(einlesedata[15]))
                        # print ('Mit_auf', Mittel_Auf)
                        pass
                    else: 
                        Mittel_Auf = 0
                    Aufzuchtrate += Mittel_Auf
                    Muetterlichkeitsindex += float(einlesedata[76])
                    pass
                elif Vergleich != einlesedata[0] and Vergleich != None:
#                    sau ist fertig ersfast worden
# =============================================================================
#                     schreibe datensatz in Herden List 
# =============================================================================
                    Datensatz = [Vergleich, str(Wurf_anzahl),                       #Wurnummer
                              str(round(leb_Ferkel/Wurf_anzahl,rounddigit)),        #lebende Ferkel
                              str(round(erd_Ferkel/Wurf_anzahl, rounddigit)),       #erdrückte Ferkel
                              str(round(auf_ferkel/Wurf_anzahl, rounddigit)),       #aufgezogene Ferkel
                              str(round(Aufzuchtrate/Wurf_anzahl*100, rounddigit)), #Aufzutsrate
                              str(round(Muetterlichkeitsindex/Wurf_anzahl, rounddigit))]    #Muetterlichkeitsindex
                    UebersichtSauen_List.append(Datensatz)
                    #setze neu daten für die Nächst Sau
                    Wurf_anzahl = 1
                    leb_Ferkel = int(einlesedata[12])
                    erd_Ferkel = int(einlesedata[18])
                    auf_ferkel = int(einlesedata[17])
                    # if auf_ferkel !=0:
                    if int(einlesedata[17])!=0:
                        # Aufzuchtrate = int(einlesedata[64])/int(einlesedata[17])
                        Aufzuchtrate = (int(einlesedata[17]))/(int(einlesedata[12])+int(einlesedata[16])-int(einlesedata[15]))
                    else:
                        Aufzuchtrate = 0
                    Muetterlichkeitsindex = float(einlesedata[76])
                    Vergleich = einlesedata[0]
# #            letzte datensatz angeheftet werden
# ### letzter datensatz muss manuell eingeschrieben werden! da erst ab dem Zweiten "verglichen" werden
                # for kk = len(Load):
            #checke das auch hier ein Muetterlichkeitsindex angegeben wurde
                if kk == len(Load)-1:
                    Letzter_Datensatz = [Vergleich, 
                              str(Wurf_anzahl),                                 #Wurnummer
                              str(round(leb_Ferkel/Wurf_anzahl,rounddigit)),    #lebende Ferkel
                              str(round(erd_Ferkel/Wurf_anzahl, rounddigit)),   #erdrückte Ferkel
                              str(round(auf_ferkel/Wurf_anzahl, rounddigit)),   #aufgezogene Ferkel
                              str(round(Aufzuchtrate/Wurf_anzahl*100, rounddigit)), #Aufzutsrate
                              str(round(Muetterlichkeitsindex/Wurf_anzahl, rounddigit))]    #Muetterlichkeitsindex
                    UebersichtSauen_List.append(Letzter_Datensatz)
        #erzeuge spalten und reihen der Tabelle 
        self.UebersichtSauen_tableWidget.setRowCount(len(UebersichtSauen_List))                      # number of rows
        self.UebersichtSauen_tableWidget.setColumnCount(len(Header_UebersichtSauen))          # number of colums
# =============================================================================
#         Trage alles in die Tabelle ein
# =============================================================================
        for tt in range(len(UebersichtSauen_List)):
            List_entry = UebersichtSauen_List[tt]
            for zz in range(len(Header_UebersichtSauen)):
                self.UebersichtSauen_tableWidget.setItem(tt,zz, QtWidgets.QTableWidgetItem(List_entry[zz]))
        
        
# #       Write Header and show Table
        self.UebersichtSauen_tableWidget.setHorizontalHeaderLabels(Header_UebersichtSauen)

        self.UebersichtSauen_tableWidget.setSortingEnabled(True) #erlaubt das Sortieren der Tabelle
        self.UebersichtSauen_tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) #tabelle nicht editierbar
#         # Alternaierende Zeilen Fraben
        self.UebersichtSauen_tableWidget.setAlternatingRowColors(True)

        self.UebersichtSauen_tableWidget.show()
        pass
    
    
    def ErfassteWuerfe_Widget(self, Files):
        """
        Liest alle files aus der Load funktion ein und Schreibt die Sauen in ein Bearbeiten_Widget array
        """
        xx = 0
        Bearbeit_Button= []                        # erzeuge eine Liste für die Bearbeiten Buttons
        Loesch_Button =[]
        Header = ['Saunummer', 'Sau Rasse', 'Geburtsdatum', 'Wurfdatum', 'Wurfnummer',"", ""]
        #load Layout
        ErfassteWuerfe_layout = self.Main_Window.verticalLayout_ErfassteWuerfe

        # Schaue ob schon ein Widget angelegt wurde
        if ErfassteWuerfe_layout.count() == 1:
            #es wurde noch keins angelegt
            #erzeuge ein widget
            self.ErfassteWuerfe_tableWidget = QtWidgets.QTableWidget()
        if ErfassteWuerfe_layout.count() != 1:
#            es wurde schon ein widget angelegt. 
#            lösche dieses und erzeuge ein neues
            ErfassteWuerfe_layout.removeWidget(self.ErfassteWuerfe_tableWidget)
        
        ErfassteWuerfe_layout.addWidget(self.ErfassteWuerfe_tableWidget)        
        self.ErfassteWuerfe_tableWidget.setRowCount(len(Files))                      # number of rows
        self.ErfassteWuerfe_tableWidget.setColumnCount(7)          # number of colums
        
        for xx in range(len(Files)):
            Data = Files[xx]
            for yy in range(0,3):               #fill in the first 3 colums 
                self.ErfassteWuerfe_tableWidget.setItem(xx,yy, QtWidgets.QTableWidgetItem(Data[yy]))
                pass
#                setze noch die Wurnummer
            for zz in range (7,9):
                # Wurfnummer und Wurfdatum
                self.ErfassteWuerfe_tableWidget.setItem(xx,zz-4, QtWidgets.QTableWidgetItem(Data[zz]))
#                    bearbeiten button
#            schreibe daten in das bearbeiten array


#            funktionen für den Bearbeiten Button
            Bearbeiten = QtWidgets.QPushButton("Bearbeiten", self)
            Bearbeit_Button.append(Bearbeiten)
            self.ErfassteWuerfe_tableWidget.setCellWidget(xx,5, Bearbeiten)
            Bearbeit_Button[xx].clicked.connect(partial(
                    self.Load_Widgets, Files[xx]))
#            funktionen für den Löschen Butten
            Loeschen= QtWidgets.QPushButton("Löschen", self)
            Loesch_Button.append(Loeschen)
            self.ErfassteWuerfe_tableWidget.setCellWidget(xx,6, Loeschen)
            Loesch_Button[xx].clicked.connect(partial(
                    self.loeschen_prog, Files[xx], xx))
        #zeige Tabelle
        self.ErfassteWuerfe_tableWidget.setHorizontalHeaderLabels(Header)
        self.ErfassteWuerfe_tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) #tabelle nicht editierbar
        # Alternierende Zeilen Fraben
        self.ErfassteWuerfe_tableWidget.setAlternatingRowColors(True)        
        self.ErfassteWuerfe_tableWidget.show()
        pass
    
    def loeschen_prog(self, Files, xx):
# =============================================================================
#         set Message Box
# =============================================================================
        message= QtWidgets.QMessageBox()
        buttonReply = message.question(self, 'Löschen', 
            "Wollen Sie diese Datei Saunummer = %s; Wurfnummer = %s wirklich löschen?" %(Files[0], Files[8]), 
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, 
            QtWidgets.QMessageBox.No)
        if buttonReply == message.Yes:
            loeschen_init = Save.loeschen_class()
            error = loeschen_init.loeschen(save_dir, Files)
#            self.Bearbeit_Button[xx].setEnabled(False)
#            self.Loesch_Button[xx].setEnabled(False)
            self.Status_Bar(error)
#            update Bearbeiten Widget
            self.Load_files()

        else:
            error = "Datei wurde nicht gelöscht"
            self.Status_Bar(error)
            pass
        pass
        
    def Load_Widgets(self,Files):
        """
        Lädt die Files/daten in die einzelnen widgets
        """
        
        
        Boolean = self.Add_Abfrage(Files)              # legt eine Neues Sau widget an
        if Boolean ==True: 
            self.SauAbfrage.Sau_Load(Files)      # lade die Daten in das Sau widget
            self.Abfrage_Widget(Files)           # Öffnet das Abfrage widget
        # self.Abfrage.SetInput(Files)          # problem with 236   # lade InputDatein               
        pass
        
                
    
            
    def Status_Bar(self, message):
        '''
        Write Information to Statursbar
        '''
        if message ==None:
            self.Main_Window.statusbar.clearMessage()
        else:
            self.Main_Window.statusbar.showMessage(message, 1000)
                    
    
    def close_request(self):
        #### verschiebe das tab an die letzte position self.Tab_count und setze den Tab an der letzten position mit dem neuen Index
        
        self.tabWidget.removeTab(1)
        # if self.tabWidget.currentIndex() >0: #only to be shure that we do not close the Main window.
            # self.tabWidget.removeTab(self.tabWidget.currentIndex()) #closes all Tabs?
            # current_Tab = self.tabWidget.currentWidget()
            # current_Tab.deleteLater()
            ### make a widget active again
            # self.Main_Window.tabWidget.setCurrentWidget(self.tabWidget.currentWidget())         #makes current widget active
            # self.Tab_count -= 1


    def Abfrage_toolbox(self,Files, count):
       """
       Generat toolbox with all Abfrage Boxes, and deaktivate the seceond and third one by default.
       Files == Datafiles
       count == number of visabel Tabs
       """
       self.tabWidget.setCurrentWidget(self.tabWidget.currentWidget())
       # toolbox= self.Main_Window.tabWidget.
       # index = self.tabWidget.currentIndex()
       # print(index)
       # tab = self.tabWidget
       # toolbox = self.tabWidget.currentWidget()
       # print("##",toolbox.whatsThis())
       
       if count == 1:
           """
           erzeugt die Toolboxes
           """
           layout = QtWidgets.QGridLayout()
           self.toolbox = QtWidgets.QToolBox()
           # self.toolbox.count()
           self.toolbox.setCurrentIndex(self.toolbox.count())        
           layout.addWidget(self.toolbox, 0,5)
        
# =============================================================================
#             öffne Sau UI
# =============================================================================
           self.Sau_widget = widget(Sau_UI)                            #lade Ui in widget
           self.SauAbfrage=SauAbf.SauAbfrage(self.Sau_widget)          #lade Abfrageprogramm
           self.toolbox.addItem(self.Sau_widget, "Sau")                #öffne widget in neuem Toolboxitem      
           self.Sau_widget.pushButton_PushSau.clicked.connect(partial(self.Abfrage_Widget, Files))
           
    # =============================================================================
    #        öffne Abfrage Widget
    # =============================================================================
    
           self.Abfrage_UI_widget = widget(Abfrage_UI)                     # lege eine neue seite an mit der UI
           self.toolbox.addItem(self.Abfrage_UI_widget, "Mütterlichkeitskarte")
           self.toolbox.setCurrentIndex(1)
           self.toolbox.setItemEnabled(1, False)
        
# =============================================================================
#       öffne Ausgabe Widget        
# =============================================================================
           # self.Ausgabe_widget = widget(Ausgabe_UI)                               # öffne Ausgabe widget
            # currentWidget.addItem(self.Ausgabe_widget, "Mütterlichkeitsindex")
            # currentWidget.setCurrentIndex(2)
           # self.toolbox.addItem(self.Ausgabe_widget, "Mütterlichkeitsindex")
           # self.toolbox.setCurrentIndex(2)
           # self.toolbox.setItemEnabled(2, False)
           
           # tab.setLayout(layout)
           self.tab1.setLayout(layout)                                 # set layout für neues tab
       
       elif count >= 2:
           """
           aktiviert Abfrge Widget 
           """
           toolbox = self.toolbox
           # toolbox = tab.setCurrentWidget(tab.widget(0))
           # toolbox = tab.setCurrentIndex(1)
           toolbox.setItemEnabled(1, True)
           toolbox.setCurrentIndex(1)
            # toolbox.currentWidget()
           
           if count ==3:
               """
               aktiviert Ausgabe Widget
               """
               # self.toolbox.setItemEnabled(2, True)
               # toolbox.setCurrentIndex(2)
               if self.cout_Ausga== 0:
                   #nur wenn noch kein Widget erstellt ist.
                   self.cout_Ausga+=1
                   self.Ausgabe_widget = widget(Ausgabe_UI)                               # öffne Ausgabe widget
                   self.toolbox.addItem(self.Ausgabe_widget, "Mütterlichkeitsindex")
                   self.toolbox.setCurrentIndex(2)
               else:
                   self.toolbox.removeItem(2)
                   self.Ausgabe_widget = widget(Ausgabe_UI)                               # öffne Ausgabe widget
                   self.toolbox.addItem(self.Ausgabe_widget, "Mütterlichkeitsindex")
                   self.toolbox.setCurrentIndex(2)
               
               pass
       
       pass


    def Add_Abfrage(self, Files = False):
        '''
        Fügt ein Abfrage Tab hinzu.
        '''
        
        
#        if self.count_AddWidget== 0:
# # =============================================================================
        if Files == False:
# #           erzeugt eine Liste mit 58 None Einträgen, wenn keine Übergeben wurde
#             Files=[None]*76
            Files = self.empty_init.empty_file()
#             
# =============================================================================
        Tab_count = self.tabWidget.count()

        self.cout_Abfr = 0              # nur ein Abfrage seite pro widget erlaubt
        self.cout_Ausga = 0             # nur ein Ausgabe seite pro widget erlaubt
#        self.count_AddWidget +=1
        

        # öffne immer nur ein Tab auf einmal!
        if Tab_count == 1:

            self.tab1 = QtWidgets.QWidget()
            self.tabWidget.addTab(self.tab1, "Neue Abfrage")        # öffne neues Tab
            # self.Main_Window.tabWidget.setCurrentIndex(self.Main_Window.tabWidget.currentIndex())
        
    # =============================================================================
    #           öffne ein neues Tab          
    # =============================================================================
            self.tabWidget.setCurrentIndex(Tab_count)                  # Vergebe eine Index für das Widget
            self.tabWidget.setTabsClosable(True)                            #closable of tab
            self.right = self.tabWidget.tabBar().RightSide                  # erzeuge eine Position für einen Button
            self.tabWidget.tabBar().setTabButton(0, self.right, None)       # mache Übersichtsfenster nicht Schließbar
            self.tabWidget.tabCloseRequested.connect(self.close_request)     # close of tab
            
            
            self.Abfrage_toolbox(Files, count =1)
    
            Dropdown_Files= self.load_init.find_files(save_dir)
            #lade SauDropdown
            self.SauAbfrage.SaudropDown(Dropdown_Files)    
    # =============================================================================
            # self.Tab_count +=1
            Add_Abfrage_boolean = True
            error = None
        else:
            error = "Bitte erst das geöffnete Tab schließen"
            message= QtWidgets.QMessageBox()
            message.question(self, 'Tab schließen', 
                "Bitte erst das geöffnete Tab schließen", 
                QtWidgets.QMessageBox.Yes)
            Add_Abfrage_boolean=False
        self.Status_Bar(error)
        return (Add_Abfrage_boolean)
        pass
    

        
    def Abfrage_Widget(self, Files):
        self.tabWidget.setCurrentWidget(self.tabWidget.currentWidget())         #makes current widget active
 ###       frage die Files ab
        Files= self.SauAbfrage.Sau_Return(Files)
# =============================================================================
#       message Box mit abfrage ob die sauangaben wirklich stimmen
#       soll nur abgefrag werden wenn die Sau wirklich neu angelegt wird
        if os.path.exists(save_dir+'%s.csv' %Files[0])==False:
            #zu dieser Sau gibts noch keine Datein, öffne meessage box
            message= QtWidgets.QMessageBox()
            buttonReply = message.question(self, 'Weiter', 
                "Nach dem Fortfahren können Sie die die Stammdaten der Sauen nicht mehr anpassen. Sind Sie sicher, dass diese stimmen?", 
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, 
                QtWidgets.QMessageBox.No)
            if buttonReply == message.Yes:
            #angaben stimmen,setze den SauMessageBox_Boolean.
#                Sau_MessagaBox = True
                SauBoolean, Files, error= self.SauAbfrage.Sau_Button(Files)
                self.Status_Bar(error)
            else:
#            #angaben Nachbearbeiten,setze den SauBoolean auf False.
                SauBoolean = False
        else:
            #Datei wurde schon angelegt,frage den SauBoolean ab.
            SauBoolean, Files, error= self.SauAbfrage.Sau_Button(Files)
            self.Status_Bar(error)
# =============================================================================
        if SauBoolean == True:
# =============================================================================
#           öffne Abfrage UI
# =============================================================================

            Tab_Index = self.tabWidget.currentIndex()            
            self.Abfrage_toolbox(Files, count =2)
            
            self.Abfrage = abfrage.Abfrage(self.Abfrage_UI_widget)               # init Abfrage
            self.Abfrage.SetInput(Files)                                         # lade InputDatei VOR Abfrage Logik          
            self.Abfrage.Widget_Logik()                                          # lade Widget Logik
            
            #### lade daten in abfrage 
            Files= self.Abfrage.Uebergabe_var()

# =============================================================================
#           changing name of Tab
# =============================================================================
            self.Main_Window.tabWidget.setTabText(Tab_Index, "%s/%s" %(Files[0], Files[8]))

            #### Save
            error = self.save_init.Save_Abfrage(save_dir, Files)

            self.Status_Bar(error)
            
#            update Bearbeiten Widget (nach dem speicher!)
            self.Load_files()


            self.Abfrage_UI_widget.pushButton_Weiter.clicked.connect(partial(
                self.Ausgabe_Widget, Files))                                    # rufe funktion auf ab wann das nächste fenster geöffnet werden darf



# =============================================================================
#            self.count_AddWidget= 0         # bereit für ein neues Widget 
# =============================================================================
                     
            pass
        pass
    def Ausgabe_Widget(self, Files):
        
        Files= self.Abfrage.Uebergabe_var()

        error = self.save_init.Save_Abfrage(save_dir, Files)
        self.Status_Bar(error)
        Abfrage_Boolean, error= self.Abfrage.Abfrage_Weiter()
        self.Status_Bar(error)
# =============================================================================
#           changing name of Tab da Wurfnummer neu dazu kommen kann.
# =============================================================================        
        self.tabWidget.setCurrentWidget(self.tabWidget.currentWidget())         #makes current widget active
        # currentWidget = self.toolbox.widget(2)
        

        # self.cout_Ausga= 0

        if Abfrage_Boolean == True:
            #berrechne Mütterlichkeits index
            Mi_Berrechnung = MI.Muetterlichkeitsindex(Files)
            Files = Mi_Berrechnung.Muttererlichkeitserfassung()
            self.Abfrage_toolbox(Files,3)            


            # Tab_Index = self.tabWidget.currentIndex()            

            Ausgabe_Logik = Ausgabe.Ausgabe(self.Ausgabe_widget)
            Ausgabe_Logik.Ausgabe_Anzeige(Files)
            error = self.save_init.Save_Abfrage(save_dir, Files)
            self.Status_Bar(error)
            
    #            update Bearbeiten Widget
            self.Load_files()                

            
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
