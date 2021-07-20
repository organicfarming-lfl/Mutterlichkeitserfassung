#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 11:03:58 2020
title           :Abfrage_v05.py
#description     :Einlesen und verarbeiten der daten des Abfrage UIs 
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
#import PyQt5.QtCore as core
#import PyQt5.QtWidgets as widgets
from PyQt5 import QtGui
#from PyQt5 import uic
from PyQt5 import QtCore
#from PyQt5 import QtWidgets
from functools import partial




class Abfrage: 
    def __init__(self, Abfrage_UI):
        self.Abfrage_Window=Abfrage_UI
        pass
    def SetInput(self, Files):
        """
        Format of File see self.Uebergabe_var
        """
        
        Einlesen= [
#             0-8
             self.Abfrage_Window.lineEdit_Saunummer,                                         #0
             self.Abfrage_Window.lineEdit_Muetterlichkeitserfassung_Rasse_Sau,               #1
             self.Abfrage_Window.lineDate_Muetterlichkeitserfassung_Geburtsdatum,            #2
             self.Abfrage_Window.lineEdit_Muetterlichkeitserfassung_NummerMutter,            #3
             self.Abfrage_Window.lineEdit_Muetterlichkeitserfassung_NummerVater,             #4
             self.Abfrage_Window.lineEdit_Muetterlichkeitserfassung_NameVater,               #5
             self.Abfrage_Window.lineEdit_Muetterlichkeitserfassung_Abstammungsnummer,       #6
             self.Abfrage_Window.lineDate_WurfDatum,                                         #7
             self.Abfrage_Window.lineEdit_Wurfnummer,                                        #8
             self.Abfrage_Window.lineEdit_Ebername,                                          #9
             self.Abfrage_Window.lineEdit_EberRasse,                                         #10
             self.Abfrage_Window.LineDate_Absetzdatum,                                       #11

             # 9-14 Ferkel leb Tot s1kg weg zug auf
             self.Abfrage_Window.lineEdit_Anzah_Ferkel_leb,                                  #12
             self.Abfrage_Window.lineEdit_Anzah_Ferkel_tot,                                  #13
             self.Abfrage_Window.lineEdit_Anzah_Ferkel_s1kg,                                 #14
             self.Abfrage_Window.lineEdit_Anzah_Ferkel_weg,                                  #15
             self.Abfrage_Window.lineEdit_Anzah_Ferkel_zug,                                  #16
             self.Abfrage_Window.lineEdit_Anzah_Ferkel_auf,                                  #17
            # 15- 19   Verluste: erd, Biss, Hung, schw, sonst
             self.Abfrage_Window.lineEdit_Anzah_Verluste_erd,                                #18
             self.Abfrage_Window.lineEdit_Anzah_Verluste_biss,                               #19
             self.Abfrage_Window.lineEdit_Anzah_Verluste_hung,                               #20
             self.Abfrage_Window.lineEdit_Anzah_Verluste_schw,                               #21
             self.Abfrage_Window.lineEdit_Anzah_Verluste_sonst,                              #22
            # 20 - 21 Anomalien Ja Nein 
             self.Abfrage_Window.checkBox_Anomaly_Ja,                                        #23
             self.Abfrage_Window.checkBox_Anomaly_Nein,                                      #24
#            22- 23 Vitaler Wurf Ja Nein
             self.Abfrage_Window.checkBox_Wurf_Vitaler_Wurf_Ja,                              #25                   
             self.Abfrage_Window.checkBox_Wurf_Vitaler_Wurf_Nein,                            #26
#           24-25 Homogener Wurf Geburt Ja Nein
             self.Abfrage_Window.checkBox_Wurf_Homogen_Geburt_Ja,                            #27
             self.Abfrage_Window.checkBox_Wurf_Homogen_Geburt_Nein,                          #28
#           26-27 Homogener Wurf (Umstallen/Absetzen Ja Nein
             self.Abfrage_Window.checkBox_Wurf_Homogen_Umstallen_Ja,                         #29
             self.Abfrage_Window.checkBox_Wurf_Homogen_Umstallen_Nein,                       #30
#           28-30 Geburtshilfe Nein, Allophatie, Manuell 
             self.Abfrage_Window.checkBox_Geburt_Geburtshilfe_Nein,                          #31
             self.Abfrage_Window.checkBox_Geburt_Geburtshilfe_Allophatie,                    #32
             self.Abfrage_Window.checkBox_Geburt_Geburtshilfe_Manuell,                       #33
#           31-32 Schwergeburt Ja Nein
             self.Abfrage_Window.checkBox_Geburt_Geburt_Schwergebrut_Ja,                     #34
             self.Abfrage_Window.checkBox_Geburt_Geburt_Schwergebrut_Nein,                   #35
#            33 - 34 Geburtsverhalten Ruhig Unruhig
             self.Abfrage_Window.checkBox_Geburt_Geburtsverhalten_Ruhig,                     #36
             self.Abfrage_Window.checkBox_Geburt_Geburtsverhalten_Unruhig,                   #37
#            35- 36 Abliegeverhalten_Vorabliegeverhalten Ja Nein
             self.Abfrage_Window.checkBox_Abliegeverhalten_Vorabliegeverhalten_Ja,           #38
             self.Abfrage_Window.checkBox_Abliegeverhalten_Vorabliegeverhalten_Nein,         #39
#            37-38 Abliegeverhalten_KontrolliertJa Nein
             self.Abfrage_Window.checkBox_Abliegeverhalten_Kontrolliertes_Abliegen_Ja,       #40
             self.Abfrage_Window.checkBox_Abliegeverhalten_Kontrolliertes_Abliegen_Nein,     #41
#            39-41         Futteraufnahme Temp_1, Tag1_Ja, Tag1_Nein, Tag2_Ja Tag2_Nein
             self.Abfrage_Window.lineEdit_Futteraufname_Temp_1,                              #42
             self.Abfrage_Window.checkBox_Futteraufname_Ja_1,                                #43
             self.Abfrage_Window.checkBox_Futteraufname_Nein_1,                              #44
#            42-44         Futteraufnahme Temp2, Tag2_Ja Tag2_Nein
             self.Abfrage_Window.lineEdit_Futteraufname_Temp_2,                              #45
             self.Abfrage_Window.checkBox_Futteraufname_Ja_2,                                #46
             self.Abfrage_Window.checkBox_Futteraufname_Nein_2,                              #47
#            45-47         Futteraufnahme Temp3, Tag3_Ja Tag3_Nein            
             self.Abfrage_Window.lineEdit_Futteraufname_Temp_3,                              #48
             self.Abfrage_Window.checkBox_Futteraufname_Ja_3,                                #49
             self.Abfrage_Window.checkBox_Futteraufname_Nein_3,                              #50
#            48- 50 Erkrankungen Nein MMA Sonst
             self.Abfrage_Window.checkBox_Futteraufname_Erkrankung_Nein,                     #51
             self.Abfrage_Window.checkBox_Futteraufname_Erkrankung_MMA,                      #52
             self.Abfrage_Window.checkBox_Futteraufname_Erkrankung_Sonst,                    #53
#           51- 53 Verteidigungsverhalten_Tag1  Nein Leicht Stark 
             self.Abfrage_Window.checkBox_Verteidigungsverahlten_Nein_1,                     #54
             self.Abfrage_Window.checkBox_Verteidigungsverahlten_Leicht_1,                   #55
             self.Abfrage_Window.checkBox_Verteidigungsverahlten_Stark_1,                    #56
#           54 -55 Verteidigungsverhalten_Tag1  Nein Leicht Stark 
             self.Abfrage_Window.checkBox_Verteidigungsverahlten_Nein_2,                     #57
             self.Abfrage_Window.checkBox_Verteidigungsverahlten_Leicht_2,                   #58
             self.Abfrage_Window.checkBox_Verteidigungsverahlten_Stark_2,                    #59
#           57-59 Verteidigungsverhalten_Tag1  Nein Leicht Stark 
             self.Abfrage_Window.checkBox_Verteidigungsverahlten_Nein_3,                     #60
             self.Abfrage_Window.checkBox_Verteidigungsverahlten_Leicht_3,                   #61
             self.Abfrage_Window.checkBox_Verteidigungsverahlten_Stark_3,                    #62
#           60 Bemerkung = ["Bermerkung", 
             self.Abfrage_Window.textEdit_Bemerkung]                                         #63
        Line_edits = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21, 22,42,45,48,63]
#        print ("####",Files)
        for xx in range(0, len(Einlesen)):# and 37 and 40 and 43 and 58):
#            print ("##", xx, Files[xx])
            if Files[xx]!= None:
                if xx in (Line_edits):
                    #set datum
                    if xx == 2 or xx ==7 or xx == 11:
                        #geburtsdatum und Wurfdatum oder Absetdatum
                        Einlesen[xx].setDate(QtCore.QDate.fromString(Files[xx], "dd.MM.yy"))
                    else:
                        Einlesen[xx].setText(str(Files[xx]))
                #schreibe checkbox
                else:
                    if Files[xx] == "True":
                        Einlesen[xx].setChecked(True)
        #deaktiviere die Sau Parameter
        for yy in range(0,7):
            Einlesen[yy].setEnabled(False)
            
    
    def Widget_Logik(self):
        """
        legt die Logik fest.
        """
#        self.Abfrage_Window = uic.loadUi(Abfrage_UI)
      
# =============================================================================
# Checkbox Uncheck Logig
# =============================================================================
#        Vitaler Wurf
        self.Abfrage_Window.checkBox_Wurf_Vitaler_Wurf_Ja.stateChanged.connect(
                partial(self.Check_Logik, 
                        self.Abfrage_Window.checkBox_Wurf_Vitaler_Wurf_Ja, 
                        self.Abfrage_Window.checkBox_Wurf_Vitaler_Wurf_Nein))
        self.Abfrage_Window.checkBox_Wurf_Vitaler_Wurf_Nein.stateChanged.connect(
                partial(self.Check_Logik, 
                        self.Abfrage_Window.checkBox_Wurf_Vitaler_Wurf_Nein, 
                        self.Abfrage_Window.checkBox_Wurf_Vitaler_Wurf_Ja))
#        Homogener Wurf Geburt
        self.Abfrage_Window.checkBox_Wurf_Homogen_Geburt_Ja.stateChanged.connect(
                partial(self.Check_Logik, 
                     self.Abfrage_Window.checkBox_Wurf_Homogen_Geburt_Ja, 
                     self.Abfrage_Window.checkBox_Wurf_Homogen_Geburt_Nein))
        self.Abfrage_Window.checkBox_Wurf_Homogen_Geburt_Nein.stateChanged.connect(
            partial(self.Check_Logik, 
                     self.Abfrage_Window.checkBox_Wurf_Homogen_Geburt_Nein, 
                     self.Abfrage_Window.checkBox_Wurf_Homogen_Geburt_Ja))
#        Homogener Wurf Umstall
        self.Abfrage_Window.checkBox_Wurf_Homogen_Umstallen_Ja.stateChanged.connect(
                partial(self.Check_Logik, 
                     self.Abfrage_Window.checkBox_Wurf_Homogen_Umstallen_Ja, 
                     self.Abfrage_Window.checkBox_Wurf_Homogen_Umstallen_Nein))
        self.Abfrage_Window.checkBox_Wurf_Homogen_Umstallen_Nein.stateChanged.connect(
                partial(self.Check_Logik, 
                     self.Abfrage_Window.checkBox_Wurf_Homogen_Umstallen_Nein, 
                     self.Abfrage_Window.checkBox_Wurf_Homogen_Umstallen_Ja))
#        Geburtshilfe
        self.Abfrage_Window.checkBox_Geburt_Geburtshilfe_Nein.stateChanged.connect(
                partial(self.Check_Logik, 
                     self.Abfrage_Window.checkBox_Geburt_Geburtshilfe_Nein, 
                     self.Abfrage_Window.checkBox_Geburt_Geburtshilfe_Allophatie,
                     self.Abfrage_Window.checkBox_Geburt_Geburtshilfe_Manuell))
        
        self.Abfrage_Window.checkBox_Geburt_Geburtshilfe_Allophatie.stateChanged.connect(
                partial(self.Check_Logik, 
                     self.Abfrage_Window.checkBox_Geburt_Geburtshilfe_Allophatie, 
                     self.Abfrage_Window.checkBox_Geburt_Geburtshilfe_Nein))
                
        self.Abfrage_Window.checkBox_Geburt_Geburtshilfe_Manuell.stateChanged.connect(
                partial(self.Check_Logik, 
                     self.Abfrage_Window.checkBox_Geburt_Geburtshilfe_Manuell, 
                     self.Abfrage_Window.checkBox_Geburt_Geburtshilfe_Nein))
#        Schwergeburt        
        self.Abfrage_Window.checkBox_Geburt_Geburt_Schwergebrut_Ja.stateChanged.connect(
            partial(self.Check_Logik, 
                     self.Abfrage_Window.checkBox_Geburt_Geburt_Schwergebrut_Ja, 
                     self.Abfrage_Window.checkBox_Geburt_Geburt_Schwergebrut_Nein))
        self.Abfrage_Window.checkBox_Geburt_Geburt_Schwergebrut_Nein.stateChanged.connect(
            partial(self.Check_Logik, 
                     self.Abfrage_Window.checkBox_Geburt_Geburt_Schwergebrut_Nein, 
                     self.Abfrage_Window.checkBox_Geburt_Geburt_Schwergebrut_Ja))
#        Geburtsverhalten
        self.Abfrage_Window.checkBox_Geburt_Geburtsverhalten_Ruhig.stateChanged.connect(
            partial(self.Check_Logik, 
                 self.Abfrage_Window.checkBox_Geburt_Geburtsverhalten_Ruhig, 
                 self.Abfrage_Window.checkBox_Geburt_Geburtsverhalten_Unruhig))
        
        self.Abfrage_Window.checkBox_Geburt_Geburtsverhalten_Unruhig.stateChanged.connect(
            partial(self.Check_Logik, 
                     self.Abfrage_Window.checkBox_Geburt_Geburtsverhalten_Unruhig, 
                     self.Abfrage_Window.checkBox_Geburt_Geburtsverhalten_Ruhig))
#            Vorabliegeverhalten
        self.Abfrage_Window.checkBox_Abliegeverhalten_Vorabliegeverhalten_Ja.stateChanged.connect(
            partial(self.Check_Logik, 
                 self.Abfrage_Window.checkBox_Abliegeverhalten_Vorabliegeverhalten_Ja, 
                 self.Abfrage_Window.checkBox_Abliegeverhalten_Vorabliegeverhalten_Nein))
        self.Abfrage_Window.checkBox_Abliegeverhalten_Vorabliegeverhalten_Nein.stateChanged.connect(
            partial(self.Check_Logik, 
                 self.Abfrage_Window.checkBox_Abliegeverhalten_Vorabliegeverhalten_Nein, 
                 self.Abfrage_Window.checkBox_Abliegeverhalten_Vorabliegeverhalten_Ja))
#            Kontrolliertes Vorabliegeverhalten
        self.Abfrage_Window.checkBox_Abliegeverhalten_Kontrolliertes_Abliegen_Ja.stateChanged.connect(
                partial(self.Check_Logik, 
                        self.Abfrage_Window.checkBox_Abliegeverhalten_Kontrolliertes_Abliegen_Ja, 
                        self.Abfrage_Window.checkBox_Abliegeverhalten_Kontrolliertes_Abliegen_Nein))
        self.Abfrage_Window.checkBox_Abliegeverhalten_Kontrolliertes_Abliegen_Nein.stateChanged.connect(
                partial(self.Check_Logik, 
                        self.Abfrage_Window.checkBox_Abliegeverhalten_Kontrolliertes_Abliegen_Nein, 
                        self.Abfrage_Window.checkBox_Abliegeverhalten_Kontrolliertes_Abliegen_Ja))
#            Futteraufnahme_1
        self.Abfrage_Window.checkBox_Futteraufname_Ja_1.stateChanged.connect(
                partial(self.Check_Logik, 
                        self.Abfrage_Window.checkBox_Futteraufname_Ja_1, 
                        self.Abfrage_Window.checkBox_Futteraufname_Nein_1))
        self.Abfrage_Window.checkBox_Futteraufname_Nein_1.stateChanged.connect(
                partial(self.Check_Logik, 
                        self.Abfrage_Window.checkBox_Futteraufname_Nein_1, 
                        self.Abfrage_Window.checkBox_Futteraufname_Ja_1))
#        Futteraufnhme_2
        self.Abfrage_Window.checkBox_Futteraufname_Ja_2.stateChanged.connect(
                partial(self.Check_Logik, 
                        self.Abfrage_Window.checkBox_Futteraufname_Ja_2, 
                        self.Abfrage_Window.checkBox_Futteraufname_Nein_2))
        self.Abfrage_Window.checkBox_Futteraufname_Nein_2.stateChanged.connect(
                partial(self.Check_Logik, 
                        self.Abfrage_Window.checkBox_Futteraufname_Nein_2, 
                        self.Abfrage_Window.checkBox_Futteraufname_Ja_2))
#            Futteraufnahem 3
        self.Abfrage_Window.checkBox_Futteraufname_Ja_3.stateChanged.connect(
                partial(self.Check_Logik, 
                        self.Abfrage_Window.checkBox_Futteraufname_Ja_3, 
                        self.Abfrage_Window.checkBox_Futteraufname_Nein_3))
        self.Abfrage_Window.checkBox_Futteraufname_Nein_3.stateChanged.connect(
                partial(self.Check_Logik, 
                        self.Abfrage_Window.checkBox_Futteraufname_Nein_3, 
                        self.Abfrage_Window.checkBox_Futteraufname_Ja_3))
#        Erkrankung
        self.Abfrage_Window.checkBox_Futteraufname_Erkrankung_Nein.stateChanged.connect(
                partial(self.Check_Logik, 
                        self.Abfrage_Window.checkBox_Futteraufname_Erkrankung_Nein, 
                        self.Abfrage_Window.checkBox_Futteraufname_Erkrankung_MMA, 
                        self.Abfrage_Window.checkBox_Futteraufname_Erkrankung_Sonst))
        
        self.Abfrage_Window.checkBox_Futteraufname_Erkrankung_MMA.stateChanged.connect(
                partial(self.Check_Logik, 
                        self.Abfrage_Window.checkBox_Futteraufname_Erkrankung_MMA, 
                        self.Abfrage_Window.checkBox_Futteraufname_Erkrankung_Nein))
        self.Abfrage_Window.checkBox_Futteraufname_Erkrankung_Sonst.stateChanged.connect(
                partial(self.Check_Logik, 
                        self.Abfrage_Window.checkBox_Futteraufname_Erkrankung_Sonst, 
                        self.Abfrage_Window.checkBox_Futteraufname_Erkrankung_Nein))
        
#        Verteidigungsverhalten _1
        self.Abfrage_Window.checkBox_Verteidigungsverahlten_Nein_1.stateChanged.connect(
                partial(self.Check_Logik, 
                        self.Abfrage_Window.checkBox_Verteidigungsverahlten_Nein_1, 
                        self.Abfrage_Window.checkBox_Verteidigungsverahlten_Leicht_1, 
                        self.Abfrage_Window.checkBox_Verteidigungsverahlten_Stark_1))
        self.Abfrage_Window.checkBox_Verteidigungsverahlten_Leicht_1.stateChanged.connect(
                partial(self.Check_Logik, 
                        self.Abfrage_Window.checkBox_Verteidigungsverahlten_Leicht_1, 
                        self.Abfrage_Window.checkBox_Verteidigungsverahlten_Nein_1, 
                        self.Abfrage_Window.checkBox_Verteidigungsverahlten_Stark_1))
        self.Abfrage_Window.checkBox_Verteidigungsverahlten_Stark_1.stateChanged.connect(
                partial(self.Check_Logik, 
                        self.Abfrage_Window.checkBox_Verteidigungsverahlten_Stark_1, 
                        self.Abfrage_Window.checkBox_Verteidigungsverahlten_Nein_1, 
                        self.Abfrage_Window.checkBox_Verteidigungsverahlten_Leicht_1))
#        Verteidigungsverhalten _2
        self.Abfrage_Window.checkBox_Verteidigungsverahlten_Nein_2.stateChanged.connect(
                partial(self.Check_Logik, 
                        self.Abfrage_Window.checkBox_Verteidigungsverahlten_Nein_2, 
                        self.Abfrage_Window.checkBox_Verteidigungsverahlten_Leicht_2, 
                        self.Abfrage_Window.checkBox_Verteidigungsverahlten_Stark_2))
        self.Abfrage_Window.checkBox_Verteidigungsverahlten_Leicht_2.stateChanged.connect(
                partial(self.Check_Logik, 
                        self.Abfrage_Window.checkBox_Verteidigungsverahlten_Leicht_2, 
                        self.Abfrage_Window.checkBox_Verteidigungsverahlten_Nein_2, 
                        self.Abfrage_Window.checkBox_Verteidigungsverahlten_Stark_2))
        self.Abfrage_Window.checkBox_Verteidigungsverahlten_Stark_2.stateChanged.connect(
                partial(self.Check_Logik, 
                        self.Abfrage_Window.checkBox_Verteidigungsverahlten_Stark_2, 
                        self.Abfrage_Window.checkBox_Verteidigungsverahlten_Nein_2, 
                        self.Abfrage_Window.checkBox_Verteidigungsverahlten_Leicht_2))
#        Verteidigungsverhalten _3
        self.Abfrage_Window.checkBox_Verteidigungsverahlten_Nein_3.stateChanged.connect(
                partial(self.Check_Logik, 
                        self.Abfrage_Window.checkBox_Verteidigungsverahlten_Nein_3, 
                        self.Abfrage_Window.checkBox_Verteidigungsverahlten_Leicht_3, 
                        self.Abfrage_Window.checkBox_Verteidigungsverahlten_Stark_3))
        self.Abfrage_Window.checkBox_Verteidigungsverahlten_Leicht_3.stateChanged.connect(
                partial(self.Check_Logik, 
                        self.Abfrage_Window.checkBox_Verteidigungsverahlten_Leicht_3, 
                        self.Abfrage_Window.checkBox_Verteidigungsverahlten_Nein_3, 
                        self.Abfrage_Window.checkBox_Verteidigungsverahlten_Stark_3))
        self.Abfrage_Window.checkBox_Verteidigungsverahlten_Stark_3.stateChanged.connect(
                partial(self.Check_Logik, 
                        self.Abfrage_Window.checkBox_Verteidigungsverahlten_Stark_3, 
                        self.Abfrage_Window.checkBox_Verteidigungsverahlten_Nein_3, 
                        self.Abfrage_Window.checkBox_Verteidigungsverahlten_Leicht_3))
        
# =============================================================================
#         Anomalie
# =============================================================================
        self.Abfrage_Window.checkBox_Anomaly_Ja.stateChanged.connect(
                partial(self.Check_Logik, self.Abfrage_Window.checkBox_Anomaly_Ja,
                        self.Abfrage_Window.checkBox_Anomaly_Nein))
        
        self.Abfrage_Window.checkBox_Anomaly_Nein.stateChanged.connect(
                partial(self.Check_Logik, self.Abfrage_Window.checkBox_Anomaly_Nein,
                        self.Abfrage_Window.checkBox_Anomaly_Ja))

        


        # Integer eingabe
        maxialer_Intergerwert = 100
        minimaler_Intergerwert = 0
#        Decimals_Integerwert = 0


# =============================================================================
#       Wurfnummer
# =============================================================================
        self.Abfrage_Window.lineEdit_Wurfnummer.setValidator(
                QtGui.QIntValidator(minimaler_Intergerwert,maxialer_Intergerwert))

 
# =============================================================================
#         anzahl ferkel
# =============================================================================       
        
        #Anzahl Ferkel
        self.Abfrage_Window.lineEdit_Anzah_Ferkel_leb.setValidator(
                QtGui.QIntValidator(minimaler_Intergerwert,maxialer_Intergerwert))
        self.Abfrage_Window.lineEdit_Anzah_Ferkel_tot.setValidator(
                QtGui.QIntValidator(minimaler_Intergerwert,maxialer_Intergerwert))
        self.Abfrage_Window.lineEdit_Anzah_Ferkel_s1kg.setValidator(
                QtGui.QIntValidator(minimaler_Intergerwert,maxialer_Intergerwert))
        self.Abfrage_Window.lineEdit_Anzah_Ferkel_weg.setValidator(
                QtGui.QIntValidator(minimaler_Intergerwert,maxialer_Intergerwert))
        self.Abfrage_Window.lineEdit_Anzah_Ferkel_zug.setValidator(
                QtGui.QIntValidator(minimaler_Intergerwert,maxialer_Intergerwert))
        self.Abfrage_Window.lineEdit_Anzah_Ferkel_auf.setValidator(
                QtGui.QIntValidator(minimaler_Intergerwert,maxialer_Intergerwert))

# =============================================================================
#         Verluste
# =============================================================================
        self.Abfrage_Window.lineEdit_Anzah_Verluste_erd.setValidator(
                QtGui.QIntValidator(0,maxialer_Intergerwert))
        self.Abfrage_Window.lineEdit_Anzah_Verluste_biss.setValidator(
                QtGui.QIntValidator(0,maxialer_Intergerwert))
        self.Abfrage_Window.lineEdit_Anzah_Verluste_hung.setValidator(
                QtGui.QIntValidator(0,maxialer_Intergerwert))
        self.Abfrage_Window.lineEdit_Anzah_Verluste_schw.setValidator(
                QtGui.QIntValidator(0,maxialer_Intergerwert))
        self.Abfrage_Window.lineEdit_Anzah_Verluste_sonst.setValidator(
                QtGui.QIntValidator(0,maxialer_Intergerwert))
# =============================================================================
#         Temperatur
# =============================================================================
        Mint_Temp = 35.0
        Max_Temp = 45.0
        Decimals_Temp = 2
        self.Abfrage_Window.lineEdit_Futteraufname_Temp_1.setValidator(
                QtGui.QDoubleValidator(Mint_Temp,Max_Temp, Decimals_Temp))
        self.Abfrage_Window.lineEdit_Futteraufname_Temp_2.setValidator(
                QtGui.QDoubleValidator(Mint_Temp,Max_Temp, Decimals_Temp))
        self.Abfrage_Window.lineEdit_Futteraufname_Temp_3.setValidator(
                QtGui.QDoubleValidator(Mint_Temp,Max_Temp, Decimals_Temp))
        
        # Datum Forma
#         lineDate_Muetterlichkeitserfassung_Geburtsdatum
# lineDate_WurfDatum 
# LineDate_Absetzdatum
        self.Date_format ="dd.MM.yy"        

        self.Abfrage_Window.lineDate_Muetterlichkeitserfassung_Geburtsdatum.setDisplayFormat(self.Date_format)
        
        self.Abfrage_Window.lineDate_WurfDatum.setDisplayFormat(self.Date_format)
        
        self.Abfrage_Window.LineDate_Absetzdatum.setDisplayFormat(self.Date_format)

        pass
    
# =============================================================================
#         Date    
# =============================================================================


# =============================================================================
#         Logik das nur integer in Anzahl Ferkel... eingegeben werden können    
# =============================================================================
    
#    def Clear_Logik(self, Check, Clear_1, Clear_2, )    
    
    def Check_Logik(self, Check, Uncheck_1,Uncheck_2 = "None", Uncheck_3 = "None"):
        """
        setzt die Uncheck logik für die Checkboxen mit meheren Abhängigen Checkboxen
        """
        if Check.isChecked():
            Uncheck_1.setChecked(False)
            if Uncheck_2 != "None" and type(Uncheck_2) != int :
                Uncheck_2.setChecked(False)
            if Uncheck_3 != "None" and type(Uncheck_3) != int:
                Uncheck_3.setChecked(False)
        pass

    
    def Abfrage_Weiter(self):
        """
        wenn Pflichtfelder ausgefüllt sind dann wird im hauptprogramm das nächste widget gefüllt.
        """        
        #### Fitness ist ein Pflicht feld.
        
        Abfrage_Boolean = False
        Datum_Boolena = False
        
        # check if leb + zug - weg - erd - biss - schw - sonst = auf is fullfilled        
        #check if text field is filled
        if self.Abfrage_Window.lineEdit_Anzah_Ferkel_leb.text() =="":
            Anzah_Ferkel_leb = 0
        else:
            Anzah_Ferkel_leb = int(
                    self.Abfrage_Window.lineEdit_Anzah_Ferkel_leb.text())
            pass
        #zuge
        if self.Abfrage_Window.lineEdit_Anzah_Ferkel_zug.text() =="":
            Anzah_Ferkel_zug = 0
        else:
            Anzah_Ferkel_zug = int(
                    self.Abfrage_Window.lineEdit_Anzah_Ferkel_zug.text())
            pass
        #weg
        if self.Abfrage_Window.lineEdit_Anzah_Ferkel_weg.text() =="":
            Anzah_Ferkel_weg = 0
        else:
            Anzah_Ferkel_weg = int(
                    self.Abfrage_Window.lineEdit_Anzah_Ferkel_weg.text())
            pass
        #erdrückt
        if self.Abfrage_Window.lineEdit_Anzah_Verluste_erd.text() =="":
            Anzah_Verluste_erd = 0
        else:
            Anzah_Verluste_erd = int(
                    self.Abfrage_Window.lineEdit_Anzah_Verluste_erd.text())
            pass
        #biss
        if self.Abfrage_Window.lineEdit_Anzah_Verluste_biss.text() =="":
            Anzah_Verluste_biss = 0
        else:
            Anzah_Verluste_biss = int(
                    self.Abfrage_Window.lineEdit_Anzah_Verluste_biss.text())
            pass
        #hunger
        if self.Abfrage_Window.lineEdit_Anzah_Verluste_hung.text() =="":
            Anzah_Verluste_hung = 0
        else:
            Anzah_Verluste_hung = int(
                    self.Abfrage_Window.lineEdit_Anzah_Verluste_hung.text())
            pass
        #Schw
        if self.Abfrage_Window.lineEdit_Anzah_Verluste_schw.text() =="":
            Anzah_Verluste_schw = 0
        else:
            Anzah_Verluste_schw = int(
                    self.Abfrage_Window.lineEdit_Anzah_Verluste_schw.text())
            pass
        #sonst
        if self.Abfrage_Window.lineEdit_Anzah_Verluste_sonst.text() =="":
            Anzah_Verluste_sonst = 0
        else:
            Anzah_Verluste_sonst = int(
                    self.Abfrage_Window.lineEdit_Anzah_Verluste_sonst.text())
            pass
        if self.Abfrage_Window.lineEdit_Anzah_Ferkel_auf.text() =="":
            Anzah_Ferkel_auf = 0
        else:
            Anzah_Ferkel_auf = int(
                    self.Abfrage_Window.lineEdit_Anzah_Ferkel_auf.text())
            pass
        
        Ferkel = (Anzah_Ferkel_leb +Anzah_Ferkel_zug-Anzah_Ferkel_weg-
        Anzah_Verluste_erd-Anzah_Verluste_biss-Anzah_Verluste_hung-
        Anzah_Verluste_schw-Anzah_Verluste_sonst)

# =============================================================================
#       Wurfdatum und Wurfnummer abfrage
# =============================================================================
        # print(self.Abfrage_Window.lineDate_WurfDatum.date().toString(self.Date_format))
        # self.Abfrage_Window.lineDate_WurfDatum.setDisplayFormat("dd.mm.yy")
        
        
        # if self.Abfrage_Window.lineDate_WurfDatum.text()!="01.01.00":
        if self.Abfrage_Window.lineDate_WurfDatum.date().toString(self.Date_format)!="01.01.00":
            if self.Abfrage_Window.lineEdit_Wurfnummer.text() != "":
                self.Abfrage_Window.lineEdit_Wurfnummer.setStyleSheet(
                    "background-color: white")
                error = None
                Datum_Boolena = True
            else:
                self.Abfrage_Window.lineEdit_Wurfnummer.setStyleSheet(
                     "background-color: yellow; border: 1px solid black;")
                error = "Bitte Wurfnummer Eingeben"
                Datum_Boolena = False
                
        elif self.Abfrage_Window.lineDate_WurfDatum.date().toString(self.Date_format)=="01.01.00":
        # elif self.Abfrage_Window.lineDate_WurfDatum.text()=="01.01.00":
            self.Abfrage_Window.lineDate_WurfDatum.setStyleSheet(
                     "background-color: yellow; border: 1px solid black;")
#                error = "Bitte Wurfnummer Eingeben"
            Datum_Boolena = False
            if self.Abfrage_Window.lineEdit_Wurfnummer.text() != "":
                self.Abfrage_Window.lineEdit_Wurfnummer.setStyleSheet(
                "background-color: white")
                error = "Bitte Wurfdatum Eingeben"
            else:
                self.Abfrage_Window.lineEdit_Wurfnummer.setStyleSheet(
                     "background-color: yellow; border: 1px solid black;")
                error = "Bitte Wurfdatum und Wurfnummer Eingeben"
            
        elif self.Abfrage_Window.lineEdit_Wurfnummer.text() != "":
            self.Abfrage_Window.lineEdit_Wurfnummer.setStyleSheet(
                "background-color: white")
            error = None
            Datum_Boolena = True
        else:
            self.Abfrage_Window.lineEdit_Wurfnummer.setStyleSheet(
                 "background-color: yellow; border: 1px solid black;")
            error = "Bitte Wurfnummer Eingeben"
            Datum_Boolena = False
#            error = None
#        else:
#            #color fields
#            Datum_Boolena = False
#            self.Abfrage_Window.lineDate_WurfDatum.setStyleSheet(
#                    "background-color: yellow; border: 1px solid black;")
#            error = "Bitte Wurfnummer Eingeben"

        if Ferkel ==Anzah_Ferkel_auf and Anzah_Ferkel_auf!=0:
            Abfrage_Boolean = True
            # felder korrekt ausgefüllt
            #return default color
            self.Abfrage_Window.lineEdit_Anzah_Ferkel_leb.setStyleSheet(
                    "background-color: white")
            self.Abfrage_Window.lineEdit_Anzah_Ferkel_zug.setStyleSheet(
                    "background-color: white")
            self.Abfrage_Window.lineEdit_Anzah_Ferkel_weg.setStyleSheet(
                    "background-color: white")
            self.Abfrage_Window.lineEdit_Anzah_Verluste_erd.setStyleSheet(
                    "background-color: white")
            self.Abfrage_Window.lineEdit_Anzah_Verluste_biss.setStyleSheet(
                    "background-color: white")
            self.Abfrage_Window.lineEdit_Anzah_Verluste_hung.setStyleSheet(
                    "background-color: white")
            self.Abfrage_Window.lineEdit_Anzah_Verluste_schw.setStyleSheet(
                    "background-color: white")
            self.Abfrage_Window.lineEdit_Anzah_Verluste_sonst.setStyleSheet(
                    "background-color: white")
            self.Abfrage_Window.lineEdit_Anzah_Ferkel_auf.setStyleSheet(
                    "background-color: white") 
            error=None
        else:
            #color fields
            self.Abfrage_Window.lineEdit_Anzah_Ferkel_leb.setStyleSheet(
                    "background-color: yellow; border: 1px solid black;")
            self.Abfrage_Window.lineEdit_Anzah_Ferkel_zug.setStyleSheet(
                    "background-color: yellow; border: 1px solid black;")
            self.Abfrage_Window.lineEdit_Anzah_Ferkel_weg.setStyleSheet(
                    "background-color: yellow; border: 1px solid black;")
            self.Abfrage_Window.lineEdit_Anzah_Verluste_erd.setStyleSheet(
                    "background-color: yellow; border: 1px solid black;")
            self.Abfrage_Window.lineEdit_Anzah_Verluste_biss.setStyleSheet(
                    "background-color: yellow; border: 1px solid black;")
            self.Abfrage_Window.lineEdit_Anzah_Verluste_hung.setStyleSheet(
                    "background-color: yellow; border: 1px solid black;")
            self.Abfrage_Window.lineEdit_Anzah_Verluste_schw.setStyleSheet(
                    "background-color: yellow; border: 1px solid black;")
            self.Abfrage_Window.lineEdit_Anzah_Verluste_sonst.setStyleSheet(
                    "background-color: yellow; border: 1px solid black;")
            self.Abfrage_Window.lineEdit_Anzah_Ferkel_auf.setStyleSheet(
                    "background-color: yellow; border: 1px solid black;")
            Abfrage_Boolean = False
            error = "Abfrage felder nicht richtig ausgefüllt, leb + zug - weg - erd - biss - schw - sonst = auf; %i = %i" %(Ferkel, Anzah_Ferkel_auf)
        if Abfrage_Boolean==True and Datum_Boolena==True:
            return (True, error)
        else:
            if error == None: 
                error = "Bitte füllen sie die markierten Felder aus"
            return (False, error)
            
    
    def Uebergabe_var(self):
        """
        erzeugt ein liste mit allen UI werten in der form 

        """
        
        Files = [ # 0-8 Saunummer, Rasse Sau, Geburtsdatu,, NummerMutter, NummerVater, NameVater, Abstammungsnummer
             self.Abfrage_Window.lineEdit_Saunummer.text(),                                         #0
             self.Abfrage_Window.lineEdit_Muetterlichkeitserfassung_Rasse_Sau.text(),               #1
             self.Abfrage_Window.lineDate_Muetterlichkeitserfassung_Geburtsdatum.date().toString(self.Date_format),#2
             # self.Abfrage_Window.lineDate_Muetterlichkeitserfassung_Geburtsdatum.text(),            #2
             self.Abfrage_Window.lineEdit_Muetterlichkeitserfassung_NummerMutter.text(),            #3
             self.Abfrage_Window.lineEdit_Muetterlichkeitserfassung_NummerVater.text(),             #4
             self.Abfrage_Window.lineEdit_Muetterlichkeitserfassung_NameVater.text(),               #5
             self.Abfrage_Window.lineEdit_Muetterlichkeitserfassung_Abstammungsnummer.text(),       #6
             self.Abfrage_Window.lineDate_WurfDatum.date().toString(self.Date_format),              #7
             # self.Abfrage_Window.lineDate_WurfDatum.text(),                                       #7
             self.Abfrage_Window.lineEdit_Wurfnummer.text(),                                        #8
             self.Abfrage_Window.lineEdit_Ebername.text(),                                          #9
             self.Abfrage_Window.lineEdit_EberRasse.text(),                                         #10
             self.Abfrage_Window.LineDate_Absetzdatum.date().toString(self.Date_format),            #11
             # self.Abfrage_Window.LineDate_Absetzdatum.text(),                                     #11

#           9-14 Ferkel leb Tot s1kg weg zug auf
             self.Abfrage_Window.lineEdit_Anzah_Ferkel_leb.text(),                                  #12
             self.Abfrage_Window.lineEdit_Anzah_Ferkel_tot.text(),                                  #13
             self.Abfrage_Window.lineEdit_Anzah_Ferkel_s1kg.text(),                                 #14
             self.Abfrage_Window.lineEdit_Anzah_Ferkel_weg.text(),                                  #15
             self.Abfrage_Window.lineEdit_Anzah_Ferkel_zug.text(),                                  #16
             self.Abfrage_Window.lineEdit_Anzah_Ferkel_auf.text(),                                  #17
#           15-19   Verluste: erd, Biss, Hung, schw, sonst
             self.Abfrage_Window.lineEdit_Anzah_Verluste_erd.text(),                                #18
             self.Abfrage_Window.lineEdit_Anzah_Verluste_biss.text(),                               #19
             self.Abfrage_Window.lineEdit_Anzah_Verluste_hung.text(),                               #20
             self.Abfrage_Window.lineEdit_Anzah_Verluste_schw.text(),                               #21
             self.Abfrage_Window.lineEdit_Anzah_Verluste_sonst.text(),                              #22
#           20-21  Anomalien Ja Nein 
             self.Abfrage_Window.checkBox_Anomaly_Ja.isChecked(),                                   #23
             self.Abfrage_Window.checkBox_Anomaly_Nein.isChecked(),                                 #24
#           22- 23 Vitaler Wurf Ja Nein
             self.Abfrage_Window.checkBox_Wurf_Vitaler_Wurf_Ja.isChecked(),                         #25                   
             self.Abfrage_Window.checkBox_Wurf_Vitaler_Wurf_Nein.isChecked(),                       #26
#           24-25 Homogener Wurf Geburt Ja Nein
             self.Abfrage_Window.checkBox_Wurf_Homogen_Geburt_Ja.isChecked(),                       #27
             self.Abfrage_Window.checkBox_Wurf_Homogen_Geburt_Nein.isChecked(),                     #28
#           26-27 Homogener Wurf (Umstallen/Absetzen Ja Nein
             self.Abfrage_Window.checkBox_Wurf_Homogen_Umstallen_Ja.isChecked(),                    #29
             self.Abfrage_Window.checkBox_Wurf_Homogen_Umstallen_Nein.isChecked(),                  #30
#           28-30 Geburtshilfe Nein, Allophatie, Manuell 
             self.Abfrage_Window.checkBox_Geburt_Geburtshilfe_Nein.isChecked(),                     #31
             self.Abfrage_Window.checkBox_Geburt_Geburtshilfe_Allophatie.isChecked(),               #32
             self.Abfrage_Window.checkBox_Geburt_Geburtshilfe_Manuell.isChecked(),                  #33
#           31-32 Schwergeburt Ja Nein
             self.Abfrage_Window.checkBox_Geburt_Geburt_Schwergebrut_Ja.isChecked(),                #34
             self.Abfrage_Window.checkBox_Geburt_Geburt_Schwergebrut_Nein.isChecked(),              #35
#           33-34 Geburtsverhalten Ruhig Unruhig
             self.Abfrage_Window.checkBox_Geburt_Geburtsverhalten_Ruhig.isChecked(),                #36
             self.Abfrage_Window.checkBox_Geburt_Geburtsverhalten_Unruhig.isChecked(),              #37
#           35-36 Abliegeverhalten_Vorabliegeverhalten Ja Nein
             self.Abfrage_Window.checkBox_Abliegeverhalten_Vorabliegeverhalten_Ja.isChecked(),      #38
             self.Abfrage_Window.checkBox_Abliegeverhalten_Vorabliegeverhalten_Nein.isChecked(),    #39
#           37-38 Abliegeverhalten_KontrolliertJa Nein
             self.Abfrage_Window.checkBox_Abliegeverhalten_Kontrolliertes_Abliegen_Ja.isChecked(),  #40
             self.Abfrage_Window.checkBox_Abliegeverhalten_Kontrolliertes_Abliegen_Nein.isChecked(),#41
#            39-41         Futteraufnahme Temp_1, Tag1_Ja, Tag1_Nein, Tag2_Ja Tag2_Nein
             self.Abfrage_Window.lineEdit_Futteraufname_Temp_1.text(),                              #42
             self.Abfrage_Window.checkBox_Futteraufname_Ja_1.isChecked(),                           #43
             self.Abfrage_Window.checkBox_Futteraufname_Nein_1.isChecked(),                         #44
#            42-44         Futteraufnahme Temp2, Tag2_Ja Tag2_Nein
             self.Abfrage_Window.lineEdit_Futteraufname_Temp_2.text(),                              #45
             self.Abfrage_Window.checkBox_Futteraufname_Ja_2.isChecked(),                           #46
             self.Abfrage_Window.checkBox_Futteraufname_Nein_2.isChecked(),                         #47
#            45-47         Futteraufnahme Temp3, Tag3_Ja Tag3_Nein            
             self.Abfrage_Window.lineEdit_Futteraufname_Temp_3.text(),                              #48
             self.Abfrage_Window.checkBox_Futteraufname_Ja_3.isChecked(),                           #49
             self.Abfrage_Window.checkBox_Futteraufname_Nein_3.isChecked(),                         #50
#             48- 50 Erkrankungen Nein MMA Sonst
             self.Abfrage_Window.checkBox_Futteraufname_Erkrankung_Nein.isChecked(),                #51
             self.Abfrage_Window.checkBox_Futteraufname_Erkrankung_MMA.isChecked(),                 #52
             self.Abfrage_Window.checkBox_Futteraufname_Erkrankung_Sonst.isChecked(),               #53
#           51- 53 Verteidigungsverhalten_Tag1  Nein Leicht Stark 
             self.Abfrage_Window.checkBox_Verteidigungsverahlten_Nein_1.isChecked(),                #54
             self.Abfrage_Window.checkBox_Verteidigungsverahlten_Leicht_1.isChecked(),              #55
             self.Abfrage_Window.checkBox_Verteidigungsverahlten_Stark_1.isChecked(),               #56
#           54 -56 Verteidigungsverhalten_Tag1  Nein Leicht Stark 
             self.Abfrage_Window.checkBox_Verteidigungsverahlten_Nein_2.isChecked(),                #57
             self.Abfrage_Window.checkBox_Verteidigungsverahlten_Leicht_2.isChecked(),              #58
             self.Abfrage_Window.checkBox_Verteidigungsverahlten_Stark_2.isChecked(),               #59
#           57-59 Verteidigungsverhalten_Tag1  Nein Leicht Stark 
             self.Abfrage_Window.checkBox_Verteidigungsverahlten_Nein_3.isChecked(),                #60
             self.Abfrage_Window.checkBox_Verteidigungsverahlten_Leicht_3.isChecked(),              #61
             self.Abfrage_Window.checkBox_Verteidigungsverahlten_Stark_3.isChecked(),               #62
#           60 Bemerkung = ["Bermerkung", 
             self.Abfrage_Window.textEdit_Bemerkung.toPlainText()]                                  #63

        return(Files)
        