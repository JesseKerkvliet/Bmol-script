"""
Sebastiaan de Vriend 23-01-2015 Maken optiescherm.

"""

import wx

from SubPaneel import SubPaneel
from KnoppenPaneel import KnoppenPaneel


class OptieScherm(wx.Frame):

    def __init__(self, parent, id=wx.ID_ANY, title='Primer_programma',
                 pos=wx.DefaultPosition, size=(600,450),
                 style=wx.DEFAULT_FRAME_STYLE &~(wx.RESIZE_BORDER |
                                                  wx.CLOSE_BOX |
                                                  wx.SYSTEM_MENU),
                 name="PrimerScherm", seq=''):
        super(OptieScherm, self).__init__(parent, id, title, pos, size,
                                           style, name)
        self.MainPaneel = SubPaneel(self)
        self.Vbox = wx.BoxSizer(wx.VERTICAL)
        self.seq = wx.TextCtrl(self, style=(wx.TE_MULTILINE | wx.TE_READONLY |
                                            wx.TE_NO_VSCROLL),
                               id=-1, value=seq)
        self.seq.Enable(False)
        self.Knop = KnoppenPaneel(self)
        self.Vbox.Add(self.seq, 8, wx.ALL | wx.EXPAND)
        self.MaakPL()
        self.MaakGC()
        self.MaakTM()
        self.Vbox.Add(self.Knop, 0.5, wx.ALL | wx.EXPAND)
        
                               

        self.SetSizer(self.Vbox)
        self.Show()


    def MaakPL(self):
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        text = wx.StaticText(self, label='Primer Lengte')
        
        self.PrimerLen = wx.Slider(self, value=20, minValue=10, maxValue=30,
                                   style=wx.SL_LABELS, name='Primer lengte:')
        hbox.Add(text, 1, wx.ALL | wx.EXPAND)
        hbox.Add(self.PrimerLen, 5, wx.ALL | wx.EXPAND)
        
        self.Vbox.Add(hbox, 1, wx.ALL | wx.EXPAND)
        
    def MaakGC(self):
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        text = wx.StaticText(self, label= 'GC waardes')
        mintext = wx.StaticText(self, label = 'min')
        self.MinGC = wx.Slider(self, value=55, minValue=40, maxValue=55,
                               style=wx.SL_LABELS)
        maxtext = wx.StaticText(self, label='max')
        self.MaxGC = wx.Slider(self, value=60, minValue=60, maxValue=75,
                               style=wx.SL_LABELS)
        hbox.Add(text, 1, wx.ALL | wx.EXPAND)
        hbox.Add(SubPaneel(self), 1, wx.ALL | wx.EXPAND)
        hbox.Add(mintext, 1, wx.ALL | wx.EXPAND)
        hbox.Add(self.MinGC, 1, wx.ALL | wx.EXPAND)
        hbox.Add(maxtext, 1, wx.ALL | wx.EXPAND)
        hbox.Add(self.MaxGC, 1, wx.ALL | wx.EXPAND)
        self.Vbox.Add(hbox, 1, wx.ALL | wx.EXPAND)


    def MaakTM(self):
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        text = wx.StaticText(self, label= 'GC waardes')
        mintext = wx.StaticText(self, label = 'min')
        self.MinTM = wx.Slider(self, value=55, minValue=40, maxValue=55,
                               style=wx.SL_LABELS)
        maxtext = wx.StaticText(self, label='max')
        self.MaxTM = wx.Slider(self, value=60, minValue=60, maxValue=75,
                               style=wx.SL_LABELS)
        hbox.Add(text, 1, wx.ALL | wx.EXPAND)
        hbox.Add(SubPaneel(self), 1, wx.ALL | wx.EXPAND)
        hbox.Add(mintext, 1, wx.ALL | wx.EXPAND)
        hbox.Add(self.MinTM, 1, wx.ALL | wx.EXPAND)
        hbox.Add(maxtext, 1, wx.ALL | wx.EXPAND)
        hbox.Add(self.MaxTM, 1, wx.ALL | wx.EXPAND)
        self.Vbox.Add(hbox, 1, wx.ALL | wx.EXPAND)


        self.Vbox.Add(hbox, 1, wx.ALL | wx.EXPAND)
    def GetDoorgaan(self):
        return self.Knop.GetDoorgaan()

    def GetSettingVal(self):
        pl = self.PrimerLen.GetValue()
        
