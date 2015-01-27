"""
Sebastiaan de Vriend 23-01-2015 Maken optiescherm.

"""

import wx

from SubPaneel import SubPaneel
from KnoppenPaneel import KnoppenPaneel
from Opties import Opties


class OptieScherm(wx.Frame):
    """De classe maakt de frame aan voor het optiescherm. zie init
       voor meet informatie"""
    def __init__(self, parent, id=wx.ID_ANY, title='Primer_programma',
                 pos=wx.DefaultPosition, size=(600,350),
                 style=wx.DEFAULT_FRAME_STYLE &~(wx.RESIZE_BORDER |
                                                  wx.CLOSE_BOX |
                                                  wx.SYSTEM_MENU),
                 name="PrimerScherm", seq=''):
        """
        """
        super(OptieScherm, self).__init__(parent, id, title, pos, size,
                                           style, name)
        self.MainPaneel = SubPaneel(self, id=-1)
        self.Vbox = wx.BoxSizer(wx.VERTICAL)
        self.Knop = KnoppenPaneel(self, vraag=True)
        self.Opties = Opties(self, seq)
        self.Vbox.Add(self.Opties, 1, wx.ALL | wx.EXPAND)
        self.Vbox.Add(self.Knop, 0, wx.ALL | wx.EXPAND)
        self.SetSizer(self.Vbox)
        self.Vbox.Fit(self)
        self.Show(True)
        

    def GetDoorgaan(self):
        """Functie returnt id van Knop.GetDoorgaan()."""
        return self.Knop.GetDoorgaan()

    def GetSettingVal(self):
        pass

    def GetHelp(self):
        """Functie returnt id van Knop.GetHelp()."""
        return self.Knop.GetHelp()


if __name__ == '__main__':
    app = wx.App(False)
    OptieScherm(None, -1, seq='atcg')
    app.MainLoop()
