"""
Sebastiaan de Vriend 23-01-2015 Maken optiescherm.

"""

import wx

from SubPaneel import SubPaneel
from KnoppenPaneel import KnoppenPaneel


class OptieScherm(wx.Frame):

    def __init__(self, parent, id=wx.ID_ANY, title='Primer_programma',
                 pos=wx.DefaultPosition, size=(700,700),
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
        self.Knop = KnoppenPaneel(self)
        self.Vbox.Add(self.seq, 8, wx.ALL | wx.EXPAND)
        self.Vbox.Add(self.Knop, 2, wx.ALL | wx.EXPAND)
        
                               

        self.SetSizer(self.Vbox)
        self.Show()

    def GetDoorgaan(self):
        return self.Knop.GetDoorgaan()
