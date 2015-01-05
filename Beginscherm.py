"""
Sebastiaan de Vriend 05-01-2015 Begin maken met beginscherm.

Programma toon beginscherm voor primerprogramma.
"""

import wx

from SubPaneel import SubPaneel
from TekstPaneel import TekstPaneel

class BeginScherm(wx.Frame):
    """
    De klasse maakt de frame 'Beginscherm' aan met daarin een
    welkoms boodschap. Meer informatie staat in de init documentatie.
    """
    def __init__(self, parent, id=wx.ID_ANY, title='Primer_programma',
                 pos=wx.DefaultPosition, size=(300,500),
                 style=wx.DEFAULT_FRAME_STYLE &~(wx.RESIZE_BORDER |
                                                  wx.CLOSE_BOX |
                                                  wx.SYSTEM_MENU),
                 name="PrimerScherm"):
        super(BeginScherm, self).__init__(parent, id, title, pos, size,
                                           style, name)
        self.MainPaneel = SubPaneel(self)
        Vbox = wx.BoxSizer(wx.VERTICAL)
        self.Text = TekstPaneel(self, TekstTy=1)
        self.MainPaneel.SetSizer(Vbox)
        self.Show()
    
        
        
    
if __name__ == "__main__":
    app = wx.App(False)
    frame = BeginScherm(None)
    app.MainLoop()
