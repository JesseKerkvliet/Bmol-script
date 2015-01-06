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
    def __init__(self, parent, id=wx.ID_ANY, size=wx.DefaultSize):
        self.KnopPaneel = wx.Panel.__init(self, parent, id, size=size)
        
