# -*- coding: cp1252 -*-
"""
Sebastiaan de Vriend 06-01-2015 Controller maken.

Programma toont de schermen en roept de overige scripten aan.
Ook koppelt het programma alles aan elkaar.
"""

import wx



from Beginscherm import BeginScherm
from InvoerScherm import InvoerScherm
from OptieScherm import OptieScherm
from ResultaatScherm import ResultaatScherm

import Bmolscript

class PrimerProg(wx.App):
    """Klasse roept alles aan."""
    def OnInit(self):
        self.SC = 0
        self.SchermLijst = [BeginScherm, InvoerScherm, OptieScherm,
                            ResultaatScherm]
        self.SchermBeheer()
        self.Bind(wx.EVT_BUTTON, self.KnopBeheer)
        self.seq = ''
        #bla = 'atacacacacacacacacacacaacaccacaacaccacacaac'
        return True
          
    def SchermBeheer(self):
        naam = 'Primer generator 2.0'
        fmt = (600,350)
        if self.SC == 2:
            self.frame = self.SchermLijst[self.SC](None, seq=self.seq,
                                                   title=naam, size=fmt)
        elif self.SC == 3:
            self.frame = self.SchermLijst[self.SC](None, primers=self.res,
                                                   title=naam, size=fmt)
        else:
            self.frame = self.SchermLijst[self.SC](None, title=naam, size=fmt)

    def KnopBeheer(self, event):
        EventID = event.GetId()
        
        if EventID == self.frame.GetDoorgaan():
            if self.SC == 1:
                self.seq = self.frame.GetSeq().upper()
            elif self.SC == 2:
                self.info = self.frame.GetSettingVal()
                
                self.res = Bmolscript.main(self.info[2], self.info[1],
                                           self.info[0], self.seq)
                
            self.SluitScherm()
        elif EventID == self.frame.GetHelp():
            self.ShowMessage()
    
    def GetHelpFromReadme(self, tl):
        with open('README.txt', 'r') as f:
            data = f.readlines()
        go = False
        tekst = ''
        for regel in data:
            if regel[:-1] == tl[0]:
                go = True
            elif regel[:-1]== tl[1]:
                go = False
            if go:
                if regel[0] == '-' :
                    title = regel[1:-1]
                elif tl[0] not in regel and tl[1] not in regel:
                    tekst += regel
        return title, tekst
        
    def ShowMessage(self):
        if self.SC == 1:
            title, tekst = self.GetHelpFromReadme(['<<', '>>'])
        elif self.SC == 2:
            title, tekst = self.GetHelpFromReadme(['[[', ']]'])

        wx.MessageBox(tekst, title, 
            wx.OK | wx.ICON_INFORMATION)
    
    def SluitScherm(self):
        self.frame.Destroy()
        self.SC += 1
        self.SchermBeheer()

    

    

app = PrimerProg(False)
app.MainLoop()
