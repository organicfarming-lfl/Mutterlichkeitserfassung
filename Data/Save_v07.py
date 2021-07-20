#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 16:11:42 2020

title           :Save_v07.py
description     :Save and Load files
author          :Jonas Müller
e-mail          :Mueller.M.Jonas@gmx.de
date            :13.04.2021
version         :00.07
usage           :python pyscript.py
notes           :
python_version  :3.7.3
"""


from PyQt5 import QtCore
#import PyQt5.QtWidgets as widgets
#import PyQt5.QtGui as gui
#import PyQt5.uic as uic
import csv
import os
# import datetime 
# import pandas as pd
# from dateutil.parser import parse
# import arrow
#import numpy as np

class loeschen_class:
    def __init__(self):
        pass
    def loeschen(self, Path, loesch_inhalt):
        # find zu löschende Zeile
        Files = []
        with open(Path +'%s.csv' %loesch_inhalt[0], "r", newline='', encoding='utf-8' ) as csvfile:
            csv_reader = csv.reader(csvfile)        # load files
            header = next(csv_reader)               # skip the heder of every file
            if header != None:
                for row in csv_reader:              #iterate over all rows
                    Files.append(row)
                    
        if len(Files)==1:
            os.remove(Path +'%s.csv' %loesch_inhalt[0]) 
            error = "Datei wurde Gelöscht"
            
        else:
            length = len(Files)
            for qq in range((length)):
                #vergleiche Saunummer[1], Wurfdatum[7] und Wurfnummer [8]
                vergleich = Files[qq]
                if vergleich[0] == loesch_inhalt[0] and vergleich[7] == loesch_inhalt[7] and vergleich[8] == loesch_inhalt[8]:
                    Files.pop(qq)
                    break
                
            
            if len(Files) == length:
                error = "Löschen Fehlgeschlagen"
            if len(Files) != length:
                #lösche den Datensatz
                os.remove(Path +'%s.csv' %loesch_inhalt[0])
                #schreibe ihn Neu
                # init Save
                Save_init = save()
                #schreiben den ersten eintrag
                Save_init.Save_Abfrage(Path, Files[0])
                for zz in range(1, len(Files)):
                    Save_init.Datei_exist(Path, Files[zz])
                error ="Löschen des Datensatzes war erfolgreich"            
                pass
        return (error)

class load:
    def __init__(self):
        pass
    def find_files(self, Path):
        '''
        finds all files in the folder Path and return the loaded files 
        '''
        
#        Files = ['Saunummer', 'Sau Rasse', 'Geburtsdatum', 'Nummer Mutter Sau', 'Nummer Vater Sau', 'Name Vater Sau', 'Abstammungsnummer']   # header manuell filled
        Files=[]
        for filename in os.listdir(Path):
            with open(Path +filename, "r", newline='', encoding='utf-8') as csvfile:
                csv_reader = csv.reader(csvfile)        # load files
                header = next(csv_reader)               # skip the heder of every file
                if header != None:
                    for row in csv_reader:              #iterate over all rows
                        Files.append(row)
                        
        #transform date to required format dd.mm.yy
        for kk in range(len(Files)):
            eingelesen = Files[kk]
            date_format = "dd.MM.yy"
            for date in (2, 7,11):
                # eingelesen[date] = parse(eingelesen[date]).strftime(format)
                # eingelesen[date] = QtCore.QDate.fromString(eingelesen[date], date_format).toString(date_format)
                # aa = QtCore.QDate.fromString(eingelesen[date], date_format)
                # print("##", QtCore.QDate.fromString(eingelesen[date], date_format).toString(date_format))
                eingelesen[date] = QtCore.QDate.fromString(eingelesen[date], date_format).toString(date_format)
                
                # eingelesen[date] = pd.to_datetime((eingelesen[date]))
                # eingelesen[date] = str(eingelesen[date].strftime(date_format))
                
                # eingelesen[date] = datetime.datetime.strptime(eingelesen[date], format).strftime(format)
                # print(ts)
                
            #     print (eingelesen[date])
            Files[kk] = eingelesen
        return(Files)
        
    
class save:
    
    def __init__(self):
        """
        Erzeugt einen Header für alle Save files

        Returns
        -------
        None.

        """ 
        self.file_Header = self.Header()

        
        
    def Header(self):
        
# =============================================================================
        file_Header = [
                      # 0-8 Saunummer, Rasse Sau, Geburtsdatu,, NummerMutter, NummerVater, NameVater, Abstammungsnummer
                       'Saunummer',                             #0
                       'Sau Rasse',                             #1
                       'Geburtsdatum',                          #2
                       'Nummer Mutter Sau',                     #3
                       'Nummer Vater Sau',                      #4
                       'Name Vater Sau',                        #5
                       'Abstammungsnummer',                     #6
                       'Wurf Datum',                            #7
                       'Wurfnummer',                            #8
                       'Ebername',                              #9
                       'Eber Rasse',                            #10
                       'Absetzdatum',                           #11
                       # 9-14 Ferkel leb Tot s1kg weg zug auf
                       'Anzahl Ferkel Lebend',                  #12
                       'Anzahl Ferkel Tot',                     #13
                       'Anzahl Ferkel Weniger 1kG',             #14
                       'Anzahl Ferkel Weggegeben',              #15
                       'Anzahl Ferkel Hinzu gezogen',           #16
                       'Anzahl Ferkel Aufgezogen',              #17
                       # 15- 19   Verluste: erd, Biss, Hung, schw, sonst
                       'Anzahl Verluste erdrückt',              #18
                       'Anzahl Verluste Biss',                  #19
                       'Anzahl Verluste verhungert',            #20
                       'Anzahl Verluste Schwach',               #21
                       'Anzahl verluste sonst',                 #22        
                       # 20 - 21 Anomalien Ja Nein 
                       'Anomalien Ja',                          #23
                       'Anomalien Nein',                        #24
                       # 22- 23 Vitaler Wurf Ja Nein
                       'Vitaler Wurf Ja',                       #25
                       'Vitaler Wurf Nein',                     #26
                       # 24-25 Homogener Wurf Geburt Ja Nein
                       'Homogener Wurf Ja',                     #27
                       'Homogeber Wurf Nein',                   #28
                       # 26-27 Homogener Wurf (Umstallen/Absetzen Ja Nein
                       'Homogener Wurf Absetzen Ja',            #29
                       'Homogener Wurf Absetzen Nein',          #30
                       # 28-30 Geburtshilfe Nein, Allophatie, Manuell 
                       'Geburtshilfe Nein',                     #31
                       'Geburtshilfe Allopathie',               #32
                       'Geburtshilfe Manuell',                  #33
                       # 31-32 Schwergeburt Ja Nein
                       'Schwergeburt Ja',                       #34
                       'Schwergeburt Nein',                     #35
                       # 33 - 34 Geburtsverhalten Ruhig Unruhig
                       'Geburtsverhalten Ruhig',                #36
                       'Geburtsverhalten Unruhig',              #37
                       # 35- 36 Abliegeverhalten_Vorabliegeverhalten Ja Nein
                       'Vorabliegeverhalten Ja',                #38
                       'Vorabliegeverhalten Nein',              #39
                       # 37 - 38 Abliegeverhalten_KontrolliertJa Nein
                       'Kontrolliertes Abliegevarhelten Ja',    #40
                       'Kontrolliertes Abliegeverhalten Nein',  #41
                       # 39-41 Futteraufnahme Temp_1, Tag1_Ja, Tag1_Nein
                       'Temperatur Tag1',                       #42
                       'Futteraufnahme Tag 1 Ja',               #43
                       'Futteraufnahme Tag 1 Nein',             #44
                       # 42-44 Futteraufnahme Temp_2, Tag2_Ja, Tag2_Nein
                       'Temperatur Tag2',                       #45
                       'Futteraufnahme Tag 2 Ja',               #46
                       'Futteraufnahme Tag 2 Nein',             #47
                       # 45-47 Futteraufnahme Temp_3, Tag3_Ja, Tag3_Nein
                       'Temperatur Tag3',                       #48
                       'Futteraufnahme Tag 3 Ja',               #49
                       'Futteraufnahme Tag 3 Nein',             #50
                       # 48- 50 Erkrankungen Nein MMA Sonst
                       'Erkrankung Nein',                       #51
                       'Erkrankung MMA',                        #52
                       'Erkrankung Sonst',                      #53
                       # 51- 53 Verteidigungsverhalten_Tag1  Nein Leicht Stark 
                       'Verteidigungsverhalten Tag1 Nein',      #54
                       'Verteidigungsverhalten Tag1 Leicht',    #55
                       'Verteidigungsverhalten Tag1 Stark',     #56
                       # 54- 56 Verteidigungsverhalten_Tag2  Nein Leicht Stark 
                       'Verteidigungsverhalten Tag2 Nein',      #57
                       'Verteidigungsverhalten Tag2 Leicht',    #58
                       'Verteidigungsverhalten Tag2 Stark',     #59
                       # 57- 59 Verteidigungsverhalten_Tag3  Nein Leicht Stark 
                       'Verteidigungsverhalten Tag3 Nein',      #60
                       'Verteidigungsverhalten Tag3 Leicht',    #61
                       'Verteidigungsverhalten Tag3 Stark',     #62
                       #Bemerkung
                       'Bemerkung',                             #63
                       #60-65 Berechnung
                       'Leistung',                              #64
                       'Geburt',                                #65
                       'Wurf',                                  #66
                       'Fitness',                               #67
                       'Abliegeverhalten',                      #68
                       'Umgaenglichkeit',                       #69
                       #66-71 Gewichtung 
                       'Leistugs Gewichtung',                   #70
                       'Geburt Gewichtung',                     #71
                       'Wurf Gewichtung',                       #72
                       'Fitness Gewichtung',                    #73
                       'Ableigeverhalten Gewichtung',           #74
                       'Umgaenglichkeit Gewichtung',            #75
                       #Mütterlichkeitsindex
                       'Muetterlichkeitsindex',                 #76
                       ]
        return (file_Header)
    
    def Writer(self, Data):
        '''
        write  
        '''
        #transform date to required format dd.mm.yy
        date_format = "dd.MM.yy"
        for date in (2, 7,11):
            # Data[date] = parse(Data[date]).strftime(format)
            # Data[date] = datetime.datetime.strptime(Data[date], format).strftime(format)
            # Data[date] = pd.to_datetime((Data[date]))
            # Data[date] = str(Data[date].strftime(format))
            Data[date]=QtCore.QDate.fromString(Data[date] , date_format).toString(date_format)

        
        self.writer.writerow({
        'Saunummer':                             Data[0],
        'Sau Rasse':                             Data[1],                        
        'Geburtsdatum':                          Data[2],                     
        'Nummer Mutter Sau':                     Data[3],                
        'Nummer Vater Sau':                      Data[4],                 
        'Name Vater Sau':                        Data[5],                    
        'Abstammungsnummer':                     Data[6],
        'Wurf Datum':                            Data[7],
        'Wurfnummer':                            Data[8],
        'Ebername':                              Data[9],
        'Eber Rasse':                            Data[10],
        'Absetzdatum':                           Data[11],             
# 8-13 Ferkel leb Tot s1kg weg zug auf
        'Anzahl Ferkel Lebend':                  Data[12],              
        'Anzahl Ferkel Tot':                     Data[13],                
        'Anzahl Ferkel Weniger 1kG':             Data[14],         
        'Anzahl Ferkel Weggegeben':              Data[15],
        'Anzahl Ferkel Hinzu gezogen':           Data[16],
        'Anzahl Ferkel Aufgezogen':              Data[17],
# 14- 18   Verluste: erd, Biss, Hung, schw, sonst
        'Anzahl Verluste erdrückt':              Data[18],
        'Anzahl Verluste Biss':                  Data[19],              
        'Anzahl Verluste verhungert':            Data[20],
        'Anzahl Verluste Schwach':               Data[21],
        'Anzahl verluste sonst':                 Data[22],                 
#                       # 19 - 20 Anomalien Ja Nein 
        'Anomalien Ja':                          Data[23],                      
        'Anomalien Nein':                        Data[24],                    
# 21- 22 Vitaler Wurf Ja Nein
        'Vitaler Wurf Ja':                       Data[25],                   
        'Vitaler Wurf Nein':                     Data[26],                 
# 23-24 Homogener Wurf Geburt Ja Nein
        'Homogener Wurf Ja':                     Data[27],                 
        'Homogeber Wurf Nein':                   Data[28],               
# 25-26 Homogener Wurf (Umstallen/Absetzen Ja Nein
        'Homogener Wurf Absetzen Ja':            Data[29],        
        'Homogener Wurf Absetzen Nein':          Data[30],      
# 27-29 Geburtshilfe Nein, Allophatie, Manuell 
        'Geburtshilfe Nein':                     Data[31],                 
        'Geburtshilfe Allopathie':               Data[32],           
        'Geburtshilfe Manuell':                  Data[33],             
# 30-31 Schwergeburt Ja Nein
        'Schwergeburt Ja':                       Data[34],                 
        'Schwergeburt Nein':                     Data[35],                 
# 32 - 33 Geburtsverhalten Ruhig Unruhig
        'Geburtsverhalten Ruhig':                Data[36],          
        'Geburtsverhalten Unruhig':              Data[37],         
# 34- 35 Abliegeverhalten_Vorabliegeverhalten Ja Nein
        'Vorabliegeverhalten Ja':                Data[38],            
        'Vorabliegeverhalten Nein':              Data[39],          
# 36 - 37 Abliegeverhalten_KontrolliertJa Nein
        'Kontrolliertes Abliegevarhelten Ja':    Data[40],
        'Kontrolliertes Abliegeverhalten Nein':  Data[41],
# 38-40 Futteraufnahme Temp_1, Tag1_Ja, Tag1_Nein
        'Temperatur Tag1':                       Data[42],                 
        'Futteraufnahme Tag 1 Ja':               Data[43],          
        'Futteraufnahme Tag 1 Nein':             Data[44],        
# 41-43 Futteraufnahme Temp_2, Tag2_Ja, Tag2_Nein
        'Temperatur Tag2':                       Data[45],                   
        'Futteraufnahme Tag 2 Ja':               Data[46],           
        'Futteraufnahme Tag 2 Nein':             Data[47],         
# 44-46 Futteraufnahme Temp_3, Tag3_Ja, Tag3_Nein
        'Temperatur Tag3':                       Data[48],                 
        'Futteraufnahme Tag 3 Ja':               Data[49],           
        'Futteraufnahme Tag 3 Nein':             Data[50],         
# 47- 49 Erkrankungen Nein MMA Sonst
        'Erkrankung Nein':                       Data[51],                   
        'Erkrankung MMA':                        Data[52],                   
        'Erkrankung Sonst':                      Data[53],
# 50- 52 Verteidigungsverhalten_Tag1  Nein Leicht Stark 
        'Verteidigungsverhalten Tag1 Nein':      Data[54], 
        'Verteidigungsverhalten Tag1 Leicht':    Data[55],
        'Verteidigungsverhalten Tag1 Stark':     Data[56], 
# 53- 55 Verteidigungsverhalten_Tag2  Nein Leicht Stark 
        'Verteidigungsverhalten Tag2 Nein':      Data[57],  
        'Verteidigungsverhalten Tag2 Leicht':    Data[58],
        'Verteidigungsverhalten Tag2 Stark':     Data[59],
# 56- 59 Verteidigungsverhalten_Tag3  Nein Leicht Stark
        'Verteidigungsverhalten Tag3 Nein':      Data[60], 
        'Verteidigungsverhalten Tag3 Leicht':    Data[61],
        'Verteidigungsverhalten Tag3 Stark':     Data[62], 
        'Bemerkung':                             Data[63],
#60-65 Mütterlichkeitsindex
        'Leistung':                              Data[64],
        'Geburt':                                Data[65],  
        'Wurf':                                  Data[66],
        'Fitness':                               Data[67],
        'Abliegeverhalten':                      Data[68],
        'Umgaenglichkeit':                       Data[69],       
# 70-75 Gewichtung
        'Leistugs Gewichtung':                   Data[70],
        'Geburt Gewichtung':                     Data[71],
        'Wurf Gewichtung':                       Data[72],  
        'Fitness Gewichtung':                    Data[73],
        'Ableigeverhalten Gewichtung':           Data[74],     
        'Umgaenglichkeit Gewichtung':            Data[75],
#Mütterlichkeitsindex
        'Muetterlichkeitsindex':                 Data[76]})
        
    
    def Save_Abfrage(self, Path, Data):
        '''speichert die Aktuelle Datein in eine Datei mit dem Namen der Saunummer Datei[0] unter dem Pfad
        '''
# =============================================================================
#        mache die Data Liste und file_Header gleich Lang indem an die Data liste lauter Nones angefügt werden
        if len(Data)!= len(self.file_Header):
            for xx in range(len(Data), len(self.file_Header)):
                Data.append(None)
# =============================================================================
        
# =============================================================================
#         checke ob die datei schon existiert
# =============================================================================
#        if (Data[0]!=None):
        if os.path.exists(Path+'%s.csv' %Data[0])==True:
            #datei existiert
            error = self.Datei_exist(Path, Data)

        if os.path.exists(Path+'%s.csv' %Data[0])== False:
            #datei existiert noch nicht und wird nun erstellt 
            with open(Path+'%s.csv' %Data[0], 'w', newline='', encoding='utf-8') as csvfile:
                csv.register_dialect("custom", delimiter=" ", skipinitialspace=True)
                self.writer = csv.DictWriter(csvfile, dialect='excel',  fieldnames=self.file_Header)
                self.writer.writeheader()
                self.Writer(Data)
            error = "Datein Gespeichert"
        return (error)
        pass
    
    def Datei_exist(self,Path, Data):
        #Data sind die Übergeben daten
        existing_files = []
        gesuchte_reihe = []
        #checken ob die datei überhaupt neue Informationen hat 
        if Data[7] =="01.01.00" or (Data[8]== None or Data[8]==""):
            error = "Fehler! Dateine wurden noch nicht gespeichert"
        if (Data[7] !="01.01.00" and (Data[8]!= None or Data[8]=="")):
            #lese die existierend Datein ein
            with open(Path+'%s.csv' %Data[0], "r", newline='', encoding='utf-8') as csvfile:
                csv_reader = csv.reader(csvfile)        # load files
                header = next(csv_reader)               # skip the heder of every file
                if header != None:
                    for row in csv_reader:              #iterate over all rows
                        existing_files.append(row)
# =============================================================================
#                 vergleiche die Datein
#                        finde die gleiche datei (für das Laden wichtig!)
# =============================================================================
            for qq in range(len(existing_files)):
                data_set = existing_files[qq]

# =============================================================================
#                 vergleiche datensatz mit den neuen daten
#                 der unterschied der Datensätzen soll in der Wurfnummer [7] und Wurfdatum[8] festgelegt werden
#                 leere datensätze sollen überschrieben werden 
# =============================================================================
                if (data_set[7]== "01.01.00" or data_set[7]=="" and (data_set[8]==""or 
                                                                     data_set[8]==None or data_set[8]=="0") or 
                    ((data_set[7]==Data[7]) and (data_set[8]== Data[8]))) :
                # if ((data_set[7]==Data[7]) and (data_set[8]== Data[8]) or (Data[7]== "01.01.00" and (Data[8]=="" or Data[8]==None))):
                    gesuchte_reihe.append( qq) # übergibt welche Reihennummer überschrieben werden soll
                    
                    uebergabe = []
                    for zz in range(len(data_set)):
                        
                        #überprüfe ob neue information in den dateine stecken
                        if Data[zz]!=data_set[zz]:
                            if Data[zz]== None and data_set[zz]!= None:
                                #checke ob was in dem Datensatz steht -- Wenn der alte und neue Leer sind dann nimm den "Alten"
                                uebergabe.append(data_set[zz])
                            else: 
                                #-- wenn der Datensatz nicht leer ist übernimm diesen
                                uebergabe.append(Data[zz])
                        else :
                            uebergabe.append(Data[zz])
                        pass                    
                    break
                    
                        #sucht nach leeren einträgen oder nach der zu überschreibenden Zeile

# =============================================================================
#                 schreibe neue Datenen in datensatz
# =============================================================================
            with open(Path+'%s.csv' %Data[0], 'w', newline='', encoding='utf-8') as csvfile:
                csv.register_dialect("custom", delimiter=" ", skipinitialspace=True)
                self.writer = csv.DictWriter(csvfile, dialect='excel',  fieldnames=self.file_Header)
                self.writer.writeheader()
# =============================================================================
#               unterscheide ob eine Reihe ersetzt werden muss oder ob 
#               eine neue reihe angehängt werden muss
# =============================================================================
                if len(gesuchte_reihe)!=0:
                    #ersetzen einer Reihe mit den Neuen Daten
                    for kk in range (len(existing_files)):
                        data_set = existing_files[kk]   
                        if kk != gesuchte_reihe[0]:
                            self.Writer(data_set)
                        else:
                            self.Writer(uebergabe)
                else:
                    #append new line
                    #vorher haben wir bereits gecheckt ob es leere einträge gibt die wir überschreiben können
                    for kk in range (len(existing_files)):
#                Schreibe die Datein wieder in das File                          
                        self.Writer(existing_files[kk])
#                Füge die Neue datei hinzu
                    #checke das die datein aber schon ausgefüllt sind 
                    self.Writer(Data)
#            gesuchte_reihe = None
                error = "Datein Gespeichert"

                    
        return (error)
                    
                
class  File():
    def __init__(self):
        pass
    def empty_file(self):
        save_init = save()
        File_length = len(save_init.Header())
        File = [None]*(File_length)
        return File
        
        