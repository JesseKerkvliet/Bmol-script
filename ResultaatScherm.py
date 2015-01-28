"""
Sebastiaan de Vriend 27-01-2015 maken resultaatscherm.

"""

import wx

from KnoppenPaneel import KnoppenPaneel
from PrimerPaneel import PrimerPaneel
from SubPaneel import SubPaneel
from TekstPaneel import TekstPaneel


class ResultaatScherm(wx.Frame):

    def __init__(self, parent, id=wx.ID_ANY, title='Primer_programma',
                 pos=wx.DefaultPosition, size=(600, 350),
                 style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER |
                                                  wx.CLOSE_BOX |
                                                  wx.SYSTEM_MENU),
                 name="PrimerScherm", primers=[], seq=''):
        super(ResultaatScherm, self).__init__(parent, id, title, pos, size,
                                          style, name)
        self.MainPaneel = SubPaneel(self, id=-1)
        self.Vbox = wx.BoxSizer(wx.VERTICAL)
        if len(primers[0]) == 0 or len(primers[1]) == 0:
            self.tekst = TekstPaneel(self, TekstTy=2)
            self.Vbox.Add(self.tekst, 1, wx.ALL | wx.EXPAND)
        else:
            self.Vbox.Add(PrimerPaneel(self, primers, seq))
        self.Knop = KnoppenPaneel(self, knaam='Opnieuw')
        
        self.Vbox.Add(self.Knop, 0, wx.ALL | wx.EXPAND)
        self.SetSizer(self.Vbox)
        self.Vbox.Fit(self)
        self.Show()

    def GetDoorgaan(self):
        return self.Knop.GetDoorgaan()