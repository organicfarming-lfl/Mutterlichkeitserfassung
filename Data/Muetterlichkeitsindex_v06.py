# -*- coding: utf-8 -*-

"""
Created on Sat Apr 11 20:31:03 2020
title           :Muetterlichkeitsindex_v05.py
description     :Berrechnen des Muetterlichkeitsindex
author          :Jonas Müller
e-mail          :Mueller.M.Jonas@gmx.de
date            :13.04.2021
version         :00.05
usage           :python pyscript.py
notes           :
python_version  :3.7.3

"""

# =============================================================================
# Muetterlichkeitsindex
# =============================================================================

#import sys
#import os
#GuI Libs
#import PyQt5.QtCore as core
#from PyQt5 import QtWidgets
#from PyQt5 import QtGui
#from PyQt5 import uic


#from functools import partial

#current_dir = os.path.dirname(os.path.abspath(__file__))
#program_dir = current_dir+"/Data/"
#sys.path.insert(1,program_dir)
# Own modules
#from {path} import {class}
#import Abfrage as abfrage



#UI_dir = current_dir+"/UI/"




class Muetterlichkeitsindex:
    
#    def __init__(self, Abfrage_UI):
    def __init__(self, Uebergabe_var):
        """
        Einlesen der datein
        es wir die Saunummer, wurfnummer benötigt
        wird es? 
        """
        
        self.Files = Uebergabe_var
# =============================================================================
#         Format Files
# =============================================================================
#                                  
        pass
    
    def Muttererlichkeitserfassung(self):
        """
        File[nummer] Siehe Save_v...py
        ruft die funktionen auf und speichert sie in der Uebergabe_var
                       'Leistung',                          #64
                       'Geburt',                            #65
                       'Wurf',                              #66
                       'Fitness',                           #67
                       'Abliegeverhalten',                  #68
                       'Umgaenglichkeit',                   #69
        """
        self.rounddigit= 2
        self.List = [self.MutterID_Leistung(), self.MutterID_Geburtsverhalten(), self.MutterID_Wurf(),
                self.MutterID_Fitness(), self.MutterID_Abliegeverhalten(), self.MutterID_Umgaenglichkeit()]
        for yy in range(len(self.List)):
            #schreibe die Einträge in die Files.
            xx = yy+64
            self.Files[xx] = self.List[yy]
            pass
        #letzter eintrag
        self.Files[76] = self.Muetterlichkeitsindex()
        # return files
        return (self.Files)
    def Muetterlichkeitsindex(self):
        
#        List = [self.MutterID_Leistung(), self.MutterID_Geburtsverhalten(), self.MutterID_Wurf(),
#        self.MutterID_Fitness(), self.MutterID_Abliegeverhalten(), self.MutterID_Umgaenglichkeit()]
        Muetterlichkeitsindex = 0
        for qq in range (len(self.List)):   #Gewichtung aus dem Datei Format, von File
            Gewichtung = 70+qq
            if self.Files[Gewichtung] == None:
                self.Files[Gewichtung] = 1/6
                Muetterlichkeitsindex = Muetterlichkeitsindex + self.List[qq]*self.Files[Gewichtung]
            else:
                Muetterlichkeitsindex = Muetterlichkeitsindex + self.List[qq]*self.Files[Gewichtung]
                pass
            pass
        return str(int(round(Muetterlichkeitsindex, self.rounddigit)))
        

    def MutterID_Leistung(self):
        """
        File[nummer] Siehe Save_v...py
        zählt 39 % zum mütterlichkeitsindex
        leistung = auf*auf/ (leb+zug-weg)
        Leistung = (Aufgezogene Ferkel[17])**2 /(Leben gebohren Ferkel[12] + 
                                                 zugesetzte Ferkel[16] - wegversetzte Ferkel[15])
        y = auf^2/(leb+zug-weg) 
        y <= 4 -> rot -> 0 Punkte Punkte;
        4 < y <= 5 -> rot -> 1 Punkte;
        5 < y <= 6 -> rot -> 2 Punkte;
        6 < y <= 7 -> rot -> 3 Punkte;
        7 < y <= 8 -> gelb -> 4 Punkte;
        8 < y <= 9 -> gelb -> 5 Punkte;
        9 < y <= 10 -> gelb -> 6 Punkte; 
        10 < y <= 11 -> gelb -> 7 Punkte;
        11 < y <= 12 -> grün -> 8 Punkte;
        12 < y <= 13 -> grün -> 9 Punkte;
        y > 13 -> grün -> 10 Punkte;
        
        """
# =============================================================================
#         setze daten auf null wenn nichts eingetragen wurde
# =============================================================================
        # if (self.Files[17]== "" and 
        # self.Files[12] == ""and 
        # self.Files[16] == "" and
        # self.Files[15]== ""):
        #     Leistung =0
            # self.error = "aufgezogen, Lebend gebohren, Wegegeben und Zugezogen nicht vollständig ausgefüllt"
        if (self.Files[12] == ""and 
        self.Files[16] == "" and
        self.Files[15]== ""):
            Leistung = 0
            self.error = "aufgezogen, Lebend gebohren, Wegegeben und Zugezogen nicht vollständig ausgefüllt"
        if (int(self.Files[12])+int(self.Files[12])-int(self.Files[12]) ==0):
            Leistung = 0
            self.error = "Lebend gebohren - Wegegeben + Zugezogen = 0"
        else: 
            
            ID_Leistung = int(self.Files[17])**2/(
                    int(self.Files[12])+
                    int(self.Files[16])-
                    int(self.Files[15]))
            if ID_Leistung <= 4:
                Leistung = 0 
            if (ID_Leistung >4 and ID_Leistung <=5):
                Leistung = 1
            if (ID_Leistung >5 and ID_Leistung <=6):
                Leistung = 2
            if (ID_Leistung >6 and ID_Leistung <=7):
                Leistung = 3
            if (ID_Leistung >7 and ID_Leistung <=8):
                Leistung = 4
            if (ID_Leistung >8 and ID_Leistung <=9):
                Leistung = 5 
            if (ID_Leistung >9 and ID_Leistung <=10):
                Leistung = 6
            if (ID_Leistung >10 and ID_Leistung <=11):
                Leistung = 7 
            if (ID_Leistung >11 and ID_Leistung <=12):
                Leistung = 8
            if (ID_Leistung >12 and ID_Leistung <=13):
                Leistung = 9
            if (ID_Leistung >13):
                Leistung = 10
                pass
            self.error = None
#        print("leistung = ",Leistung)
        return round(Leistung, self.rounddigit)
        pass


    def MutterID_Geburtsverhalten(self):
        """
File[nummer] Siehe Save_v...py
#        Geburtshilfe[31](nein) + Geburtsverhalten[36] (normal) =        Note 1 ==10
                    #... Geburtshilfe = nein & Geburstverhalten = ruhig-> 10 Punkte -> grün
#        Geburtshilfe[31](nein) + Geburtsverhalten[37] (nervös) =        Note 2 ==20/3
                    #... Geburtshilfe = nein & Geburstverhalten = unruhig-> 20/3 Punkte -> gelb
#        Geburtshilfe([32]Medizin) + Geburtsverhalten[36] (normal) =     Note 2 ==20/3
                    #... Geburtshilfe = Allopathie & Geburstverhalten = ruhig-> 20/3 Punkte -> gelb
#        Geburtshilfe([33]Manuell) + Geburtsverhalten[36] (normal) =     Note 3 ==10/3
                    #... Geburtshilfe = manuell & Geburstverhalten = ruhig-> 10/3 Punkte -> gelb
#        Geburtshilfe([32]Medizin) + Geburtsverhalten[37] (nervös) =     Note 3 ==10/3
                    #... Geburtshilfe = Allopathie & Geburstverhalten = unruhig-> 10/3 Punkte -> gelb
#        Geburtshilfe([33]Manuell) + Geburtsverhalten[37] (nervös) =     Note 4 ==0
                    #... Geburtshilfe = manuell & Geburstverhalten = unruhig-> 0 Punkte -> rot
#        Geburtshilfe([32]Medizin und [35]Manuell) + Geburtsverhalten[36] (normal) = Note 3 ==10/3
                    #... Geburtshilfe = Allopathie+manuell & Geburstverhalten = ruhig-> 10/3 Punkte -> gelb
#        Geburtshilfe([32]Medizin und [33]Manuell) + Geburtsverhalten[37] (nervös) = Note 4 ==0
                    #... Geburtshilfe = Allopathie+manuell  & Geburstverhalten = unruhig-> 0 Punkte -> rot
#        Geburtshilfe[34](Schwergeburt) + Geburtsverhalten[36] (normal) = Note 4 ==0
                    #... Geburtshilfe = Allopathie+manuell  & Geburstverhalten = unruhig-> 0 Punkte -> rot
#        Geburtshilfe[34](Schwergeburt) + Geburtsverhalten[37] (Nervös) = Note 4 ==0
                    #... Geburtshilfe = Allopathie+manuell  & Geburstverhalten = unruhig-> 0 Punkte -> rot
        """
        
        if self.Files[35] == True:              # keine Schwergeburt
#... Geburtshilfe = nein & Geburstverhalten = ruhig-> 10 Punkte -> grün
            if (self.Files[31] == True          #keine Geburtshilfe
                and self.Files[36] == True):     #Ruhig
                Geburts_Wert = 10
                pass
#... Geburtshilfe = nein & Geburstverhalten = unruhig-> 20/3 Punkte -> gelb
            elif (self.Files[31] == True        # keine Geburtshilfee
                and self.Files[37] == True):    #unruhig
                Geburts_Wert = 20/3
                pass
#... Geburtshilfe = Allopathie & Geburstverhalten = ruhig-> 20/3 Punkte -> gelb
            elif (self.Files[32] == True     #medizin
                and self.Files[33] == False   # keine Manuele Hilfe
                and self.Files[36] == True):    #normales Geburtsverhalten
                Geburts_Wert = 20/3
                pass
#... Geburtshilfe = manuell & Geburstverhalten = ruhig-> 10/3 Punkte -> gelb
            elif (self.Files[33] == True        #manuell
                and self.Files[32] == False     #keine Medizin
                and self.Files[36] == True):    #ruig
                Geburts_Wert = 10/3
                pass     
#... Geburtshilfe = Allopathie & Geburstverhalten = unruhig-> 10/3 Punkte -> gelb
            elif (self.Files[32] == True                # Medizin
                and self.Files[33] == False             # keine Manuelle hilfe
                and self.Files[37] == True):            #nervös
                Geburts_Wert = 10/3
                pass
#... Geburtshilfe = manuell & Geburstverhalten = unruhig-> 0 Punkte -> rot
            elif (self.Files[32] == False                #keine Medizin
                and self.Files[33] == True              #Manuelle Hilfe
                and self.Files[37] == True):             #nervös
                Geburts_Wert = 0
                pass
#... Geburtshilfe = Allopathie+manuell & Geburstverhalten = ruhig-> 10/3 Punkte -> gelb
            elif (self.Files[32] == True                #Medizin
                and self.Files[33] == True              #Manuell
                and self.Files[36] == True):            #Ruhig
                Geburts_Wert = 10/3
                pass
#... Geburtshilfe = Allopathie+manuell  & Geburstverhalten = unruhig-> 0 Punkte -> rot
            elif (self.Files[32] == True                #Manuell
                and self.Files[33] == True              #Medizin
                and self.Files[37] == True):            #unruhig
                Geburts_Wert = 0
                pass

            else:
                Geburts_Wert = 0
                
            pass

        elif self.Files[34] == True:                    #Schwergeburt
            Geburts_Wert = 0
            
            pass
        else:
            Geburts_Wert = 0
        self.error = None
        return round(Geburts_Wert, self.rounddigit)
   
    def MutterID_Wurf(self):
        """
        File[nummer] Siehe Save_v...py
        vitaler Wurf[25] und Hmogener Wurf [27]=            Note 1 == 10
            vital = ja & homogen = ja  -> grün -> 10 Punkte
        entweder Vitaler Wurf [25]oder Homogener Wurf[27] = Note 2 == 5
            vital = nein & homogen = ja  -> gelb -> 5 Punkte
            vital = ja & homogen = nein  -> gelb -> 5 Punkte
        werder Vitaler noch Homogener Wurf =        Note 3 == 0
            vital = nein & homogen = nein  -> rot -> 0 Punkte
         
        """
#vital = ja & homogen = ja  -> grün -> 10 Punkte
        if (self.Files[25] == True and      #Vitaler Wurf Ja
            self.Files[27] == True):        # Homogener Wurf Ja
            Wurfqualitaet = 10
            pass
#vital = nein & homogen = ja  -> gelb -> 5 Punkte
#vital = ja & homogen = nein  -> gelb -> 5 Punkte

        elif (self.Files[25] == True or   # Vitaer Wurf Ja 
            self.Files[27] == True):    # Homogener Wurf Ja
            Wurfqualitaet = 5
            pass
#vital = nein & homogen = nein  -> rot -> 0 Punkte
        else:
            Wurfqualitaet = 0
            pass
        self.error = None
        return round(Wurfqualitaet, self.rounddigit)

    def MutterID_Fitness(self):
        """
        MMA = nein & …
        … max. 1-mal Temp > 39,5 & max. 1-mal Futteraufnahme = nein -> grün -> 10 Punkte 
        … mehr als 1-mal Temp > 39,5 & max. 1-mal Futteraufnahme = nein -> gelb -> 5 Punkte 
        … max. 1-mal Temp > 39,5 & mehr als 1-mal Futteraufnahme = nein -> gelb -> 5 Punkte 
        … mehr als 1-mal Temp > 39,5 &  mehr als 1-mal Futteraufnahme = nein -> rot -> 0 Punkte 
        MMA = ja -> rot -> 0 Punkte
        """ 
        
        if ((self.Files[43] or self.Files[44]) ==True and         #check ob Futteraufnahme Tag1 Ja/Nein angehakelt wurde
            (self.Files[46] or self.Files[47]) == True and        #check ob Futteraufnahme Tag2 Ja/Nein angehakelt wurde
            (self.Files[49] or self.Files[50]) == True and        #check ob Futteraufnahme Tag3 Ja/Nein angehakelt wurde
            not self.Files[42] == "" and                         # check ob Temp Tag1 eingetragen wurde
            not self.Files[45] == "" and                         # check ob Temp Tag2 eingetragen wurde
            not self.Files[48] == ""):                           # check ob Temp Tag3 eingetragen wurde
            Temp395 = 0
            Futter_Nein=0
            for xx in (self.Files[42],self.Files[45], self.Files[48]):
                #berechne # Temp >= 39.5
#                if float(xx.replace(',','.')) >=39.5:
                if float(xx .replace(',','.')) >=39.5:
                    Temp395+= 1
                    pass
#            print (Temp395)
            for yy in (self.Files[44],self.Files[47], self.Files[50]):
                #berechne # Futteraufnahem Nein 
                if yy == True:
                    Futter_Nein += 1
                    pass
                pass
            pass
        else:
            Temp395 = 3
            Futter_Nein=3
            self.error = "Futteraufnahem oder Temperatur nicht vollständig ausgefüllt"
            pass
        if self.Files[52] == True:
#            Erkrankung MMA
#            MMA = ja -> rot -> 0 Punkte         
            Fitness = 0
        elif self.Files[51] == True:
            #Erkrankung MMA Nein
            if (Temp395 <= 1 and Futter_Nein <= 1):
                #… max. 1-mal Temp > 39,5 & max. 1-mal Futteraufnahme = nein -> grün -> 10 Punkte 
                Fitness = 10
                pass
            elif (Temp395 >= 1 and Futter_Nein <= 1):
                #… mehr als 1-mal Temp > 39,5 & max. 1-mal Futteraufnahme = nein -> gelb -> 5 Punkte 
                Fitness = 5
                pass
            elif (Temp395 <= 1 and Futter_Nein >= 1):
                #… max. 1-mal Temp > 39,5 & mehr als 1-mal Futteraufnahme = nein -> gelb -> 5 Punkte 
                Fitness = 5
                pass
            elif (Temp395 > 1 and Futter_Nein > 1):
                #… mehr als 1-mal Temp > 39,5 &  mehr als 1-mal Futteraufnahme = nein -> rot -> 0 Punkte 
                Fitness = 0
                pass 
            pass
        else: 
            Fitness = 0
        return round(Fitness, self.rounddigit)
    
    def MutterID_Abliegeverhalten(self):
        """
        File[nummer] Siehe Save_v...py
Voabliegeverhalten[38] = ja & kontrolliertes Abliegen[40] = ja  -> grün -> 10 Punkte
Voabliegeverhalten[39] = nein & kontrolliertes Abliegen[40] = ja  -> gelb -> 5 Punkte
Voabliegeverhalten[38] = ja & kontrolliertes Abliegen[41] = nein  -> gelb -> 5 Punkte
Voabliegeverhalten[39] = nein & kontrolliertes Abliegen[41] = nein  -> rot -> 0 Punkte
        """
#checke ob Überhaupt was angeklickt wurde
        if ((self.Files[38] == True or self.Files[39] == True)
            and (self.Files[40] == True or self.Files[41] == True)):

#            Voabliegeverhalten[38] = ja & kontrolliertes Abliegen[40] = ja  -> grün -> 10 Punkte
            if (self.Files[38] == True and 
                self.Files[40] == True):
                Abliegeverhalten = 10
                pass
#            Voabliegeverhalten[39] = nein & kontrolliertes Abliegen[40] = ja  -> gelb -> 5 Punkte
            elif ((self.Files[39] == True and self.Files[40] == True) or 
#            Voabliegeverhalten[38] = ja & kontrolliertes Abliegen[41] = nein  -> gelb -> 5 Punkte
            (self.Files[38] == True and self.Files[41] == True)):
                Abliegeverhalten = 5
                pass
#            Voabliegeverhalten[39] = nein & kontrolliertes Abliegen[41] = nein  -> rot -> 0 Punkte
            elif (self.Files[39] == True and self.Files[41] == True):
                Abliegeverhalten = 0
                pass
#            else:
#                Abliegeverhalten =0
#                pass
        else:
            Abliegeverhalten = 0
            self.error ="keine Abliegeverhalten und oder Kontrolliertes Abliegeverhalten ausgwählt"
            pass

        return round(Abliegeverhalten, self.rounddigit)
    
    def MutterID_Umgaenglichkeit(self):
        """
        File[nummer] Siehe Save_v...py
        Zähle:
            Umgänglich 
            Wenig umgänglich 
            aggressiev
max. 1-mal leichtes VV -> grün -> 10 Punkte
min. 2-mal leichtes oder 1-mal starkes VV Punkte; max. 1-mal stakes VV -> gelb -> 5 Punkte
mehr als 1-mal starkes VV -> rot -> 0 Punkte
        """
 
# checke ob Verteidigungsverhalten angekreutzt wurde       
        if ((self.Files[54] == False and self.Files[55] == False and self.Files[56] == False) or #tag1
            (self.Files[57] == False and self.Files[58] == False and self.Files[59] == False) or   #tag2
            (self.Files[60] == False and self.Files[61] == False and self.Files[62]== False )):    #tag3
            Verteidigung_Nein = 0
            Verteidigung_Leicht = 0
            Verteidigung_Stark = 3
            self.error = "kein Verteidigungsverhalten angekreutzt"
#            print ("keins angekreutzt")
            pass
        else:
            #setze Zahler auf null
            Verteidigung_Nein = 0
            Verteidigung_Leicht = 0            
            Verteidigung_Stark = 0

            for zz in (self.Files[54],  #Verteidigung Tag 1 Nein
                       self.Files[57],  #Verteidigung Tag 2 Nein
                       self.Files[60]): #Verteidigung Tag 3 Nein
                if zz == True:
                    Verteidigung_Nein+= 1
                    pass
                pass
            for kk in (self.Files[55],  #Verteidigung Tag 1 Leicht
                       self.Files[58],  #Verteidigung Tag 2 Leicht
                       self.Files[61]): #Verteidigung Tag 3 Leicht
                if kk == True:
                    Verteidigung_Leicht+= 1
                    pass
                pass
            
            for kk in (self.Files[56],   #Verteidigung Tag 1 Stark
                       self.Files[59],   #Verteidigung Tag 2 Stark
                       self.Files[62]): #Verteidigung Tag 3 Stark
                if kk == True:
                    Verteidigung_Stark+= 1
                    pass
                pass
 
#max. 1-mal leichtes VV -> grün -> 10 Punkte
        if (Verteidigung_Leicht <=1 and Verteidigung_Stark ==0):
            Verteidigungsverhalten = 10
            pass
#min. 2-mal leichtes oder 1-mal starkes VV Punkte; max. 1-mal stakes VV -> gelb -> 5 Punkte
        elif ((Verteidigung_Leicht >=2 or Verteidigung_Stark ==1 ) and Verteidigung_Stark <=1):
            Verteidigungsverhalten = 5
            pass
#mehr als 1-mal starkes VV -> rot -> 0 Punkte
        elif Verteidigung_Stark >= 2:
            Verteidigungsverhalten = 0
            pass
        return round(Verteidigungsverhalten, self.rounddigit)
        pass