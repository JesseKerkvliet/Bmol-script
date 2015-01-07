"""
Sebastiaan de Vriend 06-01-2015 Invoer scherm maken.

Script toont invoer scherm met diverse opties en mogelijkheden.
"""

import wx
import os

from KnoppenPaneel import KnoppenPaneel
from SubPaneel import SubPaneel
from SequentieInvoer import SequentieInvoer

class InvoerScherm(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY, title='Shreck is dreck',
                 pos=wx.DefaultPosition, size=(800, 450),
                 style=wx.DEFAULT_FRAME_STYLE &~(wx.RESIZE_BORDER |
                                                 wx.CLOSE_BOX |
                                                 wx.SYSTEM_MENU),
                 name='ogre'):
        super(InvoerScherm, self).__init__(parent, id, title, pos, size,
                                           style, name)
        self.MainPaneel = SubPaneel(self)
        self.Vbox = wx.BoxSizer(wx.VERTICAL)
        self.Knoppen = KnoppenPaneel(self, vraag=True)
        self.seq = SequentieInvoer(self)
        self.Bind(wx.EVT_BUTTON, self.Openen, self.seq.GetBladeren())
        self.Vbox.Add(self.seq, 1, wx.ALL | wx.EXPAND)
        self.Vbox.Add(self.Knoppen, 1, wx.ALL | wx.EXPAND)
        self.SetSizer(self.Vbox)
        self.Show()

    def GetDoorgaan(self):
        return self.Knoppen.GetDoorgaan()

    def GetHelp(self):
        return self.Knoppen.GetHelp()


    def Openen(self, event):
        print 'bladeren'
        wildcard = """Fasta(*.fa)|*.fa|
Alle bestanden (*.*)|*.*""" 
        self.blad = wx.FileDialog(self, "woop", os.getcwd(), "",
                                  wildcard, wx.OPEN)
        if self.blad.ShowModal() == wx.ID_OK:
            filename = self.blad.GetPath()
            print filename
        self.blad.Destroy()
