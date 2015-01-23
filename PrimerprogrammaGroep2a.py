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

class PrimerProg(wx.App):
    """Klasse roept alles aan."""
    def OnInit(self):
        self.SchermCounter = 0
        self.SchermLijst = [BeginScherm, InvoerScherm, OptieScherm]
        self.SchermBeheer()
        self.Bind(wx.EVT_BUTTON, self.KnopBeheer)
        self.seq = ''
        return True
    
    def SchermBeheer(self):
        if self.SchermCounter == 2:
            self.frame = self.SchermLijst[self.SchermCounter](None, seq=self.seq)
        else:
            self.frame = self.SchermLijst[self.SchermCounter](None)

    def KnopBeheer(self, event):
        EventID = event.GetId()
        
        if EventID == self.frame.GetDoorgaan():
            if self.SchermCounter == 1:
                self.seq = self.frame.GetSeq()
            self.SluitScherm()
        elif EventID == self.frame.GetHelp():
            print 'open helpscherm'
        

    def SluitScherm(self):
        self.frame.Destroy()
        self.SchermCounter += 1
        self.SchermBeheer()

    

app = PrimerProg(False)
app.MainLoop()
