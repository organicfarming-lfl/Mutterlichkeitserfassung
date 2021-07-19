#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 16:14:48 2020

title           :Ausgabe_v07.py
description     :Ausgabe des Muetterlichkeitsindex und der Ampel
author          :Jonas Müller
e-mail          :Mueller.M.Jonas@gmx.de
date            :13.04.2021
version         :00.07
usage           :python pyscript.py
notes           :
python_version  :3.7.3
"""
#import sys
#import os
##GuI Libs
##import PyQt5.QtCore as core
##import PyQt5.QtWidgets as widgets
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5 import QtCore

class Ausgabe:
    def __init__(self, Ausgabe_UI):
        self.Ausgabe=Ausgabe_UI
        pass
    
    def Ausgabe_Anzeige(self, Files):
        
#        lade Ausgabe Datein
        # print (Files)
        Widget_List = [self.Ausgabe.widget_Leistung_Green, 
                self.Ausgabe.widget_Leistung_Yellow, 
                self.Ausgabe.widget_Leistung_Red, 
                self.Ausgabe.widget_Geburt_Green,
                self.Ausgabe.widget_Geburt_Yellow,
#                self.Ausgabe.widget_Geburt_Orange,
                self.Ausgabe.widget_Geburt_Red, 
                self.Ausgabe.widget_Wurf_Green, 
                self.Ausgabe.widget_Wurf_Yellow, 
                self.Ausgabe.widget_Wurf_Red,
                self.Ausgabe.widget_Fitness_Green, 
                self.Ausgabe.widget_Fitness_Yellow, 
                self.Ausgabe.widget_Fitness_Red, 
                self.Ausgabe.widget_Abliegeverhalten_Green, 
                self.Ausgabe.widget_Abliegeverhalten_Yellow, 
                self.Ausgabe.widget_Abliegeverhalten_Red, 
                self.Ausgabe.widget_Umgaenglichkeit_Green,
                self.Ausgabe.widget_Umgaenglichkeit_Yellow, 
                self.Ausgabe.widget_Umgaenglichkeit_Red]
        laenge = 6

        Ampel_Range = [4,6,     #leistung
                        3.3, 6.7, #geburt 10/3, 20/3
                        4,6, #Wurf
                        4,6, #fitness
                        4,6, #abliegeverhalten 
                        4,6  #umgänglichkeit
                        ]
        Widget_index = 0
        for xx in range(0, laenge):
            Min = xx*2
            Max = xx*2+1
            File_Index = 64+xx
            Color = self.Ampel(Files[File_Index],Ampel_Range[Min], Ampel_Range[Max]) #file, Min, Max
            # print (xx, Color)
            for yy in range (len(Color)):
# =============================================================================

                Layout = Widget_List[Widget_index].parent().layout()
                # Widget_List[xx]== Layout.replaceWidget(Widget_List[Widget_index], LED(Color[yy]))
                Widget_List[Widget_index]== Layout.replaceWidget(Widget_List[Widget_index], LED(Color[yy]))
                Widget_index +=1

# =============================================================================
                
                
                # Widget_List[xx].clear()         #clear all stuff from bevore
                # Layout = Widget_List[Widget_index].parent().layout()
                # Layout = Widget_List[Widget_index].addChildLayoutItem()
                # Widget_List[xx]== Layout.replaceWidget(Widget_List[Widget_index], LED(Color[yy]))
                # Widget_List[xx]== Layout.addWidget(LED(Color[yy]))
                # Widget_List[xx].update()
                # Widget_List[xx]=Widget_List[xx].addChildLayoutItem(LED(Color[yy]))
                
                # Widget_List[Widget_index].setChild(None)        #clear all stuff from before        
                
                
                # layout = QtWidgets.QVBoxLayout()
                # Widget_List[Widget_index].clearLayout()
                
                # widget = layout.addWidget(LED(Color[yy]))
                # Widget_List[xx].addWidget(widget)
                
                # Ausgabe_tableWidget = QtWidgets.QTableWidget()
                # Widget_List[xx].setWidget(Color[yy])
# =============================================================================

#                 layout = QtWidgets.QVBoxLayout()
#                 layout.addWidget((LED(Color[yy])))
#                 if Widget_List[Widget_index].count() != 1:
# #            es wurde schon ein widget angelegt. lösche dieses
#                     Widget_List[Widget_index].removeWidget(layout)
#                     Widget_List[Widget_index].setLayout(layout)
#                 else:
#                     Widget_List[Widget_index].setLayout(layout)
#                 # Widget_List[Widget_index].repaint()
#                 # Widget_index +=1
                
# =============================================================================


#       set Muetterlichkeitsindex 
        if Files[75]==None:
            pass
        else:
            self.Ausgabe.lineEdit_Muetterlichkeitsindex.setText(str(Files[76]))  
        pass



    def Ampel(self, Input, Min = 3.3, Max = 6.7):
        '''
        Nimmt den Input und vergleicht ihn mit den Min Max Werten und 
        Gibt eine Liste Mit den Fraben für die Anzeige Ampel zurück
        '''
        
        if Input >= Min:
            if Input > Max: #green
                Color = ['green', 'grey', 'grey']
            if Input <=Max:   #yellow
                Color = ['grey', 'yellow', 'grey']
        else: #red
            
            Color =['grey', 'grey','red']
        return Color


class LED(QtWidgets.QWidget):
    '''
    LED Widget mit default Color Grey
    '''
    def __init__(self, color='grey', size_l= 25, size_r = 25, size_diam=50):
        super().__init__()
        self.color = color
        self.size_l = size_l
        self.size_r = size_r
        self.size_diam = size_diam
        # print (color)
        canvas = QtGui.QPixmap(50, 50)

        
        self.label = QtWidgets.QLabel()
        self.label.setPixmap(canvas)
#                
    def paintEvent(self,e):
        painter = QtGui.QPainter(self)        
        pen = QtGui.QPen()
        pen.setWidth(3)
        pen.setColor(QtGui.QColor('grey'))
        painter.setPen(pen)
        # painter.erase()
        #füllt die Innenflächen
        brush = QtGui.QBrush()
        brush.setColor(QtGui.QColor(str(self.color)))
        brush.setStyle(QtCore.Qt.SolidPattern)
        painter.setBrush(brush)
        #Malt den Kreis
#        painter.drawEllipse(5, 5, 7, 7)
        painter.drawEllipse(self.size_l, self.size_r, self.size_diam, self.size_diam)
        painter.end()