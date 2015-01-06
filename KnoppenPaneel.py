"""
Sebastiaan de Vriend 06-01-15 Begin maken met knoppen paneel.

Script maakt een knoppenpaneel aan.
"""

import wx
from SubPaneel import SubPaneel

class KnoppenPaneel(wx.Panel):
    """
    Class maakt knoppen paneel aan. Heeft mogelijkheid om ID's
    op te vragen.
    """
    def __init__(self, parent, id=wx.ID_ANY, size=wx.DefaultSize, vraag=False):
        self.KnopPaneel = wx.Panel.__init__(self, parent, id, size=size)
        self.HBox = wx.BoxSizer(wx.HORIZONTAL)
        self.Doorgaan = wx.Button(self, id=-1, label='Doorgaan')
        self.HBox.Add(self.Doorgaan, 1, wx.ALL | wx.EXPAND)
        self.HBox.Add(self.TussenPaneel(), 1, wx.ALL | wx.EXPAND)
        if vraag:
            self.Vraag = wx.Button(self, id=-1, label='Help')
            self.HBox.Add(self.Vraag, 1, wx.ALL | wx.EXPAND)
            self.HBox.Add(self.TussenPaneel(), 1, wx.ALL | wx.EXPAND)
        self.Stop = wx.Button(self, id=-1, label='Afsluiten')
        self.HBox.Add(self.Stop, 1, wx.ALL | wx.EXPAND)
        self.SetSizer(self.HBox)
        

    def GetDoorgaan(self):
        return self.Doorgaan.GetId()

    def TussenPaneel(self):
        return SubPaneel(self)
    
        
        
        
