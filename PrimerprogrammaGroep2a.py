"""
Sebastiaan de Vriend 06-01-2015 Controller maken.

Programma toont de schermen en roept de overige scripten aan.
Ook koppelt het programma alles aan elkaar.
"""

import wx

from Beginscherm import BeginScherm

class PrimerProg(wx.App):
    """Klasse roept alles aan."""
    def OnInit(self):
        self.SchermCounter =0
        self.SchermLijst = [BeginScherm]
        self.SchermBeheer()
        self.Bind(wx.EVT_BUTTON, self.KnopBeheer)
        return True

    def SchermBeheer(self):
        self.frame = self.SchermLijst[self.SchermCounter](None)

    def KnopBeheer(self, event):
        EventID = event.GetId()
        print EventID
        if EventID == self.frame.GetDoorgaan():
            print 'doorgaan'

    def SluitScherm(self):
        self.frame.Destroy()
        self.SchermCounter += 1
        self.SchermBeheer()

app = PrimerProg(False)
app.MainLoop()
