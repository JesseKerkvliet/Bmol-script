"""
Sebastiaan de Vriend 26-01-2015 Script schrijven om de kleuren te fixen.

"""

import wx

from SubPaneel import SubPaneel

class Opties(wx.Panel):
    def __init__(self, parent, seq, id=wx.ID_ANY, size=wx.DefaultSize):
        self.OptiePan = wx.Panel.__init__(self, parent, id, size=size)
        self.Vbox = wx.BoxSizer(wx.VERTICAL)
        self.seq = wx.TextCtrl(self, style=(wx.TE_MULTILINE| wx.TE_READONLY |
                                            wx.TE_NO_VSCROLL),
                               id=-1, value=seq)
        self.Vbox.Add(self.seq, 2, wx.ALL | wx.EXPAND)
        self.seq.Enable(False)
        sliderlijst = self.MaakSliders()
        
        self.MaakPL()
        #self.MaakGC()
        #self.MaakTM()
        for x in range(len(sliderlijst)):
            if x == 0:
                self.MaakBalk(sliderlijst[x], 'GC waardes:')
            else:
                self.MaakBalk(sliderlijst[x], 'TM waardes:')
            
        self.SetSizer(self.Vbox)

    def MaakSliders(self):
        self.MinGC = wx.Slider(self, value=55, minValue=40, maxValue=55,
                               style=wx.SL_LABELS)
        self.MaxGC = wx.Slider(self, value=60, minValue=60, maxValue=75,
                               style=wx.SL_LABELS)
        self.MinTM = wx.Slider(self, value=55, minValue=40, maxValue=55,
                               style=wx.SL_LABELS)
        self.MaxTM = wx.Slider(self, value=60, minValue=60, maxValue=75,
                               style=wx.SL_LABELS)
        return [[self.MinGC, self.MaxGC], [self.MinTM, self.MaxTM]]

    def MaakBalk(self, ls, naam):
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.AddSpacer(10)
        hbox.Add(self.MaakTekst(naam, 'l'), 0, wx.ALL |
                 wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL | wx.SHAPED)
        hbox.Add(self.MaakTekst('min', 'l'), 0, wx.ALL |
                 wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL | wx.SHAPED)
        hbox.AddSpacer(40)
        hbox.Add(ls[0], 1, wx.ALL )
        hbox.Add(self.TP(), 1, wx.ALL)
        hbox.Add(self.MaakTekst('max', 'l'), 0, wx.ALL |
                 wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL | wx.SHAPED)
        hbox.AddSpacer(40)
        hbox.Add(ls[1], 1, wx.ALL )
        hbox.AddSpacer(10)
        self.Vbox.Add(hbox, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL)
        
    def MaakGC(self):
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.AddSpacer(10)
        hbox.Add(self.MaakTekst('GC waardes:', 'l'), 0, wx.ALL |
                 wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL | wx.SHAPED)
        hbox.AddSpacer(1)
        hbox.Add(self.TP(), 1, wx.ALL)
        hbox.Add(self.MaakTekst('min', 'l'), 0, wx.ALL |
                 wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL | wx.SHAPED)
        
        hbox.AddSpacer(40)
        
        hbox.Add(self.MinGC, 1, wx.ALL )
        
        hbox.Add(self.TP(), 1, wx.ALL)
        hbox.Add(self.MaakTekst('max', 'l'), 0, wx.ALL |
                 wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL | wx.SHAPED)
        hbox.AddSpacer(40)
        hbox.Add(self.MaxGC, 1, wx.ALL )
        hbox.AddSpacer(10)
        self.Vbox.Add(hbox, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL)

    def MaakTM(self):
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.AddSpacer(10)
        hbox.Add(self.MaakTekst('TM waardes:', 'l'), 0, wx.ALL |
                 wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL | wx.SHAPED)
        hbox.Add(self.TP(), 1, wx.ALL)
        hbox.Add(self.MaakTekst('min', 'l'), 0, wx.ALL |
                 wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL | wx.SHAPED)
        
        hbox.AddSpacer(40)

        hbox.Add(self.MinTM, 1, wx.ALL)
        hbox.Add(self.TP(), 1, wx.ALL)
        
        hbox.Add(self.MaakTekst('max', 'l'), 0, wx.ALL |
                 wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL | wx.SHAPED)
        hbox.AddSpacer(40)
        hbox.Add(self.MaxTM, 1, wx.ALL)
        hbox.AddSpacer(10)
        self.Vbox.Add(hbox, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL)

    def TP(self):
        return SubPaneel(self)

    def MaakTekst(self, tekst, optie):
        if optie == 'l':
            allign = wx.StaticText(self, id=-1, label=tekst,
                                   style= wx.ALIGN_LEFT)
        elif optie == 'r':
            allign = wx.StaticText(self, id=-1, label=tekst,
                                   style= wx.ALIGN_RIGHT)
        return allign
    
    def MaakPL(self):
        """
        Input: 0
        De functie maakt een horizontale boxsizer aan en maakt daarna
        een static text aan en een Slider. Vervolgens wordt de text in
        de habox gezet en rechts in het midden gealligned.
        Daarna wordt er een spacer toegevoegd voor extra ruimte en
        wordt de slider toegevoegd met weer een spacer. Als laatste
        wordt de hbox toegevoegd aan de vertical boxsizer.
        """
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        text = wx.StaticText(self, id=-1, label='Primer Lengte:',
                             style= wx.ALIGN_LEFT)
        self.PrimerLen = wx.Slider(self, value=20, minValue=10, maxValue=30,
                                   style=wx.SL_LABELS, name='Primer lengte:')
        hbox.AddSpacer(10)
        hbox.Add(text, 0, wx.ALL  | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL |
                 wx.SHAPED)
        hbox.AddSpacer(5) 
        hbox.Add(self.PrimerLen, 6, wx.ALL  )
        hbox.AddSpacer(5)
        self.Vbox.Add(hbox, 0, wx.ALL |wx.EXPAND )
