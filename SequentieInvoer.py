"""
Sebastiaan de Vriend 06-01-15 Sequentie invoer maken.

Script zorgt voor sequentie van gebruikert.
"""

import wx


from SubPaneel import SubPaneel

class SequentieInvoer(wx.Panel):
    def __init__(self, parent, id=wx.ID_ANY, size=wx.DefaultSize):
        self.SeqPan = wx.Panel.__init__(self, parent, id, size=size)
        
        self.uptext = wx.StaticText(self, id, 'Pasta hier je sequentie:')
        
        self.invoer = wx.TextCtrl(self)
        self.dtext = wx.StaticText(self, id, 'Of blader vanaf je pc:')
        self.bknop = wx.Button(self, id=-1, label='Bladeren')
        
        

        self.HBox = wx.BoxSizer(wx.HORIZONTAL)
        self.HBox.Add(self.dtext, 1, wx.ALL | wx.EXPAND)
        self.HBox.Add(self.bknop, 1, wx.ALL | wx.EXPAND)
        self.VBox = wx.BoxSizer(wx.VERTICAL)
        self.VBox.Add(self.uptext, 1, wx.ALL | wx.EXPAND)
        self.VBox.Add(self.invoer, 1, wx.ALL | wx.EXPAND)
        self.VBox.Add(self.HBox, 1, wx.ALL | wx.EXPAND)
        self.SetSizer(self.VBox)

    def GetBladeren(self):
        return self.bknop

    def GetTinvoer(self):
        return self.invoer
        
    
