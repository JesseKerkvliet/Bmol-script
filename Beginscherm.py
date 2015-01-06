"""
Sebastiaan de Vriend 05-01-2015 Begin maken met beginscherm.

Programma toon beginscherm voor primerprogramma.
"""

import wx

from SubPaneel import SubPaneel
from TekstPaneel import TekstPaneel
from KnoppenPaneel import KnoppenPaneel

class BeginScherm(wx.Frame):
    """
    De klasse maakt de frame 'Beginscherm' aan met daarin een
    welkoms boodschap. Meer informatie staat in de init documentatie.
    """
    def __init__(self, parent, id=wx.ID_ANY, title='Primer_programma',
                 pos=wx.DefaultPosition, size=(700,700),
                 style=wx.DEFAULT_FRAME_STYLE &~(wx.RESIZE_BORDER |
                                                  wx.CLOSE_BOX |
                                                  wx.SYSTEM_MENU),
                 name="PrimerScherm"):
        super(BeginScherm, self).__init__(parent, id, title, pos, size,
                                           style, name)
        self.MainPaneel = SubPaneel(self)
        Vbox = wx.BoxSizer(wx.VERTICAL)
        self.Text = TekstPaneel(self.MainPaneel, TekstTy=1)
        self.Knop = KnoppenPaneel(self.MainPaneel, vraag=True)
        Vbox.Add(self.Text, 1, wx.ALL | wx.EXPAND)
        Vbox.Add(self.Knop, 4, wx.ALL | wx.EXPAND)
        self.MainPaneel.SetSizer(Vbox)
        self.Show()
    
        
    def GetDoorgaan(self):
        return self.Knop.GetDoorgaan()
    
if __name__ == "__main__":
    app = wx.App(False)
    frame = BeginScherm(None)
    app.MainLoop()
